from django.urls import path
from . import views # importing views module from current folder

urlpatterns = [
    path('hello/', views.say_hello)
]

