from django.db import models

# Create your models here.
from django.db.models import CASCADE


class Person(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    courses = models.ManyToManyField("Course", through="Member", related_name="course")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    members = models.ManyToManyField("Person", through="Member", related_name='course')

    def __str__(self):
        return self.title


class Member(models.Model):
    course = models.ForeignKey(Course, on_delete=CASCADE)
    person = models.ForeignKey(Person, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    LEARNER = 1
    IA = 1000
    GSI = 2000
    INSTRUCTOR = 5000
    ADMIN = 10000

    MEMBER_CHOICES = (
        (LEARNER, 'Learner'),
        (IA, 'Instructional Assistant'),
        (GSI, 'Grad Student Instructor'),
        (INSTRUCTOR, 'Instructor'),
        (ADMIN, 'Administrator'),
    )

    role = models.IntegerField(choices=MEMBER_CHOICES, default=LEARNER)

    def __str__(self):
        return "Person " + str(self.person) + " --- Course " + str(self.course)
