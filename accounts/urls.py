from django.urls import path
from .views import change_password, password_change_done, MyPasswordResetView, MyPasswordResetDoneView, MyPasswordResetConfirmView, MyPasswordResetCompleteView

app_name = 'accounts'

urlpatterns = [
    # Other URL patterns
    path('change-password/', change_password, name='change_password'),
    path('password-change-done/', password_change_done, name='password_change_done'),
    path('password-reset/', MyPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]