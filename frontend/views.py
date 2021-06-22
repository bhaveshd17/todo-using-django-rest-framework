from django.contrib import messages
from django.shortcuts import render, redirect
import requests
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import User

from .forms import UserForm
from .utils import data_list


domain = 'https://todobhavesh.herokuapp.com'
# domain = 'http://127.0.0.1:8000'

@login_required(login_url='loginUser')
def toDoList(request):
    data = data_list(request)
    content = {'data':data['data_list']}
    return render(request, 'frontend/index.html', content)


@login_required(login_url='loginUser')
def createList(request):
    urlPost = domain+'/api/task-create/'
    title = request.POST.get('task')
    user = request.user.id
    requests.post(urlPost, {'title': title, 'user':user})
    return redirect('/index/')


@login_required(login_url='loginUser')
def updateList(request, pk):
    urlUpdate = domain+f'/api/task-update/{pk}/'
    taskResp = requests.get(domain + f'/api/task-details/{pk}/')
    data = data_list(request)
    dataEdit = taskResp.json()
    content = {'data': data['data_list'], 'dataEdit':dataEdit}
    if request.method == 'POST':
        task = request.POST.get('task')
        requests.put(urlUpdate, {'title': task, 'user':request.user.id})
        return redirect('/index/')
    return render(request, 'frontend/edit.html', content)


@login_required(login_url='loginUser')
def deleteList(request, pk):
    deleteUrl = domain+f'/api/task-delete/{pk}/'
    requests.delete(deleteUrl)
    return redirect('/index/')


@login_required(login_url='loginUser')
def view_api(request):
    return redirect('/api/task-list/')

#authentication
@unauthenticated_user
def signInUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/index/')
    else:
        form = UserForm()

    return render(request, 'auth/signin.html', {'form':form})

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(60 * 60 * 24)
            return redirect('/index/')
        else:
            messages.error(request, 'Wrong username or password')
            return render(request, 'auth/login.html')
    return render(request, 'auth/login.html')


def logoutUser(request):
    logout(request)
    return redirect('/')