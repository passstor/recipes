# Generated by Django 4.0.4 on 2022-05-26 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='blog/images/')),
                ('date', models.DateField()),
            ],
        ),
    ]
