from django import forms
from django.forms import Textarea
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from shop_app.models import Good

def min_num_validator(num):
    print(num, int(num))
    if num < 1:
        raise ValidationError("Count in balance field can not be less than 1")
    return int

class GoodForm(forms.ModelForm):
    balance = (MinValueValidator(limit_value=1, message='Count in balance field can not be less than 1'),
               min_num_validator)
    
    class Meta:
        model = Good
        fields = ('title', 'price', 'photo', 'balance', 'category', 'description')
        help_texts = {
                'price' : ('Be careful to enter only numbers in this field'),
                'balance': ('Balance must be more than 0, otherwise product will not published'),
                'description': ('This fields not necesary, but extra information helps increase sales'),
                'category' : ('Choosing the right category helps the buyer when searching')
        }
        widgets = {
            'description': Textarea(attrs={'cols': 20, 'rows': 5}),
        }
        error_messages = {
            'title': {
                'required': ("Please let us know what for sale"),
            }
        }
        
class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')