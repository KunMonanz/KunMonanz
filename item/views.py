from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm
from django.contrib.auth import logout
from django.contrib import messages

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, 'item/detail.html', context)

@login_required
def new(request):
    if request.method == 'POST': 
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.create_by = request.user
            item.save()
            
            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()
    
    return render(request, 'item/form.html', {
                'form': form,
                'title': 'New Item',
            })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, create_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("/")