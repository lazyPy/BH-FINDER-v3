# Generated by Django 4.1 on 2022-09-28 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0044_alter_boardinghouse_picture1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
