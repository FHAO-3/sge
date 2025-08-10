from django.views.generic import ListView, CreateView
from . import models
from django.urls import reverse_lazy


class BrandListView(ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'  # usado ao inves de mandar o `render`

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
    form_class = ...
    template_name = 'brand_create.html'
    success_url = reverse_lazy('brands_list')
