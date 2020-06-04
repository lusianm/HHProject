from django.shortcuts import render
from .models import User, Exercise, ExerciseList, ExerciseListElement
import operator
# Create your views here.
def base(request):
    return render(request, 'userWeb/base.html')

def login(request, User_ID):
    print(User_ID)
    user = User.objects.get(userID=User_ID)
    return render(request, 'userWeb/login.html', {'user':user.getUserInfo})


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
    return render(request, 'userWeb/exercise.html', {'exercise':str(exercise)})

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
    
    print(value)
    if(exercise.ExerPart == "가슴"):
        value *= user.Part1/(user.Part1+user.Part2+user.Part3+user.Part4)
    elif(exercise.ExerPart == "하체"):
        value *= user.Part2/(user.Part1+user.Part2+user.Part3+user.Part4)
    elif(exercise.ExerPart == "전신"):
        value *= user.Part3/(user.Part1+user.Part2+user.Part3+user.Part4)
    else:
        value *= user.Part4/(user.Part1+user.Part2+user.Part3+user.Part4)
    print(value)
    return value

def list(request, User_ID):
    user = User.objects.get(userID=User_ID)
    exercise = Exercise.objects.all()
    data = {}
    for exer in exercise:
        data[exer.Name+"|"+exer.ExerPart] = CalcValue(User_ID, exer.Name)
    print(data)
    data = sorted(data.items(), key=operator.itemgetter(1), reverse=True)
    print(dict(data))
    return render(request, 'userWeb/list.html', {'exercise':dict(data).keys()})

def userlist(request, User_ID):
    user = User.objects.get(userID=User_ID)
    ulist = user.exerciselist_set.all()
    return render(request, 'userWeb/list.html', {'exercise':ulist})

def userlistelement(request, User_ID, List_ID):
    exerlist = ((User.objects.get(userID=User_ID)).exerciselist_set.get(ListName = List_ID)).exerciselistelement_set.all()
    return render(request, 'userWeb/list.html', {'exercise':exerlist})

def test(request, U_ID, E_ID):
    user = User.objects.get(userID=U_ID)
    exercise = Exercise.objects.get(Name=E_ID) 
    return render(request, 'userWeb/test.html', {'user':str(user), 'exercise':str(exercise)})

def adduser(request, UserID_data, Password_data, Name_data, Age_data, Sex_data, Job_data, Height_data, Weight_data, BMI_data):
    if(User.objects.filter(userID = UserID_data)):
        return render(request, 'userWeb/login.html', {'user':"이미 존재하는 User 입니다."})
    newUser = User()
    newUser.userID = UserID_data
    newUser.Password = Password_data
    newUser.Name = Name_data
    newUser.Age = Age_data
    newUser.Sex = Sex_data
    newUser.Job = Job_data
    newUser.Height = Height_data
    newUser.Weight = Weight_data
    Bmi = newUser.Weight / (newUser.Height * newUser.Height/float(10000))
    if(Bmi < 18.5):
        newUser.BMI = "저체중"
    elif(Bmi < 23):
        newUser.BMI = "정상"
    elif(Bmi < 25):
        newUser.BMI = "과체중"
    else:
        newUser.BMI = "비만"
    newUser.save()
    return render(request, 'userWeb/login.html', {'user':newUser.getUserInfo})

def addList(request, UserID_data, ListName_data):
    if(User.objects.filter(userID = UserID_data)):
        newList = ExerciseList()
        newList.user = User.objects.get(userID = UserID_data)
        newList.ListName = ListName_data
        newList.save()
        return render(request, 'userWeb/login.html', {'user':str(newList)})
    return render(request, 'userWeb/login.html', {'user':"올바르지 못한 접근입니다."})


def addListExer(request, UserID_data, ListName_data, ExerName_data):
    user = User.objects.get(userID=U_ID)
    exerlist = user.exerciselist_set.all()
    if(exerlist.objects.filter(ListName = ListName_data)):
        if(Exercise.objects.filter(Name = ExerName_data)):
            exerciseList = ExerciseList.objects.get(ListName = ListName_data)
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

                return render(request, 'userWeb/login.html', {'user':str(newListExer)})
    return render(request, 'userWeb/login.html', {'user':"올바르지 못한 접근입니다."})