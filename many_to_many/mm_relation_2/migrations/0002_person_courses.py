# Generated by Django 4.0.3 on 2022-04-29 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm_relation_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='courses',
            field=models.ManyToManyField(related_name='course', through='mm_relation_2.Member', to='mm_relation_2.course'),
        ),
    ]