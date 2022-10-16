from shop_app.models import Good
from django.views.generic import DetailView


class GoodView(DetailView):
    template_name = 'product.html'
    model =  Good
    pk_url_kwarg = 'pk'