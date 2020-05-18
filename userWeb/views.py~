from django.shortcuts import render
from .models import User
# Create your views here.
def login(request, User_ID):
    print(User_ID)
    user = User.objects.get(userID=User_ID)
    return render(request, '~/HHProject/userWeb/login.html', {'user':user})
