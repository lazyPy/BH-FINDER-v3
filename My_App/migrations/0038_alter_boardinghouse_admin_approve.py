# Generated by Django 4.1 on 2022-09-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0037_boardinghouse_admin_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardinghouse',
            name='admin_approve',
            field=models.BooleanField(default=False),
        ),
    ]
