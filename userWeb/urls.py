from django.urls import path

from . import views

urlpatterns = [
    path('<User_ID>', views.login, name='login'),

]
