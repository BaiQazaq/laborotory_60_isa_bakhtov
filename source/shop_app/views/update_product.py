from django.shortcuts import render, redirect, get_object_or_404

from shop_app.models import Good


def update_view(request, pk):
    errors = {}
    good = get_object_or_404(Good, pk=pk)
    if request.method == "POST":
        if not request.POST.get('title'):
            errors['title'] = 'Field is required'
        if not request.POST.get('balance'):
            errors['balance'] = 'Field is required'
        if not request.POST.get('price'):
            errors['price'] = 'Field is required'
        good.title = request.POST.get('title')
        good.description = request.POST.get('description')
        good.photo =request.POST.get('photo')
        good.category =request.POST.get('category')
        good.balance = request.POST.get('balance')
        good.price = request.POST.get('price')
        if errors:
            return render(
        request,
        'update_product.html',
        context={
            'good': good, 
            'errors': errors
            })
        good.save()
        return redirect('page_show_good', pk=good.pk)
    return render(
        request,
        'update_product.html',
        context={
            'good': good, 
            'errors': errors
            })
