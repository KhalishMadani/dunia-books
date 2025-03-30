# Generated by Django 5.1.7 on 2025-03-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('book', models.FileField(upload_to=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
