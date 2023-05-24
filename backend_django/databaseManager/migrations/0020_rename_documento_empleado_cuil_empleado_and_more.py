# Generated by Django 4.2.1 on 2023-05-24 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databaseManager', '0019_empleado_art_empleado_obra_social'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empleado',
            old_name='documento',
            new_name='cuil_empleado',
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='cuil',
            new_name='cuit',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='calle',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='numero',
        ),
        migrations.AddField(
            model_name='empresa',
            name='ciudad',
            field=models.CharField(default=0, max_length=200, verbose_name='direccion de la empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='direccion',
            field=models.CharField(default=0, max_length=200, verbose_name='direccion de la empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empresa',
            name='provincia',
            field=models.CharField(default=0, max_length=200, verbose_name='direccion de la empresa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recibosh',
            name='legajo_empleado',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='databaseManager.empleado'),
            preserve_default=False,
        ),
    ]