from django.forms import ModelForm
from app1.models import Product
class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields="__all__"
