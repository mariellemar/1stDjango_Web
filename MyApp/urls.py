from django.urls import path
from . import views

app_name = 'MyApp'

urlpatterns = [
    path('', views.myview, name='index'),
]
