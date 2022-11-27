from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request, 'index.html')

def Platos(request):

    #CARGAR EL FORMULARIO DE REGISTRO DE PLATOS
    formulario=FormularioRegistroPlatos()


    #CREAMOS UN DICCIONAERIO PARA ENVIAR DATOS HACIA UN TEMPLATE
    diccionarioEnvioDatos={
        'formulario':formulario
    } 

    #RECIBIENDO DATOS DEL FORMULARIO
    #PETICION DE TIPO POST  
    if request.method == 'POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid(): 
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
    return render(request, 'platos.html',diccionarioEnvioDatos)



def Empleados(request):

    #CARGAR EL FORMULARIO DE REGISTRO DE EMPLEADOS
    formularioEmpleado=FormularioRegistroEmpleados()

    #CREAMOS UN DICCIONARIO PARA ENVIAR DATOS HACIA EL TEMPLATE
    diccionarioEnvio={
        'formularioEmpleados':formularioEmpleado
    }

    #recibiendo datos del formulario empleados
    #PETICION DE TIPO POST
    if request.method == 'POST':
        datosFormulario=FormularioRegistroEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpiosEmpleados=datosFormulario.cleaned_data
        print (datosLimpiosEmpleados)

    return render(request, 'empleados.html', diccionarioEnvio)

