from django.db import models

# Create your models here.

class AllCourses(models.Model):
    coursename=models.CharField(max_length=200)
    instructorname=models.CharField(max_length=100)
    instructor_contact=models.CharField(max_length=13,verbose_name="phone",default="Not Available")


    def __str__(self):
        return self.coursename

    class Meta:
        verbose_name = 'Allcourse'
        verbose_name_plural = 'Allcourses'


class Details(models.Model):
    course=models.ForeignKey(AllCourses,on_delete=models.CASCADE)
    no_of_books = models.CharField(max_length = 100,default="Enter here")
    no_of_pages = models.CharField(max_length=1000,default="Enter here")

# if we don't give meta class then in amin page it will have one more "s" for our class name eg: Allcoursess instead of Allcourses

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = 'Details'
        verbose_name_plural = 'Details'



