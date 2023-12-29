from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {'name': 'Cушки', 'category': 'Хлебобулочные изделия', 'item_price': '28'},
            {'name': 'Йогурт', 'category': 'Молочные изделия', 'item_price': '50'},
            {'name': 'Кефир', 'category': 'Молочные изделия', 'item_price': '120'},
            {'name': 'Мука ржаная', 'category': 'Бакалея', 'item_price': '100'}
        ]

        products_to_create = []
        for product_item in product_list:
            products_to_create.append(
                Product(**product_item)
            )

        Product.objects.bulk_create(products_to_create)