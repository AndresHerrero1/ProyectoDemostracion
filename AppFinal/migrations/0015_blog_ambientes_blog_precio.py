# Generated by Django 5.0.3 on 2024-04-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0014_blog_ubicacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='ambientes',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AddField(
            model_name='blog',
            name='precio',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
