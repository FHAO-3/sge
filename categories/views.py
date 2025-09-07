from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from rest_framework import generics

from . import models, forms, serializers


class CategoryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    # 'context_object_name' usado ao inves de mandar o `render`
    paginate_by = 10
    # 'paginate_by' não pode mostrar mais de (neste caso) 10 nomes da lista
    permission_required = 'categories.view_category'

    def get_queryset(self):
        '''
        Metodo sera usada para fazer requisições para pesquisar por `name` como por exemplo "url.com/?name=Category"
        '''
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CategoryCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('category_list')
    # reverse_lazy usado para evitar problemas de importação circular de urls e views no Django (é uma boa prática usar ele em class-based views)
    # 'category_list' é o nome da url que queremos redirecionar apos o form ser salvo com sucesso
    permission_required = 'categories.add_category'


class CategoryDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Category
    template_name = 'category_detail.html'
    permission_required = 'categories.view_category'


class CategoryUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    template_name = 'category_update.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.change_category'


class CategoryDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
    permission_required = 'categories.delete_category'


class CategoryCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializers


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializers
