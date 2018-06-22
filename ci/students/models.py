from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
