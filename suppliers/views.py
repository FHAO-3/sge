from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms


class SupplierListView(LoginRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=Supplier"
        '''
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = models.Supplier
    form_class = forms.SupplierForm
    template_name = 'supplier_create.html'
    success_url = reverse_lazy('supplier_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'supplier_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Supplier
    form_class = forms.SupplierForm
    template_name = 'supplier_update.html'
    success_url = reverse_lazy('supplier_list')


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
