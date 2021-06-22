import requests

domain = 'https://todobhavesh.herokuapp.com'
# domain = 'http://127.0.0.1:8000'

def data_list(request):
    response = requests.get(domain + '/api/task-list/')
    data = response.json()
    data_list = []
    for info in data:
        if info['user'] == request.user.id:
            data_list.append(info)
    return {'data_list':data_list}