# Generated by Django 4.2.2 on 2023-07-05 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0002_alter_usuario_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idade',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.TextField(max_length=254),
        ),
    ]
