from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


#=================================================================================================================#

def saludo(request):
    return HttpResponse( 'HOla Django')

#=================================================================================================================#

@login_required(login_url='/login/')
def posteo(request):
    return render(request,'posteo.html')

#=================================================================================================================#

def acceso(request):
    return render(request, "acceso.html")

#=================================================================================================================#

def login_request(request):
    
    if request.method == 'POST':
        formL = AuthenticationForm(request=request, data=request.POST)
            
        if formL.is_valid():
                username = formL.cleaned_data.get('username')
                password = formL.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                        login(request, user)

                        posts = post.objects.all()
                        contexto={'posts':posts}	
                        return render(request, 'read_post.html', contexto)
                        

                
        else: 
            return render(request, 'login.html', {'formL': formL, 'mensaje': 'Usuario o contraseña incorrectos'})
        

    formL = AuthenticationForm()
    return render(request, 'login.html', {'formL': formL})

#=================================================================================================================#

def login_correct(request):
    return render(request,'login_correct.html')

#=================================================================================================================#

def index(request):
    return render(request, 'index.html')

#=================================================================================================================#

def register(request):

    if request.method == 'POST':
        formR = UserRegisterForm(request.POST)
        if formR.is_valid():
            username = formR.cleaned_data['username']
            formR.save()
            return render(request, 'login_correct.html', {'mensaje': 'Usuario creado correctamente'})
            

    else:
        formR = UserRegisterForm()


    return render(request, "register.html", {"formR":formR})

#=================================================================================================================#

def about(request):
    return render(request, 'about.html')

#=================================================================================================================#

def update_user(request):
    User = request.user
    
    if request.method == 'POST':
        UserForm = UserRegisterForm(request.POST)
        if UserForm.is_valid():
            informacion=UserForm.cleaned_data
            User.username = informacion['username']
            User.email = informacion['email']
            User.set_password(informacion ['password1']) 
            
            User.save()


            return render (request, 'profile.html')  #vuelve a la pagina principal


    else:
        UserForm = UserRegisterForm(instance=User)
    return render(request, 'update_user.html', {'UserForm':UserForm})


@login_required(login_url='/login/')
def read_post(request):
    posts = post.objects.all()
    
    contexto={'posts':posts}	
    return render(request, 'read_post.html', contexto)

#=================================================================================================================#

@login_required(login_url='/login/')
def delete_post(request, pk):
    Post = post.objects.get(pk=pk)
    Post.delete()

    posts = post.objects.all()

    contexto={'posts':posts}	
    return render(request, 'read_post.html', contexto)

#=================================================================================================================#

@login_required(login_url='/login/')
def update_post(request, pk):
    Post = post.objects.get(pk=pk)
    
    if request.method == 'POST':
        formulario = PostForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            informacionU=formulario.cleaned_data
            Post.title = informacionU['title']
            Post.subtitle = informacionU['subtitle']
            Post.content = informacionU['content']
            Post.date = informacionU['date']
            
            Post.save()
          


            return render (request, 'ok_update.html') 
        

    else:
        formulario= PostForm(initial={'title':Post.title, 'subtitle':Post.subtitle, 'content':Post.content, 'date':Post.date, 'image':Post.image})
    return render(request, 'update_post.html', {'formulario':formulario, 'pk':pk})

#=================================================================================================================#

def ok_update(request):
    return render(request, 'ok_update.html')

#=================================================================================================================#

@login_required(login_url='/login/')
def create_post(request):
    if request.method == 'POST':
        formu = PostForm(request.POST, files=request.FILES)
        if formu.is_valid():
            informacion=formu.cleaned_data
            NewPost= post(title=informacion['title'], subtitle=informacion['subtitle'], content=informacion['content'], date=informacion['date'], image=informacion['image'])
            NewPost.save()

            posts = post.objects.all()

            contexto={'posts':posts}	
            return render(request, 'read_post.html', contexto)

    else:
        formu= PostForm()
    return render(request, 'create_post.html', {'formu':formu})

#=================================================================================================================#


def profile(request):
    return render(request, 'profile.html')

#=================================================================================================================#

@login_required(login_url='/login/')
def read_more(request, pk):
    Read = post.objects.get(pk=pk)
    contextoRead={'Read':Read}
    return render(request, 'post.html', contextoRead)

#=================================================================================================================#

def create_message(request):
    if request.method == 'POST':
        f_mensaje = MessageForm(request.POST)
        if f_mensaje.is_valid():
            texto =f_mensaje.cleaned_data
            NewMessage= message()
            NewMessage.save()

            messages = message.objects.all()

            contexto={'messages':messages}	
            return render(request, 'create_message.html', contexto)

    else:
        f_mensaje= MessageForm()
    return render(request, 'create_message.html', {'f_mensaje':f_mensaje})

#=================================================================================================================#

def buscar_contacto(request):
    contactos = User.objects.all()
    contextoB={'contactos':contactos}

    return render(request, 'contact.html', contextoB)

#=================================================================================================================#

def create_link(request):
    if request.method == 'POST':
        f_link = Link(request.POST)
        if f_link.is_valid():
            texto =f_link.cleaned_data
            NewLink= widget(link=texto['link'])
            NewLink.save()

            link= widget.objects.all()

            contexto={'link':link}	
            return render(request, 'create_link.html', contexto)

    else:
        f_link= Link()
    return render(request, 'create_link.html', {'f_link':f_link})

#=================================================================================================================#

