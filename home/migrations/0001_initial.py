# Generated by Django 4.1.1 on 2022-10-31 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('stud_code', models.CharField(max_length=6)),
                ('mobile', models.CharField(max_length=15)),
                ('address', models.TextField()),
            ],
        ),
    ]
