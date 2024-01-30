from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, HomeTemplateView, ProductListView, ProductDetailView, ProductCreateView, \
    ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts', contacts, name='contacts'),
    path('products', ProductListView.as_view(), name='catalog'),
    path("<int:pk>/product_detail/", ProductDetailView.as_view(), name="product_detail"),
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
]