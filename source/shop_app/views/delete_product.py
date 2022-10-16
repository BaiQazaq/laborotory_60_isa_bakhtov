from django.views.generic import DeleteView
from django.urls import reverse_lazy

from shop_app.models import Good


class GoodDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Good
    success_url = reverse_lazy('goods_page')
