from django.db import models

# Create your models here.
class Good(models.Model):
    CATEGORIES_VAR = (
        ('Ph', 'Phones'),
        ('Acc', 'Accumulators'),
        ('Nb', 'Notebooks'),
        ('O', 'Others') 
    )
    
    title = models.CharField(verbose_name='Title',max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Description',max_length=2000, null=True, default="No description")
    photo = models.CharField(verbose_name="Image", max_length=500, null=True, blank=False, default="No photo")
    category = models.CharField(verbose_name="Category", max_length=20, choices=CATEGORIES_VAR, default=CATEGORIES_VAR[3][1])
    balance = models.PositiveIntegerField(verbose_name='Balance',null=False, blank=False)
    price = models.DecimalField(verbose_name='Price', max_digits=7, decimal_places=2, null=False, blank=False)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.description} - {self.price}"