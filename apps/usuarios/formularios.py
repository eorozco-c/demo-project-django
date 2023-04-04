from django import forms
from .models import Usuario


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre","apellido","apellido_materno","edad","email","password","activo"]

        widgets = {
            "nombre" : forms.TextInput(attrs={"class":"form-control"}),
            "apellido" : forms.TextInput(attrs={"class":"form-control"}),
            "apellido_materno" : forms.TextInput(attrs={"class":"form-control"}),
            "edad" : forms.NumberInput(attrs={"class":"form-control"}),
            "email" : forms.EmailInput(attrs={"class":"form-control"}),
            "password" : forms.PasswordInput(attrs={"class":"form-control"}),
            "activo" : forms.CheckboxInput(attrs={"class":"form-check-input"}),
        }

        labels = {
            "nombre" : "Nombre",
            "apellido" : "Apellido",
            "apellido_materno" : "Apellido Materno",
            "edad" : "Edad",
            "email" : "Email",
            "password" : "Password",
            "activo" : "Activo",
        }

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))