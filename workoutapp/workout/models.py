from django.db import models

# Create your models here.


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=255)
    exercise_description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.exercise_name

    class Meta:
        ordering = ['exercise_name']


class Workout(models.Model):
    workout_name = models.CharField(max_length=255)
    created = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.workout_name

    class Meta:
        ordering = ['workout_name']


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        ordering = ['first_name']


class WorkoutItem(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.PROTECT)
    exercise = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    reps = models.PositiveSmallIntegerField()
    sets = models.PositiveSmallIntegerField()
