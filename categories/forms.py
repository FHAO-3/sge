from django import forms
from categories.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        '''
        lembrando que é obrigatorio adicionar sempre essa 'class Meta'
        '''
        model = Category
        fields = ['name', 'description',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows ': 3}),
        }
        # 'widgets' vamos passar um lista de cada campo eo que queremos em cada campo
        # 'forms.TextInput' e 'forms.Textarea' são usados para renderizar os campos de texto
        # 'attrs' é um dicionario que podemos passar para adicionar atributos HTML aos campos
        label = {
            'name': 'Nome',
            'description': 'Descrição',
        }
        # 'label' é usado para definir o texto do label de cada campo
