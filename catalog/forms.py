from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price', 'publish_product']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите название товара'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Введите описание товара'})
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Выберете категорию товара'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Укажите стоимость товара'})

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']

        for word in forbidden_words:
            if word in name.lower():
                self.add_error('name', f'Наименование товара не может содержать слово {word}')
            elif word in description.lower():
                self.add_error('description', f'Описание товара не может содержать слово {word}')


class ProductModeratorForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['publish_product']

