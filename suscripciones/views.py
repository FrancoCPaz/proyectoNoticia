from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Suscriptor,Genero, Noticia
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import GeneroForm, noticiaForm

# Create your views here.


def index(request):
    suscripciones= Suscriptor.objects.all()
    context={"suscripciones":suscripciones}
    return render(request, 'suscripciones/index.html', context)


def listadoSQL(request):
    suscripciones= Suscriptor.objects.raw('SELECT * FROM suscripciones_suscriptor')
    print(suscripciones)
    context={"suscripciones":suscripciones}
    return render(request, 'suscripciones/listadoSQL.html', context)

@login_required
def crud(request):
    suscripciones= Suscriptor.objects.all()
    context = {'suscripciones': suscripciones}
    return render(request, 'suscripciones/suscripcion_list.html', context)


def suscripcionesAdd(request):
    if request.method != "POST":  # Corrección de la comparación
        # No es POST, por lo tanto se muestra el formulario para agregar.
        generos = Genero.objects.all()
        context = {'generos': generos}
        return render(request, 'suscripciones/suscripcion_add.html', context)
    
    else:
        # Es un POST, por lo tanto se recuperan los datos del formulario
        # y se graban en la tabla.

        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        activo = 1  # Uso consistente del tipo de datos
        
        try:
            objGenero = Genero.objects.get(id_genero=genero)
            obj = Suscriptor.objects.create(
                rut=rut,
                nombre=nombre,
                apellido_paterno=aPaterno,
                apellido_materno=aMaterno,
                fecha_nacimiento=fechaNac,
                id_genero=objGenero,
                telefono=telefono,
                email=email,
                direccion=direccion,
                activo=activo
            )
            obj.save()
            messages.success(request, 'Suscriptor registrado!')
            context = {'mensaje': "OK, datos grabados..."}
        except Genero.DoesNotExist:
            context = {'mensaje': "Error: Género no encontrado."}
        return render(request, 'suscripciones/suscripcion_add.html', context)
        

@login_required 
def suscripciones_del(request,pk):
    context={}
    try:
        suscriptor=Suscriptor.objects.get(rut=pk)

        suscriptor.delete()
        messages.success(request, '¡Suscriptor eliminado!')
        mensaje="Bien, datos eliminados..."
        suscripciones=Suscriptor.objects.all()
        context={'suscripciones': suscripciones, 'mensaje':mensaje}
        return render(request, 'suscripciones/suscripcion_list.html', context)
        
    except: 
        mensaje="Error, rut no existe..."
        suscripciones=Suscriptor.objects.all()
        context={'suscripciones': suscripciones, 'mensaje':mensaje}
        return render(request, 'suscripciones/suscripcion_list.html', context)

@login_required  
def suscripciones_findEdit(request,pk):

    if pk != "":
        suscriptor=Suscriptor.objects.get(rut=pk)
        generos=Genero.objects.all()

        print(type(suscriptor.id_genero.genero))

        context={'suscriptor':suscriptor, 'generos':generos}
        if suscriptor:
            return render(request, 'suscripciones/suscripcion_edit.html', context)
        else:
            context={'mensaje':"Error, rut no existe..."}
            return render(request, 'suscripciones/suscripcion_list', context)

@login_required
def suscripcionesUpdate(request):
    if request.method == "POST":
        #Es un POST, por lo tanto se recuperan los datos del formulario
        #y se graban en la tabla.
        rut=request.POST["rut"]
        nombre=request.POST["nombre"]
        aPaterno=request.POST["paterno"]
        aMaterno=request.POST["materno"]
        fechaNac=request.POST["fechaNac"]
        genero=request.POST["genero"]
        telefono=request.POST["telefono"]
        email=request.POST["email"]
        direccion=request.POST["direccion"]
        activo="1"

        objGenero=Genero.objects.get(id_genero = genero)

        suscriptor = Suscriptor()
        suscriptor.rut=rut
        suscriptor.nombre=nombre
        suscriptor.apellido_paterno=aPaterno
        suscriptor.apellido_materno=aMaterno
        suscriptor.fecha_nacimiento=fechaNac
        suscriptor.id_genero=objGenero
        suscriptor.telefono=telefono
        suscriptor.email=email
        suscriptor.direccion=direccion
        suscriptor.activo=1
        suscriptor.save()

        generos=Genero.objects.all()
        context={'mensaje':"Ok, datos actualizados...", 'generos':generos, 'suscriptor':suscriptor}
        return render(request, 'suscripciones/suscripcion_edit.html', context)
    else:
        #no es un POST, por lo tanto se muestra el formulario para agregar.
        suscripciones= Suscriptor.objects.all()
        context={'suscripciones':suscripciones}
        return render(request, 'suscripciones/suscripcion_list.html', context)

