from django.shortcuts import render

from catalog.models import Product, Contact


def home(request):
    five_products = Product.objects.all().order_by('-last_edited_date')[:5]
    product_content = {
        'prod_to_display': five_products
    }
    return render(request, "catalog/home.html", product_content)


def contacts(request):
    company_info = Contact.objects.all()
    info_content = {
        'info_list': company_info
    }
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone}): {message}")
    return render(request, "catalog/contacts.html", info_content)
