from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeTemplateView, ProductListView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('products', ProductListView.as_view(), name='catalog'),
    path("<int:pk>/product_detail/", ProductDetailView.as_view(), name="product_detail"),
]