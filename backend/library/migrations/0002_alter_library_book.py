# Generated by Django 5.1.7 on 2025-03-30 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book',
            field=models.FileField(upload_to='pdfs/'),
        ),
    ]
