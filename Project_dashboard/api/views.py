from django.shortcuts import render,HttpResponse,redirect
import requests
import json
from django.http import JsonResponse

URL="http://127.0.0.1:1234/studentapi/"
# Create your views here.

def home(request):
    data={}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    data=r.json()
    li=[]
    for i in data:
        li.append(json.loads(i[0]))
    return render(request,'apidashbaord/base.html',{'data':li})

def insert(request):
    if request.method=='POST':
        name=request.POST['name']
        roll=request.POST['roll']
        city=request.POST['city']
        data={
        'name':name,
        'roll':int(roll),
            'city':city,
        }
        print(data)
        json_data=json.dumps(data)
        r = requests.post(url=URL,data=json_data)
        data=r.json()
        # print(data)
        li=[]
        for i in data:
            li.append(json.loads(i[0]))
        return JsonResponse(li,safe=False)
    return redirect(home)


def update(request):
    if request.method=="POST":
        id=request.POST.get('id')
        name=request.POST.get('name')
        roll=request.POST.get('roll')
        city=request.POST.get('city')
        data={
            'id':int(id),
            'name':name,
            'roll':int(roll),
            'city':city
        }
        json_data=json.dumps(data)
        r = requests.put(url=URL,data=json_data)
        data=r.json()
        li=[]
        for i in data:
            li.append(json.loads(i[0]))
        return JsonResponse(li,safe=False)
    return redirect(home)


def delete(request):
    if request.method =="POST":
        id=request.POST['id']
        data={}
        if id is not None:
            data={'id':int(id)}
            json_data = json.dumps(data)
            r = requests.delete(url=URL,data=json_data)
            data=r.json()
            li=[]
            for i in data:
                li.append(json.loads(i[0]))
            return JsonResponse(li,safe=False)
    return redirect(home)