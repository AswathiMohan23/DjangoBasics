from django.db import models

# Create your models here.

class AllCourses(models.Model):
    coursename=models.CharField(max_length=200)
    instructorname=models.CharField(max_length=100)

class details(models.Model):
    course=models.ForeignKey(AllCourses,on_delete=models.CASCADE)
    selfStudy = models.CharField(max_length = 500)
    instructorSupported = models.CharField(max_length=500)



