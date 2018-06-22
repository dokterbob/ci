# Generated by Django 2.0.6 on 2018-06-22 13:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('duration', models.DurationField(choices=[(datetime.timedelta(0, 900), '15 minutes'), (datetime.timedelta(0, 1800), '30 minutes'), (datetime.timedelta(0, 2700), '45 minutes')])),
                ('progress', models.CharField(choices=[('excellent', "Excellent - It's going great."), ('average', 'Average - The student is moving at an acceptable pace.'), ('bad', "I'm worried about this student's progress.")], max_length=20)),
                ('subjects', models.CharField(max_length=255)),
                ('student_care', models.CharField(max_length=255)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SessionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='session_type',
            field=models.ManyToManyField(to='mentoring.SessionType'),
        ),
        migrations.AddField(
            model_name='session',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='students.Student'),
        ),
    ]
