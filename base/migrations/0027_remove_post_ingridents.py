# Generated by Django 4.1 on 2022-08-21 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0026_alter_post_likes_alter_post_unlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='ingridents',
        ),
    ]