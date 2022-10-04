from django.shortcuts import render, redirect, get_object_or_404

from shop_app.models import Good



def delete_view(request, pk):
    good = get_object_or_404(Good, pk=pk)
    good.delete()
    return render(request, 'product_confirm_delete.html', context={'good': good})


def confirm_delete(request, pk):
    good = get_object_or_404(Good, pk=pk)
    good.delete()
    return redirect('goods_page')