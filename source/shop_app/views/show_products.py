from django.shortcuts import render
from shop_app.models import Good
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'show_products.html'
    model = Good
    context_object_name = 'goods'
    ordering = ('-created_at',)
    # extra_context = {'aaa': 'bbb'}
    queryset = Good.objects.exclude(is_deleted=True)
    paginate_by = 4
    paginate_orphans = 1

