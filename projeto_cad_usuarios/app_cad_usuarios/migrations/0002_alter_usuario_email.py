# Generated by Django 4.2.2 on 2023-07-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.TextField(max_length=254),
        ),
    ]
