from django.views.generic import CreateView
from django.urls import reverse

from shop_app.models import Good
from shop_app.forms import GoodForm


class GoodCreate(CreateView):
    template_name = 'create_product.html'
    form_class = GoodForm
    model = Good
    context_object_name = 'good'
    
    def get_success_url(self):
        return reverse('page_show_good', kwargs={'pk': self.object.pk})
