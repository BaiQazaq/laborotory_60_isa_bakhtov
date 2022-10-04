from django.shortcuts import render, get_object_or_404
from shop_app.models import Good


def product_view(request, pk):
    good = get_object_or_404(Good, pk=pk)
    return render(request, 'product.html', context={'good': good})