# forms.py

from django import forms
from .models import MedidasCliente, TabelaMedidas

class MedidasClienteForm(forms.ModelForm):
    class Meta:
        model = MedidasCliente
        fields = '__all__'

class TabelaMedidasForm(forms.Form):
    tabela_choices = [(tabela.id, tabela.nome) for tabela in TabelaMedidas.objects.all()]
    
    tabela = forms.ChoiceField(
        label='Selecione a tabela de medidas:',
        choices=tabela_choices,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )