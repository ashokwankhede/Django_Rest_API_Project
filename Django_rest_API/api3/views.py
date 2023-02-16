from django.shortcuts import render
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from .models import Students
from .serializer import StudentSerializer
from django.views.decorators.csrf import csrf_exempt
from django.db import connection as mydb
mycursor = mydb.cursor()
import json
# Create your views here.


@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            mycursor.execute("SELECT JSON_OBJECT ('id',id,'name', name, 'roll', roll ,'city' , city) FROM students where id=%d"%int(id))
            data = mycursor.fetchone()
            return JsonResponse(data,safe=False)
        mycursor.execute("SELECT JSON_OBJECT ('id',id,'name', name, 'roll', roll ,'city' , city) FROM students")
        data = mycursor.fetchall()
        return JsonResponse(data,safe=False)


    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        name=python_data['name']
        roll=int(python_data['roll'])
        city=python_data['city']
        mycursor.execute('insert into students (name,roll,city) values ("%s",%d,"%s")'%(name,roll,city))
        mydb.commit()
        mycursor.execute("SELECT JSON_OBJECT ('id',id,'name', name, 'roll', roll ,'city' , city) FROM students")
        data = mycursor.fetchall()
        print(data)
        return JsonResponse(data,safe=False)
        
    

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        mycursor.execute('select * from students where id=%d'%(id))
        data=mycursor.fetchone()
        name=python_data.get('name',data[1])
        roll=python_data.get('roll',data[2])
        city=python_data.get('city',data[3])
        mycursor.execute('update students set name="%s",roll=%d ,city="%s" where id=%d'%(name,roll,city,id))
        mydb.commit()
        mycursor.execute("SELECT JSON_OBJECT ('id',id,'name', name, 'roll', roll ,'city' , city) FROM students")
        data = mycursor.fetchall()
        return JsonResponse(data,safe=False)
        

    if request.method == 'DELETE':
        json_data = request.body    
        stream = io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id = python_data.get('id')
        mycursor.execute('delete from students where id=%d'%(id))
        mydb.commit()
        mycursor.execute("SELECT JSON_OBJECT ('id',id,'name', name, 'roll', roll ,'city' , city) FROM students")
        data = mycursor.fetchall()
        return JsonResponse(data,safe=False)



    














        