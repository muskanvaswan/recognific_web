# Generated by Django 3.1.4 on 2021-02-02 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encode', '0006_auto_20210202_0732'),
        ('recognize', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow', models.BooleanField(default=False)),
                ('classname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marked', to='encode.classset')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allowed', to='encode.student')),
            ],
        ),
    ]