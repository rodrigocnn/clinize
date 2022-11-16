from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout_django
from django.contrib.auth.hashers import make_password


from usuarios.forms import UserForm


def index(request):
    usuarios = User.objects.all()
    return render(request, template_name="usuarios/index.html",  context={"usuarios": usuarios})


def login(request):
    if request.method == 'GET':
        return render(request, template_name="usuarios/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            login_django(request, user)
            return redirect(reverse('pacientes_home'))
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            return redirect(reverse('pacientes_home'))


def logout(request):
    logout_django(request)
    return redirect(reverse('login'))


def create(request):
    # form = PacienteForm()
    # context = {'form': form}
    return render(request, "usuarios/create.html")


def store(request):
    if request.method == 'POST':
        # form = PacienteForm(request.POST)
        # if form.is_valid():

        username = request.POST['username']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()

        if user:
            messages.error(request, "Username já cadastrado no sistema!")

        user = User.objects.create_user(username=username,  email=email, password=password, first_name=first_name)
        user.save()
        messages.success(request, "Usuário Cadastrado com Sucesso!")
        return redirect(reverse('usuario_home'))


def edit(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    initial_form = {
        "username": usuario.username,
        "first_name": usuario.first_name,
        "email": usuario.email,
    }
    form = UserForm(initial=initial_form)
    context = {"usuario": usuario, 'form': form}
    return render(request, "usuarios/edit.html", context)


def update(request):
    if request.method == 'POST':

        user = User.objects.filter(pk=request.POST['id_usuario']).first()
        user.username = request.POST['username']
        user.first_name = request.POST['first_name']
        user.email = request.POST['email']

        if request.POST['password']:
            user.password = make_password(request.POST['password'])

        if not user:
            messages.error(request, "Username inexistente no sistema!")
        user.save()
        messages.success(request, "Paciente Atualizado com Sucesso!")
        return redirect(reverse('usuario_home'))


def delete(request, usuario_id):
    usuario = get_object_or_404(User, pk=usuario_id)
    usuario.delete()
    messages.success(request, "Paciente Excluído com Sucesso!")
    return redirect(reverse('usuario_home'))
