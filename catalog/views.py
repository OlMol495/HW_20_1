from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from catalog.models import Product, Contact, Category


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {'title': 'Best Store Ever'}

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:3]
        return context_data

class ProductListView(ListView):
    model = Product
    extra_context = {'title': 'Каталог продуктов'}


class ProductDetailView(DetailView):
    model = Product
    extra_context = {'title': 'Детальная информация о товаре'}


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'item_price', 'category', 'item_pic',]
    success_url = reverse_lazy('catalog:catalog')



def contacts(request):
    company_info = Contact.objects.all()
    info_content = {
        'info_list': company_info,
        'title': 'Контакты'
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "catalog/contacts.html", info_content)




