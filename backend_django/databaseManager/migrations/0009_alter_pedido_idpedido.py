# Generated by Django 4.2.1 on 2023-06-20 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseManager', '0008_alter_pedido_idpedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='idPedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
