# Generated by Django 4.1 on 2022-09-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0040_alter_boardinghouse_admin_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardinghouse',
            name='admin_approval',
            field=models.BooleanField(default=False, max_length=200),
        ),
    ]
