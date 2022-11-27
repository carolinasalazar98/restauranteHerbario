from django import forms


class FormularioRegistroPlatos(forms.Form):

    PLATOS=( 
        (1, 'Entrada'),
        (2, 'Plato Fuerte'),
        (3, 'Postres'),
        (4, 'Bebidas')
    )

    nombrePlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=30,
        required=True,
        label="Nombre Plato "
      
    )
    descripcionPlato=forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=35,
        required=True,
         label="Descripción Plato "
    )
    fotoPlato=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
         label="Foto Plato "
    )
    precioPlato=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
         label="Precio Plato "
    )
    tipoPlato=forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=PLATOS,
        label="Tipo Plato "
    )

