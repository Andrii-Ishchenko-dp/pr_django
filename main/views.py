from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from .filters import NameFilter


@login_required(login_url='login')
def index(request):
    # tasks = Task.objects.order_by('-id')[:5]
    tasks = Task.objects.all()

    myFilter = NameFilter(request.GET, queryset=tasks)
    tasks = myFilter.qs
    return render(request,'main/index.html', {'title':'Главная страница сайта', 'tasks': tasks, 'myFilter':myFilter})


@login_required(login_url='login')
def project(request, pk):
    projectObj = Task.objects.get(id=pk)
    return render(request,'main/single-project.html',{'title':projectObj.name_task,'project':projectObj})


@login_required(login_url='login')
def about(request):
    return render(request,'main/about.html')


@login_required(login_url='login')
def create(request):
    error=""
    if request.method =="POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = 'При заполнении были использованы недопустимые символы или пользователь с таким Именем и Фамилией уже существует!'
    form = TaskForm()
    context={
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html', context)


@login_required(login_url='login')
def updateProject(request,pk):
    error = ""
    project = Task.objects.get(id=pk)

    form = TaskForm(instance=project)

    if request.method =="POST":
        form = TaskForm(request.POST, instance= project)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = 'Форма была неверной'
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html', context)


@login_required(login_url='login')
def deleteProject(request,pk):
    project = Task.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("home")
    return render(request,'main/delete.html',{object:project})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username= username, password= password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'main/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Аккаунт создан ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'main/register.html', context)