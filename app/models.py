# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
import datetime


class Bateria(models.Model):
    cantidad = models.CharField(max_length=1000,blank=True, null=True)
    marca = models.CharField(max_length=1000,blank=True, null=True)
    modelo = models.CharField(max_length=1000,blank=True, null=True)
    precio = models.CharField(max_length=1000,blank=True, null=True)
    cant_bat_usadas= models.CharField(max_length=1000,blank=True, null=True)


class Factura(models.Model):
    ruc = models.CharField(max_length=1000,blank=True, null=True)
    r_social = models.CharField(max_length=1000,blank=True, null=True)
    ruc = models.CharField(max_length=1000,blank=True, null=True)
    direc_r_social = models.CharField(max_length=1000,blank=True, null=True)

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)

    def __unicode__(self):

        return self.nombre


class Produccion(models.Model):
    fecha = models.DateTimeField(help_text=u'Fecha de recepción de la llamada (No se puede modificar)',default=datetime.datetime.today(),editable=False)
            #DATOS DEL CLIENTE
    telefono_1 = models.CharField(help_text=u'Número de teléfono desde donde llama el cliente',max_length=1000,blank=True, null=True)
    telefono_2= models.CharField(help_text=u'Otro nmero de teléfono de contacto',max_length=1000,blank=True, null=True)
    cliente = models.CharField(help_text=u"Nombre del Cliente",max_length=1000,blank=True, null=True)
    dni= models.CharField(help_text=u'Otro nmero de dni',max_length=1000,blank=True, null=True)
    direccion= models.CharField(max_length=1000,blank=True, null=True)

    
          #DATOS DEL VEHICULO 
    marca_vehiculo= models.ForeignKey(Vehiculo,help_text='Marca del vehículo (p.e. Nissan)',max_length=1000,blank=True, null=True)
    modelo= models.CharField(max_length=1000,blank=True, null=True)
    version= models.CharField(max_length=1000,blank=True, null=True)
    serie= models.CharField(max_length=1000,blank=True, null=True)
    anio= models.CharField(max_length=1000,blank=True, null=True)
    motor= models.CharField(max_length=1000,blank=True, null=True)
    cilindrada= models.CharField(max_length=1000,blank=True, null=True)
    color= models.CharField(max_length=1000,blank=True, null=True)
    kilometraje= models.CharField(max_length=1000,blank=True, null=True)
    placa=models.CharField(max_length=1000,blank=True, null=True)
                #Descripcion del Producto (bateria)
    cantidad= models.CharField(max_length=1000,blank=True, null=True)
    marca = models.CharField(max_length=1000,blank=True, null=True)
    modelo_bateria = models.CharField(max_length=1000,blank=True, null=True)
    precio = models.CharField(max_length=1000,blank=True, null=True)
    cantidad_bu= models.CharField(help_text='Cantidad de baterias usadas',max_length=1000,blank=True, null=True)
    descuento = models.CharField(max_length=1000,blank=True, null=True)
    precio_total = models.CharField(max_length=1000,blank=True, null=True)
                #DATOS DE LA ATENCION
    fecha_atencion= models.DateField(max_length=1000,blank=True, null=True)
    hora_instalacion= models.TimeField(max_length=1000,blank=True, null=True)           
    misma_direccion = models.CharField(max_length=1000,blank=True, null=True)
    direccion_atencion= models.CharField(max_length=1000,blank=True, null=True)
    referencia= models.CharField(max_length=1000,blank=True, null=True)
    comprobante= models.CharField(max_length=1000,blank=True, null=True)
    
    boleta= models.BooleanField(max_length=1000,blank=True, default=True)
    factura= models.BooleanField(max_length=1000,blank=True, default=True)
    mismo_cliente= models.CharField(max_length=1000,blank=True, null=True)
    nombre_boleta= models.CharField(max_length=1000,blank=True, null=True)
    direccion1= models.CharField(max_length=1000,blank=True, null=True)
    dni= models.CharField(max_length=1000,blank=True, null=True)
    
            #DATOS DE LA FACTURA
    ruc= models.CharField(max_length=1000,blank=True, null=True)
    razon_social= models.CharField(max_length=1000,blank=True, null=True)
    direccion_rs= models.CharField(max_length=1000,blank=True, null=True)
    pago= models.CharField(max_length=1000,blank=True, null=True)
    correo= models.CharField(max_length=1000,blank=True, null=True)
    atiende= models.CharField(max_length=1000,blank=True, null=True)
    almacen= models.CharField(max_length=1000,blank=True, null=True)
    gmail= models.CharField(max_length=1000,blank=True, null=True)
    estado= models.CharField('Estado',max_length=1000,blank=True, null=True)
    observaciones= models.CharField(max_length=1000,blank=True, null=True)


    def __unicode__(self):
        return self.cliente




