from django.db import models
from django.utils import timezone
from django.db.models import TextChoices


# Create your models here.
class CategoryChoices(TextChoices):
    PHONES = 'Phones', 'Телефоны'
    ACCUMULATORS = 'Accumulators', 'Аккумуляторы'
    NOTEBOOKS = 'Notebooks', 'Ноутбуки'
    OTHERS = 'Others', 'Другие'


class Good(models.Model):
    
    title = models.CharField(verbose_name='Title',max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Description',max_length=2000, null=True, default="No description")
    photo = models.CharField(verbose_name="Image", max_length=500, null=True, blank=False, default="No photo")
    category = models.CharField(verbose_name="Category", max_length=20, choices=CategoryChoices.choices, default=CategoryChoices.OTHERS)
    balance = models.PositiveIntegerField(verbose_name='Balance',null=False, blank=False)
    price = models.DecimalField(verbose_name='Price', max_digits=7, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)
    is_deleted = models.BooleanField(verbose_name="Deleted", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name='Date of delete', null=True, default=None)
    

    def __str__(self):
        return f"{self.title} - {self.description} - {self.price}"        
    
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()