import csv
import os

import django
import reader as reader

from many_to_many.mm_relation_2.models import Person, Course, Member


def run():
    file = open(os.path.join('load.csv'))
    reader = csv.reader(file)
    next(reader)

    Person.objects.all().delete()
    Course.objects.all().delete()
    Member.objects.all().delete()

    for row in reader:
        print(row)
        p, created = Person.objects.get_or_create(email=row[0])
        c, created = Course.objects.get_or_create(title=row[2])
        r = Member.LEARNER
        if row[1] == "I": r = Member.INSTRUCTOR
        m = Member(role=r, course=c, person=p)

        m.save()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "many_to_many.settings")
django.setup()
run()
