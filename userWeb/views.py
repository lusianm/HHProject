from django.shortcuts import render
from .models import User
# Create your views here.
def base(request):
    return render(request, 'userWeb/base.html')

def login(request, User_ID):
    print(User_ID)
    user = User.objects.get(userID=User_ID)
    return render(request, 'userWeb/login.html', {'user':str(user)})
