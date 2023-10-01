from django import forms
from .models import cutie
class barbieform(forms.ModelForm):
    class Meta:
        model = cutie
        fields = ['name','price','style','img']
