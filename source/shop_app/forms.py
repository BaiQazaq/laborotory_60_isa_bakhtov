from django import forms
from shop_app.models import Good


class GoodForm(forms.ModelForm):
    
    class Meta:
        model = Good
        fields = ('title', 'price', 'photo', 'balance', 'category', 'description')
        