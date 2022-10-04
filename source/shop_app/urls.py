from django.urls import path

from shop_app.views.show_products import products_view
from shop_app.views.product import product_view
from shop_app.views.create_product import product_add_view



urlpatterns = [
    path("", products_view, name='goods_page'),
    path("products/", products_view, name='goods_page'),
    path("products/<int:pk>", product_view, name='page_show_good'),
    path("products/add/", product_add_view, name='page_add_good'),
    
]