# Generated by Django 4.1 on 2022-08-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('My_App', '0026_rename_imagess_boardinghouse_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardinghouse',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='bh-images/'),
        ),
    ]