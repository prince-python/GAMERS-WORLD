# Generated by Django 3.2.18 on 2023-05-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=10000)),
                ('orignalsize', models.CharField(max_length=10000)),
                ('Repacksize', models.CharField(max_length=10000)),
                ('img', models.ImageField(upload_to='game/')),
                ('comment', models.TextField(blank=True)),
                ('d', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
