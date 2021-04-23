from django.shortcuts import render

def toDoList(request):
    return render(request, 'frontend/index.html')
