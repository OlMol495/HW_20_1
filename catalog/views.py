from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

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




