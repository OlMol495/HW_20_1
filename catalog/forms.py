from django import forms
from catalog.models import Product, Version

PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
class StyleFormMixin:
    """Миксин для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Product"""

    class Meta:
        model = Product
        fields = ('name', 'description', 'item_pic', 'category', 'item_price',)

    def clean_name(self):
        """Валидация поля name по запрещенным словам"""
        cleaned_data = self.cleaned_data.get('name')
        for word in PROHIBITED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Введено запрещенное к использованию слово')

        return cleaned_data

    def clean_description(self):
        """Валидация поля description по запрещенным словам"""
        cleaned_data = self.cleaned_data.get('description')
        for word in PROHIBITED_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Введено запрещенное к использованию слово')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Форма для модели Version"""

    class Meta:
        model = Version
        exclude = ('product',)


class ModeratorProductForm(ProductForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')
