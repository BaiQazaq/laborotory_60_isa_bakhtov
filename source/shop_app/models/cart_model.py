from django.db import models
from django.utils import timezone


class Cart(models.Model):
    count = models.PositiveIntegerField(verbose_name='Count',null=False, blank=False)
    good = models.ForeignKey('shop_app.Good', verbose_name='Product', related_name='carts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Date of creation', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Date of change', auto_now=True)
    is_deleted = models.BooleanField(verbose_name="Deleted", default=False, null=False)
    deleted_at = models.DateTimeField(verbose_name='Date of delete', null=True, default=None)
    

    def __str__(self):
        return f"{self.count} - {self.good}"        
    
    
    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()