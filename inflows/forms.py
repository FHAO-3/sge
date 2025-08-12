from django import forms
from inflows.models import Inflow


class InflowForm(forms.ModelForm):
    class Meta:
        '''
        lembrando que é obrigatorio adicionar sempre essa 'class Meta'
        '''
        model = Inflow
        fields = ['supplier', 'product', 'quantity', 'description',]
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows ': 3}),
        }
        # 'widgets' vamos passar um lista de cada campo eo que queremos em cada campo
        # 'attrs' é um dicionario que podemos passar para adicionar atributos HTML aos campos
        # 'forms.TextInput' e 'forms.Textarea' são usados para renderizar os campos de texto
        # 'forms.Select' usado no caso de campos foreingkey
        # 'forms.NumberInput' campo usado para numeros inteiros
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
        # 'label' é usado para definir o texto do label de cada campo
