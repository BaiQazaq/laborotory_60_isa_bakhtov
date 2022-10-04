# from django import forms
# from django.forms import widgets
# from django.core.exceptions import ValidationError
# from models import Good


# class GoodForm(forms.Form):
#     title = forms.CharField(label='Title', max_length=100, required=True)
#     description = forms.TextField(label='Description', max_length=2000, required=False)
#     photo = forms.CharField(label="Image", max_length=500, nrequired=False)
#     category = forms.CharField(label="Category", max_length=20, required=False)
#     balance = forms.PositiveIntegerField(label='Balance',required=True)
#     price = forms.DecimalField(label='Price', max_digits=7, required=True)
    
    
#     def clean_title(self):
#         title = self.cleaned_data.get('title')
#         if len(title) < 2:
#             raise ValidationError('Заголовок должен быть длинее 2x символов')
#         return title