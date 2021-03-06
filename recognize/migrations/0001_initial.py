# Generated by Django 3.1.4 on 2021-01-15 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('encode', '0004_auto_20210115_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='encode.classset')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendance', to='encode.student')),
            ],
        ),
    ]
