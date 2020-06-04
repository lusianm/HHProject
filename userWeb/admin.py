from django.contrib import admin
from .models import User, Exercise, ExerciseList, ExerciseListElement
# Register your models here.

admin.site.register(User)
admin.site.register(Exercise)
admin.site.register(ExerciseList)
admin.site.register(ExerciseListElement)
