# Generated by Django 4.1 on 2022-08-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_post_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingridentnames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