@login_required
def crud_generos(request):
    generos=Genero.objects.all()
    context={'generos':generos}
    print("enviando datos generos_list")
    return render(request, "suscripciones/generos_list.html",context)

@login_required
def generosAdd(request):
    print("estoy en controlador generosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = GeneroForm(request.POST)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=GeneroForm()

            context={'mensaje':"OK, datos grabados...","form":form}
            return render(request,"suscripciones/generos_add.html",context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request,'suscripciones/generos_add.html',context)
    
@login_required
def generos_del(request,pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("Bien, datos eliminados...")
            context = {'generos':generos, 'mensajes':mensajes, 'errores':errores}
            return render(request, 'suscripciones/generos_list.html',context)        
    except: 
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe..."
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'suscripciones/generos_list.html', context)
    
@login_required
def generos_edit(request,pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("Edit encontro el genero...")
            if request.method == "POST":
                print("edit, es un POST")
                form = GeneroForm(request.POST,instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context={'genero':genero, 'form':form, 'mensaje':mensaje}
                return render(request,'suscripciones/generos_edit.html',context)
            else:
                #no es un POST
                print("edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context={'genero':genero, 'form':form, 'mensaje':mensaje}
                return render(request,'suscripciones/generos_edit.html',context)
    except:
        print("Error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request,'suscripciones/generos_list.html',context)


def menu(request):
    request.session["usuario"]="cgarcia"
    usuario=request.session["usuario"]
    context = {'usuasrio':usuario}
    return render(request, 'administrador/menu.html',context)

def acerca(request):
    return render(request, 'suscripciones/acerca.html')

def contacto(request):
    return render(request, 'suscripciones/contacto.html')

def galeria(request):
    return render(request, 'suscripciones/galeria.html')

def login(request):
    return render(request, 'suscripciones/login.html')

def noticia1(request):
    return render(request, 'suscripciones/noticia1.html')

def noticia2(request):
    return render(request, 'suscripciones/noticia2.html')

def noticia3(request):
    return render(request, 'suscripciones/noticia3.html')

def pokedex(request):
    return render(request, 'suscripciones/pokedex.html')

def registro(request):
    return render(request, 'suscripciones/registro.html')

def base(request):
    return render(request, 'suscripciones/base.html')


def agregar_noticia(request):
    form= noticiaForm()
    if request.method =='POST':
        form = noticiaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = noticiaForm()
        context={'form':form}
        return render(request, 'suscripciones/agregar_noticia.html',context)
    context={'form':form}
    return render(request, 'suscripciones/agregar_noticia.html',context)

def lista_noticia(request):
    noticia = Noticia.objects.all()
    context={'noticias':noticia}
    return render(request, 'suscripciones/listar_noticia.html',context)
    

def noticia_eliminar(request,id_noticia):
    noticia_eliminar = get_object_or_404(Noticia, id_noticia=id_noticia)
    noticia_eliminar.delete()
    messages.success(request,'noticia eliminada')
    return redirect('listar_noticia')
    
def editar_noticia(request, id_noticia):
    instance = get_object_or_404(Noticia, id_noticia=id_noticia) if id_noticia else None
    if request.method == 'POST':
        form = noticiaForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            mensaje = "editado correctamente"
            context = {
                'mensaje': mensaje,
                'form': form
            }
            return render(request, 'suscripciones/listar_noticia.html', context)
    else:
        form = noticiaForm(instance=instance)
    
    context = {'form': form}
    return render(request, 'suscripciones/editar_noticia.html', context)

