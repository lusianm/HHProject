from django.db import models

# Create your models here.
class User(models.Model):
    userID = models.CharField(max_length=20)
    Password = models.CharField(max_length=30)
    Name = models.CharField(max_length=20)
    class Age_Choices(models.IntegerChoices):
        age10 = 10
        age20 = 20
        age30 = 30
        age40 = 40
    Age = models.IntegerField(choices=Age_Choices.choices)
    class Sex_Choices(models.TextChoices):
        Man = "남성"
        Woman = "여성"
    Sex = models.CharField(choices=Sex_Choices.choices, max_length=20)
    Job = models.CharField(max_length=20)
    Height = models.FloatField()
    Weight = models.FloatField()
    class BMI_Choices(models.TextChoices):
        LowWeight = "저체중"
        NomalWeight = "정상"
        OverWeight = "과체중"
        Obesity = "비만"
    BMI = models.CharField(choices=BMI_Choices.choices, max_length=20, default = "정상")
    Part1 = models.IntegerField(default = 0)
    Part2 = models.IntegerField(default = 0)
    Part3 = models.IntegerField(default = 0)
    Part4 = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.userID + "|" + self.Name
    def getUserInfo(self):
        userText = self.userID+'|'+self.Password+'|'+self.Name+'|'+str(self.Age)+'|'+self.Sex+'|'+self.Job+'|'+str(self.Height)+'|'+str(self.Weight)+'|'+str(self.BMI)
        return userText
    

class ExerciseList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ListName = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.user) + "|" + self.ListName
    def getExer(self):
        try:
            exer = self.exerciselistelement_set.all()
        except(KeyError, ExerciseListElement.DoesNotExist):
            return str(self.listName)
        else:
            for element in exer:
                returnstr += str(element) + "|"
            return returnstr
    def canAddExer(self, addExer):
        try:
            exer = self.exerciselistelement_set.all()
        except(KeyError, ExerciseListElement.DoesNotExist):
            return True
        else:
            for element in exer:
                if(element.exerciseName == addExer):
                    return False
            return True


class ExerciseListElement(models.Model):
    exerciseList = models.ForeignKey(ExerciseList, on_delete=models.CASCADE, null=True)
    exerciseName = models.CharField(max_length = 40)
    class ExerPart_Choices(models.TextChoices):
        Part1 = "가슴"
        Part2 = "하체"
        Part3 = "전신"
        Part4 = "복부"
    exercisePart = models.CharField(choices=ExerPart_Choices.choices, max_length=20, null=True)
    def __str__(self):
        return str(str(self.exerciseList) + "|" + self.exercisePart + "|" + self.exerciseName)
    def ExerInfo(self):
        return self.exercisePart + "|" + self.exerciseName

class Exercise(models.Model):
    Name = models.CharField(max_length=40)
    class ExerPart_Choices(models.TextChoices):
        Part1 = "가슴"
        Part2 = "하체"
        Part3 = "전신"
        Part4 = "복부"
    ExerPart = models.CharField(choices=ExerPart_Choices.choices, max_length=20)
    ExerciseDesc = models.CharField(max_length=200)
    YoutubeLink = models.CharField(max_length=400, default='https://www.youtube.com/watch?v=Y3iDSy425gw')
    AccuracyLink = models.CharField(max_length=400, default='www.youtube.com')
    #나이대별
    Age10 = models.IntegerField(default = 0)
    Age20 = models.IntegerField(default = 0)
    Age30 = models.IntegerField(default = 0)
    Age40 = models.IntegerField(default = 0)
    #성별별
    SexM = models.IntegerField(default = 0)
    SexY = models.IntegerField(default = 0)
    #BMI별
    BMIL = models.IntegerField(default = 0)
    BMIN = models.IntegerField(default = 0)
    BMIH = models.IntegerField(default = 0)
    BMIO = models.IntegerField(default = 0)
    def __str__(self):
        exerciseText = self.ExerPart + '|' + self.Name 
        return exerciseText
    def ExerciseInfo(self):
        exerciseText = self.Name + '|' + self.ExerPart + '|' + self.ExerciseDesc + '|' + self.YoutubeLink + '|' + self.AccuracyLink
        return exerciseText
