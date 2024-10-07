from django import forms
from .models import CarSan,VisaCard


class VisaCardForm(forms.ModelForm):
    class Meta:
        model = VisaCard
        fields = ['number', 'cvv', 'math', 'ysers', 'name']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'رقم البطاقة'}),
            'cvv': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'رقم الأمان'}),
            'math': forms.Select(attrs={'class': 'form-control'}),
            'ysers': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم صاحب البطاقة'}),
        }


class CarSanForm(forms.ModelForm):
    class Meta:
        model = CarSan
        fields = ['name', 'idnumber', 'mobile', 'email', 'country', 'platNo', 'car', 'scantpy', 'zone']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم'}),
            'idnumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهوية'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الموبايل'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'platNo': forms.TextInput(attrs={'class': 'form-control'}),
            'car': forms.Select(attrs={'class': 'form-control'}),
            'scantpy': forms.Select(attrs={'class': 'form-control'}),
            'zone': forms.Select(attrs={'class': 'form-control'}),
        }
