from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from . import models, forms
from django.urls import reverse_lazy


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=brand"
        '''
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_create.html'
    success_url = reverse_lazy('brands_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'brands_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso


class BrandDetailView(DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'


class BrandUpdateView(UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brands_list')


class BrandDeleteView(DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brands_list')
