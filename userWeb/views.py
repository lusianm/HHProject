from django.shortcuts import render
from .models import User, Exercise, ExerciseList, ExerciseListElement
import operator
# Create your views here.
def base(request):
    return render(request, 'userWeb/base.html')

def login(request, User_ID):
    if not User.objects.filter(userID=User_ID):
        user = []
    else:
        user = User.objects.get(userID=User_ID).getUserInfo
    return render(request, 'userWeb/user.html', {'user':user})


def exercise(request, Exercise_ID, User_ID):
    exercise = Exercise.objects.get(Name=Exercise_ID)
    user = User.objects.get(userID=User_ID)
    if(user.Age == 10):
        exercise.Age10 += 1
    elif(user.Age == 20):
        exercise.Age20 += 1
    elif(user.Age == 30):
        exercise.Age30 += 1
    else:
        exercise.Age40 += 1

    if(user.Sex == "남성"):
        exercise.SexM += 1
    else:
        exercise.SexY += 1

    if(user.BMI == "저체중"):
        exercise.BMIL += 1
    elif(user.BMI == "정상"):
        exercise.BMIN += 1
    elif(user.BMI == "과체중"):
        exercise.BMIH += 1
    else:        
        exercise.BMIO += 1
    
    if(exercise.ExerPart == "가슴"):
        user.Part1 += 1
    elif(exercise.ExerPart == "하체"):
        user.Part2 += 1
    elif(exercise.ExerPart == "전신"):
        user.Part3 += 1
    else:
        user.Part4 += 1

    exercise.save()
    user.save()
    return render(request, 'userWeb/exercise.html', {'exercise':exercise.ExerciseInfo()})

def CalcValue(User_ID, Exercise_ID):
    exercise = Exercise.objects.get(Name=Exercise_ID)
    user = User.objects.get(userID=User_ID)
    value = 0
    if(user.Age == 10):
        value += exercise.Age10*0.30
    elif(user.Age == 20):
        value += exercise.Age20*0.30
    elif(user.Age == 30):
        value += exercise.Age30*0.30
    else:
        value += exercise.Age40*0.30

    if(user.Sex == "남성"):
        value += exercise.SexM*0.20
    else:
        value += exercise.SexY*0.20

    if(user.BMI == "저체중"):
        value += exercise.BMIL*0.5
    elif(user.BMI == "정상"):
        value += exercise.BMIN*0.5
    elif(user.BMI == "과체중"):
        value += exercise.BMIH*0.5
    else:        
        value += exercise.BMIO*0.5

    #부위별 가중치
    
    if(exercise.ExerPart == "가슴"):
        value *= user.Part1/(user.Part1+user.Part2+user.Part3+user.Part4+1)
    elif(exercise.ExerPart == "하체"):
        value *= user.Part2/(user.Part1+user.Part2+user.Part3+user.Part4+1)
    elif(exercise.ExerPart == "전신"):
        value *= user.Part3/(user.Part1+user.Part2+user.Part3+user.Part4+1)
    else:
        value *= user.Part4/(user.Part1+user.Part2+user.Part3+user.Part4+1)
    return value

def list(request, User_ID):
    if(not User.objects.filter(userID = User_ID)):
        return render(request, 'userWeb/user.html', {'user':"!"})
    user = User.objects.get(userID=User_ID)
    exercise = Exercise.objects.all()
    data = {}
    for exer in exercise:
        data[exer.ExerPart+"|"+exer.Name] = CalcValue(User_ID, exer.Name)
    data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'userWeb/list.html', {'exercise':dict(data).keys()})

def userlist(request, User_ID):
    if(not User.objects.filter(userID = User_ID)):
        return render(request, 'userWeb/user.html', {'user':"!"})
    user = User.objects.get(userID=User_ID)

    if(not user.exerciselist_set.all()):
        return render(request, 'userWeb/user.html', {'user':"!"})
    ulist = user.exerciselist_set.all()

    return render(request, 'userWeb/userlist.html', {'exercise':ulist})

def userlistelement(request, User_ID, List_ID):
    if(not ((User.objects.get(userID=User_ID)).exerciselist_set.get(ListName = List_ID)).exerciselistelement_set.all()):
        return render(request, 'userWeb/user.html', {'user':"!"})
    exerlist = ((User.objects.get(userID=User_ID)).exerciselist_set.get(ListName = List_ID)).exerciselistelement_set.all()
    return render(request, 'userWeb/userlistelement.html', {'exercise':exerlist})

