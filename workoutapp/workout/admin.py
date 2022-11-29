from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


@admin.register(models.WorkoutItem)
class WorkoutItemAdmin(admin.ModelAdmin):
    list_display = ['workout', 'exercise', 'sets', 'reps']


# Register your models here.
admin.site.register(models.Workout)
admin.site.register(models.Exercise)
