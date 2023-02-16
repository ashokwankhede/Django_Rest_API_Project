from django.urls import path
from api import views

urlpatterns = [
        path('',views.home,name='home'),
        path('insert/',views.insert,name='insert'),
        path('update/',views.update,name='update'),
        path('delete/',views.delete,name='delete'),
]