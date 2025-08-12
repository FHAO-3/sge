from django import forms
from outflows.models import Outflow
from django.core.exceptions import ValidationError

 
class OutflowForm(forms.ModelForm):
    class Meta:
        '''
        lembrando que é obrigatorio adicionar sempre essa 'class Meta'
        '''
        model = Outflow
        fields = ['product', 'quantity', 'description',]
        widgets = {
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
            'product': 'Produto',
            'quantity': 'Quantidade',
            'description': 'Descrição',
        }
        # 'label' é usado para definir o texto do label de cada campo

        def clean_quantity(self):
            quantity = self.cleanned_data.get('quantity')
            product = self.cleanned_data.get('product')

            if quantity > product.quantity:
                raise ValidationError(
                    f'A quantitdade disponivel eme estoque para o produto {product.title} e de {product.quantity}'
                )
            return quantity