# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 23:12
from __future__ import unicode_literals
import numpy as np

from django.db import migrations
from django.conf import settings


def populate_userinfos(apps, schema_editor):
    UserInfo = apps.get_model("examples", "UserInfo")
    # Use a fixed seed for generate content
    np.random.seed(123456)
    # Size of table
    table_size = getattr(settings, "DJANGO_AI_EXAMPLES_USERINFO_SIZE", 200)
    print(" (Table size is {})".format(table_size), end="")
    # Sex is ~ 70% F (0) / 30% M (1)
    sex = np.random.binomial(1, 0.7, table_size)  # 200 Bernoullies :)
    # Age is around 30, mostly between 25 and 35
    age = np.floor(np.random.normal(30, 2, size=(table_size,)))
    # Average 1 is a metric normally distributed around 10 with a std dev of 5
    avg1 = np.random.normal(10, 5, size=(table_size,))
    # Create the objects in the Model
    uis = []
    for i in range(0, table_size):
        uis.append(UserInfo(age=age[i], sex=sex[i], avg1=avg1[i]))
    UserInfo.objects.bulk_create(uis)


def unpopuplate_userinfos(apps, schema_editor):
    UserInfo = apps.get_model("examples", "UserInfo")
    UserInfo.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0002_student_avg1'),
    ]

    operations = [
        migrations.RunPython(populate_userinfos,
                             unpopuplate_userinfos),
    ]
