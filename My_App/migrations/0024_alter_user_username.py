# Generated by Django 4.1 on 2022-08-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0023_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]