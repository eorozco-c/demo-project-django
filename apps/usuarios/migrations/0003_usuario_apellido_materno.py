# Generated by Django 4.1.7 on 2023-03-08 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
