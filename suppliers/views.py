from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from rest_framework import generics

from . import models, forms, serializers


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista
    permission_required = 'suppliers.view_supplier'

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=Supplier"
        '''
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    form_class = forms.SupplierForm
    template_name = 'supplier_create.html'
    success_url = reverse_lazy('supplier_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'supplier_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso
    permission_required = 'suppliers.add_supplier'


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = 'supplier_detail.html'
    permission_required = 'suppliers.view_supplier'


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    form_class = forms.SupplierForm
    template_name = 'supplier_update.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'suppliers.change_supplier'


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier_list')
    permission_required = 'suppliers.delete_supplier'


# Views API
class SupplierCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializers


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = serializers.SupplierSerializers
