from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category, Product


# class Products:
#     pass


class Command(BaseCommand):

    def handle(self, *args, **options):

        categories = [
            {'name': 'Соки', 'description': 'Длительного хранения'},
            {'name': 'Бакалея', 'description': 'Длительного хранения'},
            {'name': 'Мясо', 'description': 'Скоропортящееся'},
            {'name': 'Молочные продукты', 'description': 'Скоропортящееся'},
            {'name': 'Хлебобулочные изделия', 'description': 'Средний срок хранения'}
        ]

        Category.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

        categories_to_create = []
        for category in categories:
            categories_to_create.append(Category(**category))

        # Добавление категорий в базу данных
        Category.objects.bulk_create(categories_to_create)

        # Список продуктов для добавления в БД
        products = [
            {'name': 'Cушки', 'description': 'Пакет 400 гр',
             'category': categories_to_create[4], 'item_price': '28'},

            {'name': 'Йогурт', 'description': '100 гр',
             'category': categories_to_create[3], 'item_price': '50'},

            {'name': 'Кефир', 'description': 'Тетрапак 1 л',
             'category': categories_to_create[3], 'item_price': '120'},

            {'name': 'Мука ржаная', 'description': '1 кг',
             'category': categories_to_create[1], 'item_price': '100'},

            {'name': 'Свиная вырезка', 'description': 'Ваккуумная упаковка 500 гр',
             'category': categories_to_create[2], 'item_price': '100'},

            {'name': 'Манго сок', 'description': 'Стекло 750 мл',
             'category': categories_to_create[0], 'item_price': '100'}
        ]


        Product.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

        # Список экземпляров класса Product
        products_to_create = []
        for product in products:
            products_to_create.append(Product(**product))

        # Добавление продуктов в базу данных
        Product.objects.bulk_create(products_to_create)


# from django.core.management import BaseCommand
#
# from catalog.models import Product, Category
#
#
# class Command(BaseCommand):
#     def handle(self, *args, **options):
#         product_list = [
#             {'name': 'Cушки', 'category': 'Хлебобулочные изделия', 'item_price': '28'},
#             {'name': 'Йогурт', 'category': 'Молочные изделия', 'item_price': '50'},
#             {'name': 'Кефир', 'category': 'Молочные изделия', 'item_price': '120'},
#             {'name': 'Мука ржаная', 'category': 'Бакалея', 'item_price': '100'}
#         ]
#
#         products_to_create = []
#         for product_item in product_list:
#             products_to_create.append(
#                 Product(**product_item)
#             )
#
#         Product.objects.bulk_create(products_to_create)