import datetime

from django.db import models

from students.models import Student


class SessionType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Session(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    date = models.DateTimeField(default=datetime.datetime.now)

    duration = models.DurationField()

    session_type = models.ManyToManyField(SessionType)

    PROGRESS_CHOICES = (
        ('excellent', 'Excellent - It\'s going great.'),
        ('average', 'Average - The student is moving at an acceptable pace.'),
        ('bad', 'I\'m worried about this student\'s progress.')
    )
    progress = models.CharField(choices=PROGRESS_CHOICES, max_length=20)

    subjects = models.CharField(max_length=255)
    student_care = models.CharField(max_length=255)

    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    notes = models.TextField()

    def __str__(self):
        return '{0}: {1}'.format(self.student, self.date.date())
