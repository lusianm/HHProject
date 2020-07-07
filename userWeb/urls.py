from django.urls import path

from . import views

app_name = 'userWeb'

urlpatterns = [
    path('', views.base, name='base'),
    path('Exercise/<Exercise_ID>/<User_ID>', views.exercise, name='exercise'),
    path('Login/<User_ID>', views.login, name='login'),
    path('AddUser/<UserID_data>/<Password_data>/<Name_data>/<Age_data>/<Gender_data>/<Job_data>/<Height_data>/<Weight_data>',
     views.adduser, name='adduser'),
    path('List/<User_ID>', views.list, name='list'),
    path('UserList/<User_ID>', views.userlist, name='userlist'),
    path('UserListElement/<User_ID>/<List_ID>', views.userlistelement, name='userlistelement'),
    path('AddList/<UserID_data>/<ListName_data>', views.addList, name='addList'),
    path('AddListExer/<UserID_data>/<ListName_data>/<ExerName_data>', views.addListExer, name='addListExer'),
    path('DeleteList/<UserID_data>/<ListName_data>', views.deleteList, name='deleteList'),
    path('DeleteListExer/<UserID_data>/<ListName_data>/<ExerName_data>', views.deleteListElement, name='deleteListElement'),
    path('<U_ID>/<E_ID>', views.test, name='test'),
]