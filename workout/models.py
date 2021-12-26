from django.db import models


class Training(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return f"{self.name}"


class Timetable(models.Model):
    training = models.ForeignKey("workout.Training", null=False, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.date} {self.training}"
