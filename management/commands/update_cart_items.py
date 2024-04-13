from django.core.management.base import BaseCommand
from cart.models import CartItem

class Command(BaseCommand):
    help = 'Updates the price of existing CartItem instances'

    def handle(self, *args, **options):
        cart_items = CartItem.objects.all()

        for cart_item in cart_items:
            cart_item.price = cart_item.item.price
            cart_item.save()

        self.stdout.write(self.style.SUCCESS('CartItem prices updated successfully.'))