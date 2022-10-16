from django.urls import path

from shop_app.views.show_products import IndexView
from shop_app.views.product import GoodView
from shop_app.views.create_product import GoodCreate
from shop_app.views.update_product import GoodUpdateView
from shop_app.views.delete_product import delete_view, confirm_delete



urlpatterns = [
    path("", IndexView.as_view(), name='goods_page'),
    path("products/", IndexView.as_view(), name='goods_page'),
    path("products/<int:pk>", GoodView.as_view(), name='page_show_good'),
    path("products/add/", GoodCreate.as_view(), name='page_add_good'),

    path("product/<int:pk>/update/", GoodUpdateView.as_view(), name= "update_good"),
    path("product/<int:pk>/delete/", delete_view, name= "delete_good"),
    path("product/<int:pk>/confirm_delete/", confirm_delete, name= "confirm_delete")
]
