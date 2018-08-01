# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Accion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'accion'


class Agente(models.Model):
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, db_column='user', blank=True, null=True)
    tipo_agente = models.ForeignKey('TipoAgente', models.DO_NOTHING, db_column='tipo_agente', blank=True, null=True)
    meta_personal = models.IntegerField(blank=True, null=True)
    meta_requerida = models.IntegerField(blank=True, null=True)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    correo_capital = models.CharField(max_length=1000, blank=True, null=True)
    photo = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'agente'


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
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    estado_notificacion = models.IntegerField(blank=True, null=True)
    pais = models.ForeignKey('Pais', models.DO_NOTHING, db_column='pais', blank=True, null=True)
    estructura = models.ForeignKey('Estructura', models.DO_NOTHING, db_column='estructura', blank=True, null=True)
    nacimiento = models.DateTimeField(blank=True, null=True)
    correo = models.CharField(max_length=1000, blank=True, null=True)
    dni = models.CharField(max_length=1000, blank=True, null=True)
    direccion = models.CharField(max_length=1000, blank=True, null=True)
    estado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='estado', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


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


class Citas(models.Model):
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente')
    tipo_cita = models.ForeignKey('TipoCita', models.DO_NOTHING, db_column='tipo_cita')
    propuesta_cliente = models.ForeignKey('PropuestaCliente', models.DO_NOTHING, db_column='propuesta_cliente')
    tipo_seguimiento = models.ForeignKey('TipoSeguimiento', models.DO_NOTHING, db_column='tipo_seguimiento')
    fecha_cita = models.DateTimeField()
    observacion = models.CharField(max_length=10000)
    fecha_solicitud = models.DateTimeField()
    prima_target = models.CharField(max_length=1000)
    modalidad = models.CharField(max_length=1000)
    prima_anual = models.CharField(max_length=1000)
    fecha_poliza = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'citas'


class Cliente(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    fecha_inicio = models.DateTimeField(blank=True, null=True)
    estado_civil = models.CharField(max_length=100, blank=True, null=True)
    numero_hijos = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Compania(models.Model):
    nombre = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'compania'


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


class Estado(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'estado'


class Estructura(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'estructura'


class Log(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user')
    accion = models.ForeignKey(Accion, models.DO_NOTHING, db_column='accion')
    detalle = models.CharField(max_length=1100)

    class Meta:
        managed = False
        db_table = 'log'


class Pais(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class ParientesCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    nombre = models.CharField(max_length=1000)
    edad = models.IntegerField()
    relacion = models.ForeignKey('Relacion', models.DO_NOTHING, db_column='relacion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parientes_cliente'


class Producto(models.Model):
    nombre = models.CharField(max_length=1001)

    class Meta:
        managed = False
        db_table = 'producto'


class PropuestaCliente(models.Model):
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente')
    observacion = models.CharField(max_length=10000)
    fecha = models.DateTimeField()
    detalle = models.CharField(max_length=1000)
    ramo_compania_producto = models.ForeignKey('RamoCompaniaProducto', models.DO_NOTHING, db_column='ramo_compania_producto')

    class Meta:
        managed = False
        db_table = 'propuesta_cliente'


class Ramo(models.Model):
    nombre = models.CharField(max_length=1100)

    class Meta:
        managed = False
        db_table = 'ramo'


class RamoCompaniaProducto(models.Model):
    ramo = models.ForeignKey(Ramo, models.DO_NOTHING, db_column='ramo')
    compania = models.ForeignKey(Compania, models.DO_NOTHING, db_column='compania')
    producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto')

    class Meta:
        managed = False
        db_table = 'ramo_compania_producto'


class Relacion(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'relacion'


class TelefonoUser(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='user', blank=True, null=True)
    numero = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telefono_user'


class TipoAgente(models.Model):
    nombre = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_agente'


class TipoCita(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'tipo_cita'


class TipoSeguimiento(models.Model):
    nombre = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'tipo_seguimiento'
