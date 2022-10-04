from django.shortcuts import render
from shop_app.models import Good

def products_view(request):
    goods = Good.objects.all()
    context = {
        "goods": goods
    }
    return render(request, 'show_products.html', context)