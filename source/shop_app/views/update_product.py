from django.views.generic import UpdateView
from django.urls import reverse


from shop_app.models import Good
from shop_app.forms import GoodForm


class GoodUpdateView(UpdateView):
    template_name = 'update_product.html'
    form_class = GoodForm
    model = Good
    pk_url_kwarg = 'pk'
    context_object_name = 'good'
    
    def get_success_url(self):
        return reverse('page_show_good', kwargs={'pk': self.object.pk})