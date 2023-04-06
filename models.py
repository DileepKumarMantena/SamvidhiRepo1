from django.db import models


# Create your models here.
class TeachingModel(models.Model):
    class NativeEnglishSpeaker(models.TextChoices):
        EnglishSpeaker = 'EnglishSpeaker'
        NonEnglishSpeaker = 'NonEnglishSpeaker'

    class Semester(models.TextChoices):
        Summer = 'Summer'
        Regular = 'Regular'

    CourseInstructor = models.CharField(max_length=250)
    Course = models.CharField(max_length=250)
    ClassSize = models.CharField(max_length=250)
    TeacherId = models.CharField(max_length=250,unique=True)
    NativeEnglishSpeaker = models.CharField(max_length=17, choices=NativeEnglishSpeaker.choices, default=True)
    Semester = models.CharField(max_length=10, choices=Semester.choices, default=True)
    PerformanceScore = models.CharField(max_length=250)
    objects = models.Manager

    class Meta:
        db_table = "TA"
