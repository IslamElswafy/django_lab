from django.shortcuts import render
import requests

# Create your views here.
def overviwe(request):
    url = "http://127.0.0.1:9000/trainee/list"
    head = {'contnet-type': 'application/json'}
    res = requests.get(url=url, headers=head)
    print(res.status_code)
    trainees = res.json()
    context = {'trainees': trainees}
    return render(request,'call/listapi.html',context)