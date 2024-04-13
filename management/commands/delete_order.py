import item

records_to_delete = Order.objects.filter(receipt1__isnull=True)

records_to_delete.delete()