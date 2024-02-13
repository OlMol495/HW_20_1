from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

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
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата внесения товара в базу', **NULLABLE)
    last_edited_date = models.DateField(auto_now=True, verbose_name='Дата последнего изменения', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Автор записи')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.item_price} {self.category} '

    class Meta:
        verbose_name = 'товар'  # Настройка для наименования одного объекта
        verbose_name_plural = 'товары'  # Настройка для наименования набора объектов
        ordering = ('-last_edited_date', 'name',)
        permissions = [
            ('change_published_status', 'Can change published'),
            ('change_product_description', 'Can change product description'),
            ('change_product_category', 'Can change product category')
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Наименование товара')
    version_number = models.CharField(max_length=20, verbose_name='Номер версии')
    name = models.CharField(max_length=150, verbose_name='Название версии')
    is_active = models.BooleanField(default=False, verbose_name='Активна')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """Класс отображения метаданных"""
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'


@receiver(post_save, sender=Version)
def set_active_version(sender, instance, **kwargs):
    """При установке флага версии в режим 'активна' версии, которые были активны до этого перестают быть активными"""
    if instance.is_active:
        Version.objects.filter(product=instance.product).exclude(pk=instance.pk).update(is_active=False)


class Contact(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название компании", **NULLABLE)
    phone = models.CharField(max_length=20, verbose_name='Телефон', **NULLABLE)
    email = models.CharField(max_length=200, verbose_name='Имейл', **NULLABLE)
    address = models.TextField(verbose_name='Адрес', **NULLABLE)
    ind_number = models.CharField(max_length=30, verbose_name='ИНН', **NULLABLE)

    def __str__(self):
        return f"{self.name}: {self.phone}, {self.email}, {self.address}, {self.ind_number}"

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
