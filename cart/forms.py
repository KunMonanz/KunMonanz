from django import forms
from item.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_phone_number', 'additional_order_phone_number', 'city', 'order_address', 'receipt']

    order_phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'Enter phone number', 'class': 'w-full py-4 px-6 rounded-xl mb-4'})
    )
    additional_order_phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={'placeholder': 'Enter additional phone number', 'class': 'w-full py-4 px-6 rounded-xl mb-4'})
    )
    city = forms.ChoiceField(
        choices=Order.CITY_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Select city', 'class': 'w-full py-4 px-6 rounded-xl mb-4'})
    )
    order_address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter delivery address', 'class': 'w-full py-4 px-6 rounded-xl mb-4'})
    )
    receipt = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'w-full py-4 px-6 rounded-xl mb-4'})
    )