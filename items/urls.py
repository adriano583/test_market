from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', views.ItemList.as_view(), name='item_list'),
    path('item/<int:pk>', login_required(views.ItemView.as_view()), name='item_view'),
    path('new', login_required(views.ItemCreate.as_view()), name='item_new'),
    path('edit/<int:pk>', login_required(views.ItemUpdate.as_view()), name='item_edit'),
    path('delete/<int:pk>', login_required(views.ItemDelete.as_view()), name='item_delete'),
]