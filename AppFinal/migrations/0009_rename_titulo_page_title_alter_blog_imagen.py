# Generated by Django 4.1.5 on 2023-02-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFinal', '0008_rename_titulo_blog_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='titulo',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='AppFinal/images/'),
        ),
    ]
