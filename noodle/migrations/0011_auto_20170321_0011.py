# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('noodle', '0010_auto_20170320_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseVisit', to='noodle.Course')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='enrolledIn',
            field=models.ManyToManyField(related_name='enrolledStudents', to='noodle.Course'),
        ),
        migrations.AddField(
            model_name='visitedcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseVisit', to='noodle.Student'),
        ),
        migrations.AddField(
            model_name='student',
            name='visitedCourse',
            field=models.ManyToManyField(through='noodle.VisitedCourse', to='noodle.Course'),
        ),
    ]
