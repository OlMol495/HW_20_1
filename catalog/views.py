from django.shortcuts import render

from catalog.models import Product, Contact, Category


def home(request):
    all_products = Product.objects.all()
    content = {
        'prod_to_display': all_products,
        'title': 'Best Store Ever'
    }
    return render(request, "catalog/home.html", content)


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


def product_detail(request, pk):
    one_product = Product.objects.filter(id=pk)
    content = {
        'prod_to_display': one_product,
        'title': 'Детальная информация о товаре'
    }
    return render(request, "catalog/product_detail.html", content)

