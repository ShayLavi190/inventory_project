from django.forms import ModelForm
from .models import User, Product, Transfers, Purchases, Expense
from django import forms


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class TransferForm(ModelForm):
    start_of_loan = forms.DateField(widget=DateInput)
    end_of_loan = forms.DateField(widget=DateInput)

    class Meta:
        model = Transfers
        fields = '__all__'


class PurchasesForm(ModelForm):
    class Meta:
        model = Purchases
        fields = '__all__'


class ExpenseForm(ModelForm):
    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Expense
        fields = '__all__'
