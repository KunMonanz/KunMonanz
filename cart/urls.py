from django.urls import path
from .views import cart, add_to_cart, remove_from_cart, update_cart, order_success,create_order, account_display

app_name = 'cart'

urlpatterns = [
    path('cart/update/', update_cart, name='update_cart'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('create-order/', create_order, name='create_order'),
    path('order-success/', order_success, name='order_success'),
    path('account-disply/', account_display, name='account_display'),
]

