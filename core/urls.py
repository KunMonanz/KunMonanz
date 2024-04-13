from django.urls import path
from django.contrib.auth import views as auth_views
from core.views import index, contact, signup, category_view, search_view
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', index, name="index"),
    path('contact/', contact, name="contact"),
    path('signup/', signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name="login"),
    path('category/<int:category_id>',category_view, name="categories_view" ),
    path('search/', search_view, name='search'),

]