# class Gestion(models.Model):
#     fecha = models.CharField(max_length=1000)
#     telef_1 = models.CharField(max_length=1000)
#     cliente = models.CharField(max_length=1000)
#     telef_2= models.CharField(max_length=1000)
#     direccion= models.CharField(max_length=1000)
#     fechaAten= models.CharField(max_length=1000)
#     hora_inst= models.CharField(max_length=1000)
#     vehiculo= models.CharField(max_length=1000)
#     modelo= models.CharField(max_length=1000)
#     serie= models.CharField(max_length=1000)
#     anio= models.CharField(max_length=1000)
#     motor= models.CharField(max_length=1000)
#     color= models.CharField(max_length=1000)
#     kms= models.CharField(max_length=1000)
#     placa=models.CharField(max_length=1000)
#     cantidad = models.CharField(max_length=1000)
#     marca = models.CharField(max_length=1000)
#     modelo_bat = models.CharField(max_length=1000)
#     precio = models.CharField(max_length=1000)
#     cant_bat_usadas= models.CharField(max_length=1000)
#     precio_total = models.CharField(max_length=1000)

#     misma_direcc = models.CharField(max_length=1000)
#     direcc_atencion= models.CharField(max_length=1000)
#     referencia= models.CharField(max_length=1000)
#     doc= models.CharField(max_length=1000)

#     mismo_client= models.CharField(max_length=1000)
#     nombre_boleta= models.CharField(max_length=1000)
#     direcc1= models.CharField(max_length=1000)
#     dni= models.CharField(max_length=1000)

#     pago= models.CharField(max_length=1000)
#     atiende= models.CharField(max_length=1000)
#     almacen= models.CharField(max_length=1000)
#     correo= models.CharField(max_length=1000)
#     stado= models.CharField(max_length=1000)
#     observaciones= models.CharField(max_length=1000)




