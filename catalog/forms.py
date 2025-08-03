from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from catalog.models import Product


minus_words = ['казино', 'биржа', 'обман', 'криптовалюта', 'дешево', 'полиция','крипта', 'бесплатно', 'радар']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'owner',)

    def clean_name(self):
        product_name = self.cleaned_data['name']
        if any(minus_word.lower() in product_name.lower() for minus_word in minus_words):
            raise ValidationError(f"В названии продукта нельзя использовать: {', '.join(minus_words)}")
        return product_name

    def clean_description(self):
        product_description = self.cleaned_data['description']
        if any(minus_word.lower() in product_description.lower() for minus_word in minus_words):
            raise ValidationError(f"В описании продукта нельзя использовать: {', '.join(minus_words)}")
        return product_description

    def clean_price(self):
        product_price = self.cleaned_data['price']
        if product_price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        return product_price


class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('published', )
