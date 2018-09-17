# Generated by Django 2.1 on 2018-09-13 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50, unique=True)),
                ('sex', models.CharField(max_length=50)),
                ('registerTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': '用户',
                'db_table': 'user',
                'ordering': ['username'],
            },
        ),
    ]
