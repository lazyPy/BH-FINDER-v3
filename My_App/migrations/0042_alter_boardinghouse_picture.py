# Generated by Django 4.1 on 2022-09-28 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0041_alter_boardinghouse_admin_approval'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardinghouse',
            name='picture',
            field=models.FileField(upload_to='bh-images/'),
        ),
    ]
