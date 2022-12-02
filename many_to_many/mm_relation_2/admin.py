from django.contrib import admin

# Register your models here.
from .models import Course, Person, Member

admin.site.register(Course)
admin.site.register(Person)
admin.site.register(Member)
