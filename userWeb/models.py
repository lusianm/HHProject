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
    Height = models.IntegerField()
    Weight = models.IntegerField()
    BMI = models.IntegerField()
