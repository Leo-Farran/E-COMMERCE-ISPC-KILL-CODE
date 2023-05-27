# Generated by Django 4.2.1 on 2023-05-26 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databaseManager', '0034_alter_recibosh_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id_recla', models.IntegerField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=200, verbose_name='estado de reclamo')),
                ('descripcion', models.CharField(max_length=200, verbose_name='descripción de reclamo')),
                ('fecha', models.DateField(verbose_name='fecha')),
                ('tipo', models.CharField(max_length=200, verbose_name='tipo de reclamo')),
                ('empleado', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='databaseManager.empleado')),
            ],
        ),
        migrations.RenameModel(
            old_name='Arts',
            new_name='Art',
        ),
        migrations.RenameModel(
            old_name='Deducciones',
            new_name='Deduccion',
        ),
        migrations.RenameModel(
            old_name='Extras',
            new_name='Extra',
        ),
        migrations.RenameModel(
            old_name='Facturas',
            new_name='Factura',
        ),
        migrations.RenameModel(
            old_name='Pedidos',
            new_name='Pedido',
        ),
        migrations.RenameField(
            model_name='pedido',
            old_name='medioDePedido',
            new_name='medioDePago',
        ),
        migrations.RenameModel(
            old_name='RecibosH',
            new_name='Recibo',
        ),
        migrations.DeleteModel(
            name='Reclamos',
        ),
        migrations.AddField(
            model_name='reclamo',
            name='recibo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='databaseManager.recibo'),
        ),
    ]
