from django.urls import path

from . import views

app_name = 'userWeb'

urlpatterns = [
    path('', views.base, name='base'),
    path('login/<User_ID>', views.login, name='login'),
    path('list/<User_ID>', views.list, name='list'),
    path('userlist/<User_ID>', views.userlist, name='userlist'),
    path('userlistelement/<User_ID>/<List_ID>', views.userlistelement, name='userlistelement'),
    path('exercise/<Exercise_ID>/<User_ID>', views.exercise, name='exercise'),
    path('<U_ID>/<E_ID>', views.test, name='test'),
    path('addUser/<UserID_data>/<Password_data>/<Name_data>/<Age_data>/<Sex_data>/<Job_data>/<Height_data>/<Weight_data>', views.adduser, name='adduser'),
    path('addList/<UserID_data>/<ListName_data>', views.addList, name='addList'),
    path('addListExer/<UserID_data>/<ListName_data>/<ExerName_data>', views.addListExer, name='addListExer'),
]