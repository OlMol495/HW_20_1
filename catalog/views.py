from django.shortcuts import render

from catalog.models import Product


def five_product(request):
    five_products = Product.objects.all().order_by('-last_edited_date')[5:]
    print(five_products)
    return render(request, 'catalog/home.html')


