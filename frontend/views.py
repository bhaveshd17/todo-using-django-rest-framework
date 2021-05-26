from django.shortcuts import render, redirect
import requests


domain = 'http://127.0.0.1:8000'
def toDoList(request):
    response = requests.get(domain+'/api/task-list/')
    data = response.json()
    content = {'data':data}
    return render(request, 'frontend/index.html', content)

def createList(request):
    urlPost = domain+'/api/task-create/'
    title = request.POST.get('task')
    requests.post(urlPost, {'title': title})
    return redirect('/')

def updateList(request, pk):
    urlUpdate = domain+f'/api/task-update/{pk}/'
    response = requests.get(domain + '/api/task-list/')
    taskResp = requests.get(domain + f'/api/task-details/{pk}/')
    data = response.json()
    dataEdit = taskResp.json()
    content = {'data': data, 'dataEdit':dataEdit}
    if request.method == 'POST':
        task = request.POST.get('task')
        requests.put(urlUpdate, {'title': task})
        return redirect('/')
    return render(request, 'frontend/edit.html', content)

def deleteList(request, pk):
    deleteUrl = domain+f'/api/task-delete/{pk}/'
    requests.delete(deleteUrl)
    return redirect('/')