def adduser(request, UserID_data, Password_data, Name_data, Age_data, Sex_data, Job_data, Height_data, Weight_data):
    if(User.objects.filter(userID = UserID_data)):
        return render(request, 'userWeb/user.html', {'user':"!"})
    newUser = User()
    newUser.userID = UserID_data
    newUser.Password = Password_data
    newUser.Name = Name_data
    newUser.Age = Age_data
    newUser.Sex = Sex_data
    newUser.Job = Job_data
    newUser.Height = float(Height_data)
    newUser.Weight = float(Weight_data)
    Bmi = (newUser.Weight * 10000) / (newUser.Height * newUser.Height)
    if(Bmi < 18.5):
        newUser.BMI = "저체중"
    elif(Bmi < 23):
        newUser.BMI = "정상"
    elif(Bmi < 25):
        newUser.BMI = "과체중"
    else:
        newUser.BMI = "비만"
    newUser.save()
    return render(request, 'userWeb/user.html', {'user':newUser.getUserInfo})

def addList(request, UserID_data, ListName_data):
    if(User.objects.filter(userID = UserID_data)):
        newList = ExerciseList()
        newList.user = User.objects.get(userID = UserID_data)
        if(newList.user.exerciselist_set.filter(ListName = ListName_data)):
            return render(request, 'userWeb/user.html', {'user':"!"})
        newList.ListName = ListName_data
        newList.save()
        return render(request, 'userWeb/user.html', {'user':str(newList)})
    return render(request, 'userWeb/user.html', {'user':"!"})

def addListExer(request, UserID_data, ListName_data, ExerName_data):
    user = User.objects.get(userID=UserID_data)
    exerlist = user.exerciselist_set.all()
    if(exerlist.filter(ListName = ListName_data)):
        if(Exercise.objects.filter(Name = ExerName_data)):
            exerciseList = exerlist.get(ListName = ListName_data)
            if(exerciseList.canAddExer(ExerName_data)):
                exercise = Exercise.objects.get(Name=ExerName_data)
                newListExer = ExerciseListElement()
                newListExer.exerciseList = exerciseList
                newListExer.exerciseName = ExerName_data
                newListExer.exercisePart = exercise.ExerPart
                newListExer.save()
                
                if(user.Age == 10):
                    exercise.Age10 += 10
                elif(user.Age == 20):
                    exercise.Age20 += 10
                elif(user.Age == 30):
                    exercise.Age30 += 10
                else:
                    exercise.Age40 += 10

                if(user.Sex == "남성"):
                    exercise.SexM += 10
                else:
                    exercise.SexY += 10

                if(user.BMI == "저체중"):
                    exercise.BMIL += 10
                elif(user.BMI == "정상"):
                    exercise.BMIN += 10
                elif(user.BMI == "과체중"):
                    exercise.BMIH += 10
                else:        
                    exercise.BMIO += 10
    
                if(exercise.ExerPart == "가슴"):
                    user.Part1 += 10
                elif(exercise.ExerPart == "하체"):
                    user.Part2 += 10
                elif(exercise.ExerPart == "전신"):
                    user.Part3 += 10
                else:
                    user.Part4 += 10
                user.save()
                exercise.save()

                return render(request, 'userWeb/user.html', {'user':str(newListExer)})
    return render(request, 'userWeb/user.html', {'user':"!"})
    
def deleteList(request, UserID_data, ListName_data):
    if(User.objects.filter(userID = UserID_data)):
        if(User.objects.get(userID = UserID_data).exerciselist_set.filter(ListName = ListName_data)):
            deleteList = User.objects.get(userID = UserID_data).exerciselist_set.get(ListName = ListName_data)
            for exer in deleteList.exerciselistelement_set.all():
                exer.delete()
            deleteList.delete()
            return render(request, 'userWeb/user.html', {'user':str(deleteList)})
    return render(request, 'userWeb/user.html', {'user':"!"})

def deleteListElement(request, UserID_data, ListName_data, ExerName_data):
    if(User.objects.filter(userID = UserID_data)):
        if(User.objects.get(userID = UserID_data).exerciselist_set.filter(ListName = ListName_data)):
            if(User.objects.get(userID = UserID_data).exerciselist_set.get(ListName = ListName_data).exerciselistelement_set.filter(exerciseName = ExerName_data)):
                exer = User.objects.get(userID = UserID_data).exerciselist_set.get(ListName = ListName_data).exerciselistelement_set.get(exerciseName = ExerName_data)
                exer.delete()
                return render(request, 'userWeb/user.html', {'user':str(exer)})
    return render(request, 'userWeb/user.html', {'user':"!"})

def test(request, U_ID, E_ID):
    user = User.objects.get(userID=U_ID)
    exercise = Exercise.objects.get(Name=E_ID) 
    return render(request, 'userWeb/test.html', {'user':str(user), 'exercise':str(exercise)})


