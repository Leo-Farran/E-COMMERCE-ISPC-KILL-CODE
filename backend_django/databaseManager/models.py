from django.db.models import Sum
from django.db import models


class Empleado(models.Model):
    legajo = models.IntegerField(primary_key=True)
    nombre = models.CharField('nombre del empleado', max_length=200)
    apellido = models.CharField('apellido del empleado', max_length=200)
<<<<<<< HEAD
    # Resto de los campos del modelo Empleado

=======
    calle = models.CharField('calle donde vive el empleado',max_length=200)
    casa_piso_numero = models.IntegerField()
    provincia = models.CharField('provincia del empleado', max_length=200)
    email = models.CharField('email personal del empleado',max_length=200)
    telefono = models.BigIntegerField()
    cargo = models.CharField('cargo del empleado', max_length=200)
    categoria = models.CharField('categoria del empleado',max_length=200)
    fecha_ingreso = models.DateField()
    fecha_nacimiento= models.DateField('fecha de nacimiento')
    ciudad = models.CharField('ciudad del empleado',max_length=200)
    cuil_empleado = models.BigIntegerField('cuil del empleado')
    obra_social = models.OneToOneField('ObraSocial', on_delete=models.CASCADE, related_name='empleados')
    art = models.OneToOneField('Arts', on_delete=models.CASCADE)
>>>>>>> main

class Empresa(models.Model):
    cuit = models.BigIntegerField(primary_key=True)
    nombre = models.CharField('nombre de la empresa', max_length=200)
    direccion = models.CharField('direccion de la empresa', max_length=200)
    empleado = models.ForeignKey(
        Empleado, blank=True, null=True, on_delete=models.CASCADE)
    # Resto de los campos del modelo Empresa


class Arts(models.Model):
    id_art = models.IntegerField(primary_key=True)
    nombre = models.CharField('nombre de arts', max_length=200)
    email = models.CharField('email de arts', max_length=200)
    telefono = models.BigIntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    # Resto de los campos del modelo Arts


class ObraSocial(models.Model):
    id_ObraSocial = models.IntegerField(primary_key=True)
    telefono = models.BigIntegerField()
    email = models.CharField('email de la obrasocial', max_length=200)
    nombre = models.CharField('nombre de la obrasocial', max_length=200)
    # Resto de los campos del modelo ObraSocial


class Deducciones(models.Model):
    cod_deduccion = models.IntegerField(primary_key=True)
<<<<<<< HEAD
    monto_deduccion = models.DecimalField(max_digits=8, decimal_places=2)
    causa_deduccion = models.CharField('causa de deducción', max_length=200)
    # Resto de los campos del modelo Deducciones


=======
    porcentaje_deduccion = models.DecimalField(max_digits=8, decimal_places=2)
    causa_deduccion = models.CharField('causa de deducción',max_length=200)
    
>>>>>>> main
class Extras(models.Model):
    cod_extra = models.IntegerField(primary_key=True)
    causa_extra = models.CharField('tipo de extra', max_length=200)
    monto_extra = models.DecimalField(max_digits=8, decimal_places=2)
    # Resto de los campos del modelo Extras


class RecibosH(models.Model):
    id_recibo = models.IntegerField(primary_key=True)
    montoBruto = models.DecimalField(max_digits=8, decimal_places=2)
    montoNeto = models.DecimalField(max_digits=8, decimal_places=2)
    periodo = models.DateField('periodo')
    antiguedad = models.IntegerField()
<<<<<<< HEAD
    concepto = models.CharField('descripción de reciboh', max_length=200)
    cantidad = models.IntegerField('cantidad de concepto')
    valor_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    remuneracion = models.DecimalField(max_digits=8, decimal_places=2)
=======
    concepto = models.CharField('descripción de reciboh',max_length=200)
>>>>>>> main
    asistencia = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_pago = models.DateField('fecha del pago')
    deduccion = models.ForeignKey(Deducciones, on_delete=models.CASCADE)
    extra = models.ForeignKey(Extras, blank=True, null=True, on_delete=models.CASCADE, default=0)
    legajo_empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)

    def calcular_monto_neto(self):
<<<<<<< HEAD
        self.montoNeto = self.montoBruto + \
            self.extra.monto_extra - self.deduccion.monto_deduccion
        self.save()

    def remuneracion_concepto(self):
        self.remuneracion = self.cantidad * self.valor_unitario
        self.save()


=======
        monto_deduccion = self.montoBruto * (self.deduccion.porcentaje_deduccion / 100)
        if self.extra is None:
            self.montoNeto = self.montoBruto + self.asistencia - monto_deduccion
        else:
            self.montoNeto = self.montoBruto + self.extra.monto_extra + self.asistencia - monto_deduccion
        self.save()

        
>>>>>>> main
class Reclamos(models.Model):
    id_recla = models.IntegerField(primary_key=True)
    recibo = models.OneToOneField(
        RecibosH, blank=True, null=True, on_delete=models.CASCADE)
    empleado = models.OneToOneField(
        Empleado, blank=True, null=True, on_delete=models.CASCADE)
    estado = models.CharField('estado de reclamo', max_length=200)
    descripcion = models.CharField('descripción de reclamo', max_length=200)
    fecha = models.DateField('fecha')
    tipo = models.CharField('tipo de reclamo', max_length=200)
    # Resto de los campos del modelo Reclamos


class ServiciosKillCode(models.Model):
    idServicio = models.IntegerField(primary_key=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    detalle = models.CharField(
        'detalle de servicio de kill code', max_length=200)
    nombreServicio = models.CharField(
        'nombre de servicio de kill code', max_length=200)
    # Resto de los campos del modelo ServiciosKillCode


class Pedidos(models.Model):
    idPedido = models.IntegerField(primary_key=True)
    valorTotal = models.DecimalField(max_digits=8, decimal_places=2)
    detalle = models.CharField('detalle de pedidos', max_length=200)
    cantidad = models.IntegerField()
    Servicio = models.ForeignKey(
        ServiciosKillCode, blank=True, null=True, on_delete=models.CASCADE)
    medioDePedido = models.CharField(
        'medio de pago para pedidos', max_length=200)
    Empresa = models.OneToOneField(
        Empresa, blank=True, null=True, on_delete=models.CASCADE)
    fechaHora = models.DateTimeField()

    def actualizar_valor_total(self):
        total_servicios = self.servicio_set.aggregate(total=Sum('valor'))
        self.valorTotal = total_servicios['total'] or 0
        self.save()


class Facturas(models.Model):
    idFactura = models.IntegerField(primary_key=True)
    valorFactura = models.DecimalField(max_digits=8, decimal_places=2)
    detalleFactura = models.CharField('detalle de la factura', max_length=200)
    Pedido = models.OneToOneField(
        Pedidos, blank=True, null=True, on_delete=models.CASCADE)
    cuitKillCode = models.IntegerField()
    tipoFactura = models.CharField('tipo de factura', max_length=200)
    IVA = models.DecimalField(max_digits=8, decimal_places=2)
    fechaHora = models.DateTimeField()

    def save(self, *args, **kwargs):
        if self.Pedido:
            self.valorFactura = self.Pedido.valorTotal * self.IVA
        super().save(*args, **kwargs)


class Contacto(models.Model):
    nombre = models.CharField('nombre de quien contacta', max_length=200)
    email = models.EmailField()
    comentario = models.CharField(max_length=500)
    # Resto de los campos del modelo Contacto
