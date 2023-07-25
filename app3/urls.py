from app3.views import *
from django.urls import path


urlpatterns=[
    path('fifth/',fifth,name='fifth'),
    path('sixth/',sixth,name='sixth'),
    path('string3/',string3,name='string3'),
    
]