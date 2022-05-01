from django import forms
from .models import Plato

class platoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = '__all__'
        
        # widgets = {
        #     'nombre': forms.CharField()
        # }