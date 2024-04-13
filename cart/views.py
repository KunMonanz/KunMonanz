from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from item.models import Item, Order, OrderItem
from .models import Cart, CartItem
from django.contrib import messages
from .forms import OrderForm


def add_to_cart(request, item_id):
    # Get the item based on the item_id provided
    item = get_object_or_404(Item, pk=item_id)

    # Check if the user already has a cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the item is already in the user's cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, item=item)

    # If the item already exists in the cart, increment the quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request,"Item added to cart successfully")
    # Redirect the user to the cart page or any other desired page
    return redirect('/')

def remove_from_cart(request, item_id):
    # Get the item based on the item_id provided
    item = get_object_or_404(Item, pk=item_id)

    # Check if the user has a cart
    cart = get_object_or_404(Cart, user=request.user)

    # Check if the item exists in the user's cart
    cart_item = get_object_or_404(CartItem, cart=cart, item=item)

    # If the quantity is greater than 1, decrement the quantity
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # If the quantity is 1, remove the cart item from the cart
        cart_item.delete()

    # Redirect the user to the cart page or any other desired page
    return redirect('cart')

@login_required
def update_cart(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                cart_item_id = key.split('_')[1]
                quantity = value.strip()  # Remove leading/trailing whitespace
                if quantity.isdigit():
                    try:
                        cart_item = CartItem.objects.get(id=cart_item_id)
                        cart_item.quantity = int(quantity)
                        cart_item.save()
                    except CartItem.DoesNotExist:
                        messages.error(request, f'Cart item with ID {cart_item_id} does not exist.')
                else:
                    messages.error(request, f'Invalid quantity value for cart item with ID {cart_item_id}.')
        
        messages.success(request, f'Cart updated successfully.')
        return redirect('cart')
    
    else:
        return render(request, 'cart.html')


def cart(request):
    try:
        # Retrieve the user's cart
        cart = Cart.objects.get(user=request.user)

        # Get the cart items associated with the cart
        cart_items = cart.cartitem_set.all()

        context = {
            'cart': cart,
            'cart_items': cart_items
        }
        return render(request, 'cart/cart.html', context)
    
    except Cart.DoesNotExist:
        return render(request, 'cart/no_item_in_cart.html')
  
    
@login_required
def create_order(request):
    user_cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)

    form = OrderForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            user_orders = Order.objects.filter(user=request.user)
            if not user_orders.exists():
                order = form.save(commit=False)
                order.user = request.user
                order.save()
            else:
                order = user_orders.last()

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    item=cart_item.item,
                    quantity=cart_item.quantity,
                    price=cart_item.item.price,
                    total_amount=cart_item.item.price * cart_item.quantity
                )

            return render(request, 'cart/order_success.html')
    
    return render(request, 'cart/order_form.html', {'form': form})

def account_display(request):
    user_cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_price = sum(cart_item.item.price * cart_item.quantity for cart_item in cart_items)
    return render(request, 'cart/order.html', {'total_price': total_price, 'cart_items': cart_items})

@login_required
def order_success(request):
    return render(request, 'cart/order_success.html')


