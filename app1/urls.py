from app1.views import *
from django.urls import path

urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
    path('third/',third,name='third'),
]