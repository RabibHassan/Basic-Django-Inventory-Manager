from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,
        name='home'),
    path('create/',views.create_product,
        name='create_product'),
    path('list/',views.product_list_view,
        name='product_list'),
    path('update/<int:product_id>/',views.update_product,
    name='update_product'),
    path('delete/<int:product_id>/',views.delete_product,
        name='delete_product'),
]