class Statuspoliza(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'status_poliza'
        verbose_name = 'Status Poliza'

    def __unicode__(self):
        return self.nombre

class Estructura(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'estructura'
        verbose_name = 'Estructura'

    def __unicode__(self):
        return self.nombre


class Jerarquia(models.Model):
    nombre = models.CharField(max_length=1000)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jerarquia'

    def __unicode__(self):
        return self.nombre

class Modalidad(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'modalidad'
        verbose_name = 'Forma Pago'

    def __unicode__(self):
        return self.nombre


class Accion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'accion'

class Nivel(models.Model):
    nombre = models.CharField(max_length=1000)
    descripcion = models.CharField(max_length=1000,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nivel'

    def __unicode__(self):
        return self.nombre

class Grupo(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'grupo'

    def __unicode__(self):
        return self.nombre

class Mes(models.Model):
    nombre = models.CharField('Mes',max_length=1000)

    class Meta:
        managed = False
        db_table = 'mes'
        verbose_name ='Mes'

    def __unicode__(self):
        return self.nombre

class Subgrupo(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'subgrupo'

    def __unicode__(self):
        return self.nombre

class TipoAgente(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'tipo_agente'
        verbose_name = 'Tipos de Agente'

    def __unicode__(self):
        return self.nombre


class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'estado_civil'
        verbose_name = 'Estado Civil'

    def __unicode__(self):
        return self.nombre

class Agente(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user', blank=True, null=True)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente', blank=True, null=True)
    meta_personal = models.IntegerField(blank=True, null=True)
    meta_requerida = models.IntegerField(blank=True, null=True)
    meta_equipo = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    correo_capital = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.FileField(upload_to='static',blank=True, null=True)
    estructura = models.ForeignKey('Estructura', models.DO_NOTHING, db_column='estructura', blank=True, null=True)
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo', blank=True, null=True)
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    nombre = models.CharField(max_length=1000, blank=True, null=True)
    apellidos = models.CharField(max_length=1000, blank=True, null=True)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel')
    #grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='grupo', blank=True, null=True)
    #subgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='subgrupo', blank=True, null=True)
    dni = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    telefono_1 = models.CharField(max_length=1000, blank=True, null=True)
    relacion_contacto = models.CharField(max_length=1000, blank=True, null=True)
    telefono_contacto_emergencia = models.CharField(max_length=1000, blank=True, null=True)
    contacto_emergencia = models.CharField(max_length=1000, blank=True, null=True)
    correo_personal = models.CharField(max_length=1000, blank=True, null=True)
    movil_contacto = models.CharField(max_length=1000, blank=True, null=True)
    version = models.CharField(max_length=1000, blank=True, null=True)
    codigo = models.CharField(max_length=1000, blank=True, null=True)
    tipo_movil = models.CharField(max_length=1000, blank=True, null=True)
    grupo_prueba = models.ForeignKey('Agente', models.DO_NOTHING, db_column='grupo_prueba', blank=True, null=True)
    asesor_anterior = models.CharField(max_length=1000, blank=True, null=True)
    modelo = models.CharField(max_length=1000, blank=True, null=True)
    version_movil = models.CharField(max_length=1000, blank=True, null=True)
    #agente_anterior = models.ForeignKey('Agente', models.DO_NOTHING, db_column='angente_anterior', blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'agente'
        verbose_name = 'Agente'
        ordering = ('nombre',)

    def __unicode__(self):

        if self.user:
            return self.nombre + '  '+ self.apellidos
        else:
            return 'No tiene nombre'
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)



class AuthUser(models.Model):
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    #last_login = models.DateTimeField(blank=True, null=True)
    #is_superuser = models.IntegerField()
    last_name = models.CharField(max_length=30)
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    nacimiento = models.CharField(max_length=1000, blank=True, null=True)
    email = models.CharField('Correo personal',max_length=254,blank=True, null=True)
    correo_capital = models.CharField(max_length=1000, blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    nivel = models.ForeignKey('Nivel', models.DO_NOTHING, db_column='nivel', blank=True, null=True)
    equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo', blank=True, null=True)
    estructura = models.ForeignKey('Estructura', models.DO_NOTHING, db_column='estructura', blank=True, null=True)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente', blank=True, null=True)
    grupo = models.ForeignKey('Grupo', models.DO_NOTHING, db_column='grupo', blank=True, null=True)
    subgrupo = models.ForeignKey('Subgrupo', models.DO_NOTHING, db_column='subgrupo', blank=True, null=True)
    meta_personal = models.IntegerField(blank=True, null=True)
    meta_requerida = models.IntegerField(blank=True, null=True)
    dni = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    telefono = models.CharField(max_length=1000, blank=True, null=True)
    contacto = models.CharField(max_length=1000, blank=True, null=True)
    relacion = models.CharField('Relacion del contacto',max_length=1000, blank=True, null=True)
    movil_contacto = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.FileField(upload_to='static',blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'
        verbose_name = 'Datos de los Usuario'

    def __unicode__(self):
        return self.username


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class Semanas(models.Model):
    numero = models.CharField(max_length=1000)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_fin =  models.DateTimeField(blank=True, null=True)
    anio = models.CharField(max_length=1000)
    mes = models.ForeignKey('Mes', models.DO_NOTHING, db_column='mes')

    class Meta:
        managed = False
        db_table = 'semanas'
        verbose_name = 'Semana'

    def __unicode__(self):

        if self.numero:

            return 'Semana '+str(self.numero) +' Mes '+str(self.mes)

        else:


            return ''



class Citas(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente',blank=True, null=True)
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    agente_cita_equipo = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente_cita_equipo',related_name='agente_cita_equipo', blank=True, null=True)
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente',blank=True, null=True)
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateTimeField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.CharField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad',blank=True, null=True)
    prima_anual = models.CharField(max_length=100,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField(default=False)
    agente_equipo = models.IntegerField(blank=True, null=True)
    numero_poliza = models.CharField('Numero Poliza',max_length=1000,blank=True, null=True)
    cliente_cita_equipo = models.CharField(max_length=1000, blank=True, null=True)
    propuesta_cita_equipo = models.CharField(max_length=1000, blank=True, null=True)
    cliente_antiguo = models.CharField(max_length=1000, blank=True, null=True,default='No')
    ramo_compania_producto = models.ForeignKey('RamoCompaniaProducto', models.DO_NOTHING, db_column='ramo_compania_producto', blank=True, null=True)
    status_poliza = models.ForeignKey('Statuspoliza', models.DO_NOTHING, db_column='status_poliza',default=1,blank=True, null=True)
    upload_csv = models.BooleanField(default=0)
    asesor_anterior = models.CharField(max_length=10000,blank=True, null=True)
    valida_pos = models.BooleanField(default=0)
    upload_csv_julio_enero_2019 = models.BooleanField(default=0)
    upload_ene_jul_2019_ecu=models.BooleanField(default=0)

    class Meta:
        managed = False
        db_table = 'citas'
        verbose_name = 'Cita'
        ordering = ('agente',)

    def __unicode__(self):


        return self.tipo_cita.nombre




class Pos(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente')
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.IntegerField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad',blank=True, null=True)
    prima_anual = models.IntegerField(max_length=1000,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField()
    agente_equipo = models.IntegerField(blank=True, null=True)
    numero_poliza = models.CharField(max_length=1000,blank=True, null=True)
    upload_csv = models.BooleanField(default=0)
    status_poliza = models.ForeignKey('Statuspoliza', models.DO_NOTHING, db_column='status_poliza',default=1,blank=True, null=True)
    asesor_anterior = models.CharField(max_length=10000,blank=True, null=True)
    valida_pos = models.BooleanField(default=0)
    

    class Meta:
        managed = False
        db_table = 'citas'
        verbose_name = 'POS'




class Cierres(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente')
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateField()
    observacion = models.CharField(max_length=10000,blank=True, null=True)
    fecha_solicitud = models.DateTimeField(blank=True, null=True)
    prima_target = models.CharField(max_length=1000,blank=True, null=True)
    modalidad = models.ForeignKey('Modalidad', models.DO_NOTHING, db_column='modalidad',blank=True, null=True)
    prima_anual = models.CharField(max_length=1000,blank=True, null=True)
    fecha_poliza = models.DateTimeField(blank=True, null=True)
    fecha_creacion = models.DateTimeField()
    semana = models.ForeignKey('Semanas', models.DO_NOTHING, db_column='semana',blank=True, null=True)
    inforce = models.BooleanField()
    agente_equipo = models.IntegerField(blank=True, null=True)
    numero_poliza = models.CharField(max_length=1000,blank=True, null=True)
    

    class Meta:
        managed = False
        db_table = 'citas'
        verbose_name = 'Cierre'



class Cliente(models.Model):
    #user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    nombre = models.CharField('Cliente',max_length=1000,blank=True, null=True)
    apellido = models.CharField(max_length=1000,blank=True, null=True)
    email = models.CharField(max_length=1000,blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.CharField(max_length=1000,blank=True, null=True)
    direccion = models.CharField(max_length=1000,blank=True, null=True)
    
    estado_civil = models.ForeignKey('EstadoCivil', models.DO_NOTHING, db_column='estado_civil', blank=True, null=True)
    numero_hijos = models.IntegerField(blank=True, null=True)
    agente = models.ForeignKey('Agente', models.DO_NOTHING, db_column='agente')
    #equipo = models.ForeignKey('Equipo', models.DO_NOTHING, db_column='equipo')
    dni = models.CharField(max_length=1000,blank=True, null=True)


    conyuge = models.CharField(max_length=1000,blank=True, null=True)
    edad_conyuge = models.IntegerField(blank=True, null=True)
    fecha_nacimiento_conyuge = models.DateField(blank=True, null=True)
    upload_csv=models.BooleanField(default=0)
    upload_csv_julio_enero_2019=models.BooleanField(default=0)
    upload_ene_jul_2019_ecu=models.BooleanField(default=0)
    

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        ordering=('nombre',)


    def __unicode__(self):

        if self.nombre and self.apellido:
            return self.nombre + ' '+ self.apellido

        if self.nombre and self.apellido==None:
            return self.nombre

        else:
            return 'No tiene nombre'






class Compania(models.Model):
    nombre = models.CharField('Compania',max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compania'
        verbose_name = 'Compania'

    def __unicode__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipo'
        verbose_name = 'Equipo'

    def __unicode__(self):
        return self.nombre

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'




class Pais(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'
        verbose_name = 'Paise'

    def __unicode__(self):
        return self.nombre


class Relacion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'relacion'


    def __unicode__(self):
        return self.nombre


class ParientesCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    nombre = models.CharField(max_length=1000)
    edad = models.IntegerField(blank=True,null=True)
    fecha_nacimiento =models.DateTimeField(blank=True,null=True)
    relacion = models.ForeignKey('Relacion', models.DO_NOTHING, db_column='relacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parientes_cliente'
        verbose_name = 'Parientes del Cliente'


class Producto(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'producto'
        verbose_name = 'Producto'

    def __unicode__(self):
        return self.nombre




class Ramo(models.Model):
    nombre = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'ramo'

    def __unicode__(self):
        return self.nombre

class Agentejerarquia(models.Model):


    agente=models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente',related_name='agente_asigna',verbose_name='Agente a asignar',default=142)
    country_manager = models.ForeignKey(Agente, models.DO_NOTHING, db_column='country_manager',related_name='country_manager',verbose_name='Country Manager',default=142)
    bussiness_partner = models.ForeignKey(Agente, models.DO_NOTHING, db_column='bussiness_partner',related_name='bussiness_partner',verbose_name='Business Partner',default=142)
    relation_ship_director = models.ForeignKey(Agente, models.DO_NOTHING, db_column='relation_ship_director',related_name='relation_ship_director',verbose_name='Relation Ship Director',default=142)
    relation_management = models.ForeignKey(Agente, models.DO_NOTHING, db_column='relation_management',related_name='relation_management',verbose_name='Relation Management',default=142)
    relation_management_senior = models.ForeignKey(Agente, models.DO_NOTHING, db_column='relation_management_senior',related_name='relation_management_senior',verbose_name='Relation Management Senior',default=142)
    private_client = models.ForeignKey(Agente, models.DO_NOTHING, db_column='private_client',related_name='private_client',verbose_name='Private Client',default=142)
    private_client_senior = models.ForeignKey(Agente, models.DO_NOTHING, db_column='private_client_senior',related_name='private_client_senior',verbose_name='Private Client Senior',default=142)
    class Meta:
        managed = False
        db_table = 'agentejerarquia'
        verbose_name = 'Agente / Jerarquia'

    def __unicode__(self):
        return self.agente.nombre
    @property
    def full_name(self):
        return self.agente.email






class RamoCompaniaProducto(models.Model):
    ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo')
    compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania')
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto')
    antiguo = models.BooleanField(default=0)

    class Meta:
        managed = False
        db_table = 'ramo_compania_producto'

    def __unicode__(self):
        return self.ramo.nombre+' / '+self.compania.nombre+' / '+self.producto.nombre

class PropuestaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente')
    observacion = models.CharField(max_length=10000)
    fecha = models.DateTimeField(blank=True, null=True)
    detalle = models.CharField(max_length=1000)
    ramo_compania_producto = models.ForeignKey('RamoCompaniaProducto', models.DO_NOTHING, db_column='ramo_compania_producto')
    inforce = models.BooleanField()
    interes = models.CharField(max_length=1000, blank=True, null=True)
    upload_csv=models.BooleanField(default=0)
    upload_csv_julio_enero_2019 = models.BooleanField(default=0)
    upload_ene_jul_2019_ecu=models.BooleanField(default=0)

    class Meta:
        managed = False
        db_table = 'propuesta_cliente'

    def __unicode__(self):
        return str(self.id)+'-'+self.ramo_compania_producto.ramo.nombre+' / '+self.ramo_compania_producto.compania.nombre+' / '+self.ramo_compania_producto.producto.nombre



class TelefonoUser(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    numero = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefono_user'
        verbose_name = 'Telefonos del Usuario'



class Estado(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'estado'

    def __unicode__(self):
        return self.nombre

class Log(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user')
    accion = models.ForeignKey(Accion, models.DO_NOTHING, db_column='accion')
    detalle = models.CharField(max_length=1100)

    class Meta:
        managed = False
        db_table = 'log'



class TipoCita(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'tipo_cita'
        verbose_name = 'Tipos de Cita'

    def __unicode__(self):
        return self.nombre


class TipoSeguimiento(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'tipo_seguimiento'
        verbose_name = 'Tipos de Seguimiento'

    def __unicode__(self):
        return self.nombre


class Notificacion(models.Model):
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente', blank=True,null=True)
    nivel = models.ForeignKey(Nivel, models.DO_NOTHING, db_column='nivel', blank=True,null=True)
    pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column='pais', blank=True,null=True)
    mensaje = models.TextField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificacion'



class Agentecliente(models.Model):
    agente = models.ForeignKey(Agente, models.DO_NOTHING, db_column='agente')
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')

    class Meta:
        managed = False
        db_table = 'agentecliente'

class Iconos(models.Model):
    nombre = models.CharField(max_length=10000, blank=True, null=True)
    icono = models.CharField(max_length=10000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iconos'
        verbose_name = 'Icono'

    def __unicode__(self):
        return self.nombre


class Archivo(models.Model):

    TIPO_DOCUMENTO = (
        ('Formulario', 'Formulario'),
        ('Comercial', 'Comercial'),
    )
    ruta = models.FileField(upload_to='static',max_length=100000)
    #user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='usuario')
    nombre =  models.CharField(blank=True, null=True,max_length=10000)
    #pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo')
    compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania')
    tipo_archivo = models.CharField(max_length=1000, choices=TIPO_DOCUMENTO)
    peru = models.BooleanField(default=False)
    ecuador = models.BooleanField(default=False)
    colombia = models.BooleanField(default=False)
    estados_unidos = models.BooleanField('Estados Unidos',default=False)
    bolivia = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'archivos'
        verbose_name = 'Biblioteca'

    def __unicode__(self):
        return self.nombre


