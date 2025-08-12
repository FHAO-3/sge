from django.views.generic import ListView, CreateView, DetailView
from . import models, forms
from django.urls import reverse_lazy


class InflowListView(ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=Inflow"
        '''
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)
            # 'product__title__icontains' em `product` pega o `title` e filtra usando o `icontains` que seja igual ao `prodct` passado
        return queryset


class InflowCreateView(CreateView):
    model = models.Inflow
    form_class = forms.InflowForm
    template_name = 'inflow_create.html'
    success_url = reverse_lazy('inflow_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'inflow_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso


class InflowDetailView(DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'
