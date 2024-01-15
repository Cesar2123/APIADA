from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class sesion(models.Model):
    id_user = models.IntegerField(primary_key=True,db_column='idUser')
    name = models.CharField(max_length=100, db_column="Nombre")
    email = models.CharField(max_length=100, db_column="Correo")
    pas = models.CharField(max_length=100, db_column="Pass")
    class Meta:
        db_table = 'Ingreso'
        
    # tabla de respuestas
class formulario(models.Model):
    id_respuesta = models.IntegerField(primary_key=True,db_column='idrespuesta')
    name1 = models.CharField(max_length=100, db_column="Nombres")
    apellidop = models.CharField(max_length=100, db_column="Apellidop")
    apellidom = models.CharField(max_length=100, db_column="Apellidom")
    matricula = models.CharField(max_length=100, db_column="Matricula")
    consideras = models.CharField(max_length=100, db_column="Considerascom")
    compra = models.CharField(max_length=100, db_column="Compraint")
    notificacion = models.CharField(max_length=100, db_column="Notwhats")
    experiencia = models.CharField(max_length=100, db_column="Maneraco")
    productos = models.CharField(max_length=100, db_column="Producnu")
    pago = models.CharField(max_length=100, db_column="pagotarj")
    
    class Meta:
        db_table = 'Formulario'

class cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=100, db_column='nombre')
    edad = models.IntegerField(db_column='edad')
    domicilio = models.TextField(db_column='Domicilio')
    telefono = models.TextField(max_length=100, db_column='telefono')
    

    class Meta: 
        db_table='cliente'

class producto(models.Model):
    idProducto = models.AutoField(primary_key=True,db_column='id_producto')
    nombre = models.CharField(max_length=100, db_column='nombre')
    descripcion = models.CharField(max_length=100, db_column='descripcion')
    precio = models.CharField(max_length=100, db_column='precio')
    stock = models.CharField(max_length=100, db_column='stock')
    class Meta: 
        db_table = 'producto'

class pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True, db_column='id_pedido')
    idCliente = models.ForeignKey(cliente, on_delete=models.CASCADE, db_column='id_cliente')
    fecha_pedido = models.DateField(db_column='fecha_pedido')
    paqueteria = models.CharField(max_length=100, db_column='paqueteria')
    numSeguimiento = models.CharField(max_length=100, db_column='num_seguimiento')
    estado = models.CharField(max_length=100, db_column='estado')
    class Meta: 
        db_table = 'pedido'

class detalle_pedido(models.Model):
    idDetalle = models.AutoField(primary_key=True, db_column='id_detalle')
    id_pedido = models.ForeignKey(pedido, on_delete=models.CASCADE, db_column='id_pedido', )
    id_producto = models.ForeignKey(producto, on_delete=models.CASCADE, db_column='id_producto')
    class Meta:
        db_table = 'detalle_pedido'
    
class vehiculo (models.Model):
    idVehiculo = models.AutoField(primary_key=True, db_column='id_vehiculo')
    modelo = models.CharField(max_length=50, db_column='modelo')
    matricula = models.CharField(max_length=50, db_column='matricula')
    class Meta:
        db_table = 'vehiculo'

class repartidor (models.Model):
    idRepartidor = models.AutoField(primary_key=True, db_column='id_repartidor')
    nombre = models.CharField(max_length=100, db_column='nombre')
    aPaterno = models.CharField(max_length=100, db_column='aPaterno')
    aMaterno = models.CharField(max_length=100, db_column='aMaterno')
    edad = models.IntegerField(db_column='edad')
    correo = models.CharField(max_length=100,unique=True,db_column='correo')
    domicilio = models.TextField(db_column='Domicilio')
    telefono = models.TextField(max_length=100, db_column='telefono')
    curp = models.TextField(max_length=18, db_column='curp')
    nss = models.TextField(max_length=20, db_column='nss')
    idVehiculo = models.ForeignKey(vehiculo, on_delete=models.CASCADE, db_column='id_vehiculo')
    class Meta:
        db_table = 'repartidor'



