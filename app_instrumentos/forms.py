from django import forms
from .models import Instrumento

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['nombre', 'marca', 'modelo', 'precio_venta', 'categoria', 'foto_instrumento']