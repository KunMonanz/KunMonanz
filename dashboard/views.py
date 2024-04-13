from django.shortcuts import render
from item.models import Item
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

@login_required
def index(request):
    items = Item.objects.filter(create_by=request.user)
    context = {'items': items}
    return render(request, 'dashboard/index.html', context)

