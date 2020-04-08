from django import forms

from .models import Consumption


class ConsumptionForm(forms.ModelForm):
    class Meta:
        model = Consumption
        # campos a tener en cuanta en el formulario, si esta deshabilitado no se mostrara en el template
        fields = [
            'odometro',
            'boleta',
            'monto',
            'precio_litro',
            'imagen'

        ]  # , 'fecha']
        widgets = {
            'odometro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Odometro'}),
            'boleta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "N° Boleta"}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'precio_litro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Precio X Litro'}),
            'monto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Monto'}),
            # 'fecha': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Direccion'}),
        }
        labels = {
            # 'odometro': '',
            # 'precio_litro': '',
            # 'monto': '',
            'imagen': 'Foto',
        }

# name = forms.CharField(
#     max_length=30,
#     widget=forms.TextInput(
#         attrs={'class': 'form-control'}
#     ),
#     label="Nombre",
#     required=False,
# )
