from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (contacts, HomeTemplateView, ProductListView, ProductDetailView, ProductCreateView,
                           ProductUpdateView, CategoryListView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('products', ProductListView.as_view(), name='catalog'),
    path("<int:pk>/product_detail/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path('category/', CategoryListView.as_view(), name="category_list"),
]