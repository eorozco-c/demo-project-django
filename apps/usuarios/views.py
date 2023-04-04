from django.shortcuts import render, redirect
from .models import Usuario
from .formularios import UsuarioForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


# Create your views here.
def index(request):
    template = "main.html"
    return render(request,template)

######################################### LISTAR CON FUNCION Y CON CLASE ####################################
def usuarios(request):
    template = "usuarios/first.html"
    usuarios = Usuario.objects.all()
    context = {
        "myusuarios" : usuarios,
        "titulo" : "Usuarios",
    }
    return render(request,template,context)

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuarios/first.html'
    extra_context = {'titulo': 'Usuarios'}
    context_object_name = 'myusuarios'


############################################################################################################


#################################### CREAR CON FUNCION Y CON CLASE #########################################

def nuevo(request):
    template = "form.html"
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:usuarios')
    else:
        form = UsuarioForm()
    context = {
        "form" : form,
    }
    return render(request,template,context)

class UsuarioCreateView(CreateView):
    model = Usuario
    template_name = 'form.html'
    form_class = UsuarioForm
    success_url = '/usuarios/'

############################################################################################################

#################################### DETALLE CON FUNCION Y CON CLASE #########################################

def detalles(request, id):
    myusuario = Usuario.objects.get(id=id)
    template = "usuarios/detalles.html"
    context = {
        'myusuario' : myusuario,
    }
    return render(request,template,context)

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuarios/detalles.html'
    context_object_name = 'myusuario'

############################################################################################################

#################################### ACTUALIZAR CON FUNCION Y CON CLASE #########################################

def actualizar(request, id):
    myusuario = Usuario.objects.get(id=id)
    template = "form.html"
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=myusuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios:usuarios')
    else:
        form = UsuarioForm(instance=myusuario)
    context = {
        "form" : form,
    }
    return render(request,template,context)

class UsuarioUpdateView(UpdateView):
    model = Usuario
    template_name = 'form.html'
    form_class = UsuarioForm
    context_object_name = 'myusuario'
    success_url = '/usuarios/'

############################################################################################################

#################################### ELIMINAR CON FUNCION Y CON CLASE #########################################

def eliminar(request, id):
    myusuario = Usuario.objects.get(id=id)
    myusuario.delete()
    return redirect('usuarios:usuarios')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuarios/eliminar.html'
    context_object_name = 'myusuario'
    success_url = '/usuarios/'

############################################################################################################