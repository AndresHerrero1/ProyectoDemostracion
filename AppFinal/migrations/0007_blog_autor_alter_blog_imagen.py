# Generated by Django 4.1.5 on 2023-02-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0006_alter_blog_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
