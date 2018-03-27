from django.db import models
from django.core.validators import validate_comma_separated_integer_list

class Subject(models.Model):
    title = models.CharField(max_length=255)

class Teacher(models.Model):
    firstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    fathersName = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject)

class Student(models.Model):
    firstName = models.CharField(max_length=255)
    secondName = models.CharField(max_length=255)
    fathersName = models.CharField(max_length=255)
    subjects = models.ManyToManyField(Subject)

class Student_Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateTimeField()
    vector = models.CharField(validators=[validate_comma_separated_integer_list], max_length=31)


