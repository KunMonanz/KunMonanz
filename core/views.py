from django.shortcuts import render, redirect, get_object_or_404
from item.models import Category, Item
from .forms import SignUpForm, SearchForm


def index(request):
    items = Item.objects.filter(is_sold=False)[0:8]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'core/index.html', context)


def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    items = Item.objects.filter(category=category)
    categories = Category.objects.all()
    context = {
        'category': category,
        'items': items,
        'categories': categories
    }
    return render(request, 'core/categories_view.html', context)


def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login/') 
    
    else:
        form = SignUpForm()
        
    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)


from django.db.models import Q

def search_view(request):
    query = request.GET.get('query', '')
    search_items = request.GET.get('search_items', False)
    search_categories = request.GET.get('search_categories', False)

    results = {'items': [], 'categories': []}

    if query:
        if search_items:
            items = Item.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            results['items'] = items

        if search_categories:
            categories = Category.objects.filter(name__icontains=query)
            results['categories'] = categories

    context = {'query': query, 'results': results}
    return render(request, 'core/search_results.html', context)