from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from rest_framework import generics

from . import models, forms, serializers


# OBSERVE QUE O `LoginRequiredMixin` ESTÁ ANTES DE `ListView` POIS TEM UMA ORDEM DE HERANÇA E É UMA VERIFICAÇÃO DE LOGIN
class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=brand"
        '''
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_create.html'
    success_url = reverse_lazy('brands_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'brands_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.change_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.delete_brand'


# Views API
class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializers
