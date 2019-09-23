from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from items.models import Item


class ItemList(ListView):
    model = Item


class ItemView(DetailView):
    model = Item


class ItemCreate(CreateView):
    model = Item
    fields = ['category', 'title', 'price']
    success_url = reverse_lazy('item_list')


class ItemUpdate(UpdateView):
    model = Item
    fields = ['category', 'title', 'price']
    success_url = reverse_lazy('item_list')


class ItemDelete(DeleteView):
    model = Item
    success_url = reverse_lazy('item_list')