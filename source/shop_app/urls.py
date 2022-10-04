from django.urls import path

from shop_app.views.show_products import products_view
from shop_app.views.product import product_view
from shop_app.views.create_product import product_add_view
from shop_app.views.update_product import update_view
from shop_app.views.delete_product import delete_view, confirm_delete



urlpatterns = [
    path("", products_view, name='goods_page'),
    path("products/", products_view, name='goods_page'),
    path("products/<int:pk>", product_view, name='page_show_good'),
    path("products/add/", product_add_view, name='page_add_good'),

    path("product/<int:pk>/update/", update_view, name= "update_good"),
    path("product/<int:pk>/delete/", delete_view, name= "delete_good"),
    path("product/<int:pk>/confirm_delete/", confirm_delete, name= "confirm_delete")
]
