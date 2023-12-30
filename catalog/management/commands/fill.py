from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        #Позиции категорий для внесения в БД
        categories = [
            {'name': 'Соки', 'description': 'Длительного хранения'},
            {'name': 'Бакалея', 'description': 'Длительного хранения'},
            {'name': 'Мясо', 'description': 'Скоропортящееся'},
            {'name': 'Молочные продукты', 'description': 'Скоропортящееся'},
            {'name': 'Хлебобулочные изделия', 'description': 'Средний срок хранения'}
        ]


        Category.objects.all().delete()  #Обнуление базы категорий


        with connection.cursor() as cursor: #Переопределение нумерации в базе категорий с 1
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")


        categories_to_create = []  #Формирование списка категорий для внесения в базу
        for category in categories:
            categories_to_create.append(Category(**category))


        Category.objects.bulk_create(categories_to_create)    # Внесение категорий в базу данных

        # Позиции продуктов для внесения в БД
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


        Product.objects.all().delete()     #Обнуление базы продуктов

        with connection.cursor() as cursor:    #Переопределение нумерации в базе продуктов с 1
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")


        products_to_create = []    #Формирование списка продуктов для внесения в базу
        for product in products:
            products_to_create.append(Product(**product))


        Product.objects.bulk_create(products_to_create)  # Внесение продуктов в базу данных


