# Generated by Django 5.1.4 on 2025-04-15 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0003_remove_pedido_usuario_delete_itempedido_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="tipo",
            field=models.CharField(
                choices=[("v", "Variável"), ("S", "Simples")], default="V", max_length=1
            ),
        ),
    ]
