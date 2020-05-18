from django.urls import path

from . import views

app_name = 'userWeb'

urlpatterns = [
    path('', views.base, name='base'),
    path('<User_ID>', views.login, name='login'),

]
