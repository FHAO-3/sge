from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from categories.models import Category
from brands.models import Brand
from . import models, forms
from app.metrics import get_product_metrics


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista
    permission_required = 'products.view_product'

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=product"
        '''
        queryset = super().get_queryset()
        # abaixo recebe as requisições feitas pelo usuario e filtramos
        brand = self.request.GET.get('brand')
        category = self.request.GET.get('category')
        serie_number = self.request.GET.get('serie_number')
        title = self.request.GET.get('title')

        # essas condiões abaixo verifica se tem alguma requisicão
        if brand:
            queryset = queryset.filter(brand__id=brand)

        if category:
            queryset = queryset.filter(category__id=category)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)

        if title:
            queryset = queryset.filter(title__icontains=title)

        # apos verificar e filtrar cada requisição vamos retornar as requições para o navegador
        return queryset

    def get_context_data(self, **kwargs):
        '''
        Pegar o contexto original do ListView (super().get_context_data(**kwargs)),
        Adicionar chaves extras (categories e brands) para que fiquem disponíveis no template.
        '''
        context = super().get_context_data(**kwargs)
        # `super().get_contex_data(**kwargs)` é o contexto original
        # abaixo estamos adicionano mais coisas ao contexto
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = get_product_metrics()
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'product_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso
    permission_required = 'products.add_product'


class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'
