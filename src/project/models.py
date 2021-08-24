from django.db import models
from django.db.models.deletion import SET_NULL


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS = [
        ('Assigned', 'Assigned'),
        ('In Process', 'In Process'),
        ('Complete', 'Complete'),
    ]

    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20)

    def __str__(self):
        return self.name
