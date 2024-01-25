from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy('materials:list')


class MaterialListView(ListView):
    model = Material


class MaterialDetailView(DetailView):
    model = Material


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy('material:list')
