# Generated by Django 5.1.3 on 2025-04-08 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("perfil", "0002_alter_perfil_usuario"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="perfil",
            options={"verbose_name": "Perfil", "verbose_name_plural": "Perfis"},
        ),
    ]
