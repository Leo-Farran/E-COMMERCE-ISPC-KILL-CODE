# Generated by Django 4.2.1 on 2023-05-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databaseManager', '0003_alter_empleados_id_emp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arts',
            name='email',
            field=models.CharField(max_length=300, verbose_name='email de arts'),
        ),
        migrations.AlterField(
            model_name='datos_empleados',
            name='email_per',
            field=models.CharField(max_length=300, verbose_name='email personal del empleado'),
        ),
        migrations.AlterField(
            model_name='datos_empleados',
            name='email_wk',
            field=models.CharField(max_length=300, verbose_name='email de trabajo del empleado'),
        ),
        migrations.AlterField(
            model_name='login',
            name='psw',
            field=models.CharField(max_length=300, verbose_name='contraseña usuario'),
        ),
        migrations.AlterField(
            model_name='obrassociales',
            name='email',
            field=models.CharField(max_length=300, verbose_name='email de la obrasocial'),
        ),
    ]