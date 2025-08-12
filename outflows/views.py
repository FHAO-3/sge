from django.views.generic import ListView, CreateView, DetailView
from . import models, forms
from django.urls import reverse_lazy


class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=outflow"
        '''
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)
            # 'product__title__icontains' em `product` pega o `title` e filtra usando o `icontains` que seja igual ao `prodct` passado
        return queryset


class OutflowCreateView(CreateView):
    model = models.Outflow
    form_class = forms.OutflowForm
    template_name = 'outflow_create.html'
    success_url = reverse_lazy('outflow_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'outflow_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso


class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
