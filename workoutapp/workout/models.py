from django.db import models

# Create your models here.


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255)
    exercise_description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)


class Workout(models.Model):
    created = models.DateField(auto_now=True)


class User(models.Model):
    first_name = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)


class WorkoutItem(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()
