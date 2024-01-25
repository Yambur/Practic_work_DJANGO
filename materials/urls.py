from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialCreateView, MaterialListView, MaterialDetailView

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    path('', MaterialListView.as_view(), name='list'),
    path('edit/<int:pk>/', MaterialDetailView.as_view(), name='edit'),
    #path('delete/<int:pk>/', ..., name='delete'),x`
]
