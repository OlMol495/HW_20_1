from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов
        ordering = ('name',)



class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование товара')
    description = models.TextField(**NULLABLE, verbose_name='Описание товара')
    item_pic = models.ImageField(upload_to="catalog/", verbose_name='Изображение товара', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    item_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу товара')
    created_date = models.DateField(verbose_name='Дата внесения товара в базу', **NULLABLE)
    last_edited_date = models.DateField(verbose_name='Дата последнего изменения', **NULLABLE)


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.item_price} {self.category} '

    class Meta:
        verbose_name = 'товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
        ordering = ('name', 'item_price')
