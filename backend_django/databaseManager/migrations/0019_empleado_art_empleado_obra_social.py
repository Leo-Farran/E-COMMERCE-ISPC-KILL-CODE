# Generated by Django 4.2.1 on 2023-05-24 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('databaseManager', '0018_rename_monto_extras_monto_extra_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='art',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='databaseManager.arts'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='obra_social',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='databaseManager.obrasocial'),
            preserve_default=False,
        ),
    ]
