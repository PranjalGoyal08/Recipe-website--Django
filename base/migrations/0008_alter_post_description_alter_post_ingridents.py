# Generated by Django 4.1 on 2022-08-14 12:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ingridents',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]