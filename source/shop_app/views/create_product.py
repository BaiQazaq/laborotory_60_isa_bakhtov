from django.shortcuts import render, redirect
from shop_app.models import Good


def product_add_view(request):
    if request.method == "GET":
        context = {
            'categories': Good.CATEGORIES_VAR
        }
        return render(request, 'create_product.html', context)
    print("++++"*5, request.POST.get('category'))
    good_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'price': request.POST.get('price'),
        'photo': request.POST.get('photo'),
        'category': request.POST.get('category'),
        'balance': request.POST.get('balance')
    }
    good = Good.objects.create(**good_data)
    return redirect('page_show_good', pk=good.pk)


