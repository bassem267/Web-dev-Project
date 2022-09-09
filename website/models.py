from django.db import models

# Create your models here.

class Course(models.Model):
    courseName = models.CharField(max_length=150, blank=True)
    courseID = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=250, blank=True)
    numberOfHours = models.IntegerField(blank=True)
    lectureDay = models.CharField(max_length=150, blank=True)
    hallNumber = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.courseName

    class Meta:
        ordering = ['courseName']



class Student(models.Model):
    studentName = models.CharField(max_length=150, blank=True)
    studentID = models.CharField(max_length=150, verbose_name='ID', blank=True)
    dateOfBirth = models.DateField()
    university = models.CharField(max_length=50, null=False, blank=True)
    gender = models.CharField(max_length=50, null=False, blank=True)
    studentDepartment = models.CharField(max_length=50, null=False, blank=True)
    status = models.BooleanField(default = False)
    course1 = models.CharField(max_length=150, blank=True)
    course2 = models.CharField(max_length=150, blank=True)
    course3 = models.CharField(max_length=150, blank=True)
    
    def __str__(self):
        return self.studentName
    class Meta:
        ordering = ['studentName']
        



