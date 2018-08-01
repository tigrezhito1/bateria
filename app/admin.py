from django.contrib import admin
from app.models import *
from django.contrib.admin import RelatedOnlyFieldListFilter
from daterange_filter.filter import DateRangeFilter
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from PIL import Image
from resizeimage import resizeimage
import os.path
import json
import requests
from django.contrib import admin
from django.contrib.admin.filters import DateFieldListFilter
import xlwt
from datetime import datetime
import csv



class MyAdminSite(AdminSite):
    site_header = 'POS Administrador'

admin_site = MyAdminSite(name='myadmin')
#admin_site.register(Pos)



# Register your models here.

@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
	list_display = ('id','nombre')

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('id','fecha',)
    

# @admin.register(Estructura)
# class EstructuraAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(Pais)
# class PaisAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(Gestion)
# class GestionAdmin(admin.ModelAdmin):
#     list_display = ('id','fecha')





# @admin.register(Nivel)
# class NivelAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre','descripcion')
#     list_editable = ('nombre',)

# @admin.register(TipoAgente)
# class TipoAgenteAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(Grupo)
# class GrupoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)

# @admin.register(Subgrupo)
# class SubgrupoAdmin(admin.ModelAdmin):
# 	list_display = ('id','nombre')
# 	list_editable = ('nombre',)


# @admin.register(Mes)
# class MesAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)








# @admin.register(TipoCita)
# class TipoCitaAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(TipoSeguimiento)
# class TipoSeguimientoAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)

# @admin.register(Relacion)
# class RelacionAdmin(admin.ModelAdmin):
#     list_display = ('id','nombre')
#     list_editable = ('nombre',)




# def user_logeado(request):

# 	print 'sjsjjjss',request

# class Enviasms(JSONWebTokenAuthMixin, View):

#     ## Agrega telefonos
#     def get(self, request):

#         id_user=request.user.id

		

#         audience = {numero:mensaje}

#         dato = bulksms(audience)

#         return HttpResponse(simplejson.dumps('OK'), content_type="application/json")



def bulksms(audience):

	url ="http://smsbulk.pe/SmsBulk/rest/ws/bulkSms"
	username = 'xiencias'
	password = '9nG4SB'


	for recipient in audience:
		
		phone_number = recipient

		message = audience[recipient]

		if phone_number[:3] == '+51':

			phone_number = phone_number[1:12]

		else:

			if phone_number[:2] != '51':

				phone_number = '51%s' % phone_number





		params = {'usr' : username,'pas' : password,'msg' : message ,'num' : phone_number}


		print 'params...',params

		reply = requests.get(url, params=params)

		result1 = reply.text

		return result1









# @admin.register(Citas)
# class CitasAdmin(admin.ModelAdmin):
# 	list_display = ('id','Asesor_Inicial','Asesor_Responsable')

# 	#'Asesor_Responsable','Cliente','numero_poliza','modalidad','fecha_poliza','prima_anual','status_poliza','fecha_cita','observacion')
# 	#'cliente','get_propuesta_cliente','get_tipo_seguimiento','fecha_cita','fecha_creacion','prima_target','prima_anual','inforce')
# 	list_filter = ('upload_csv','semana__mes__nombre','propuesta_cliente__ramo_compania_producto__compania__nombre','tipo_cita__nombre','tipo_seguimiento__nombre',CitasListFilter,('fecha_cita', DateRangeFilter),'agente','semana')
# 	#list_editable = ('prima_anual',)
# 	search_fields=('id','prima_target','cliente__nombre')
# 	actions=['genera_resumen_citas_por_agente_xls']


# 	def Asesor_Inicial(self, obj):
# 		return obj.agente.nombre

# 	def Asesor_Responsable(self, obj):
# 		return obj.agente.nombre

# 	# def que_semana(self, obj):
# 	# 	return obj.semana.id

# 	# def mes(self, obj):
# 	# 	return obj.semana.mes



# 	# # def agente(self, obj):
# 	# # 	return obj.agente.nombre + ' ' +obj.agente.apellidos

# 	# def get_tipo_seguimiento(self, obj):
# 	# 	return obj.tipo_seguimiento.nombre

# 	# def get_tipo_cita(self, obj):
# 	# 	return obj.tipo_cita.nombre

# 	def Cliente(self, obj):

# 		if obj.cliente:
# 			return obj.cliente.nombre+' '+obj.cliente.apellido
# 		else:
# 			return '_'




# 	def genera_resumen_citas_por_agente_xls(self, request,queryset):

# 		print 'request',request

# 		grupo = User.objects.get(pk=request.user.id).groups.get()

# 		equipo = Agente.objects.get(user_id=request.user.id).equipo.nombre

# 		my_filter={}

# 		if str(grupo)!='ADMIN':

# 			my_filter['equipo__nombre'] = equipo


# 		print 'grupo',grupo

# 		fecha_cita__gte = '1/1/1000'

# 		fecha_cita__lte = '1/12/4000'

# 		fecha_cita__gte=datetime.strptime(str(fecha_cita__gte), '%d/%m/%Y')

# 		fecha_cita__lte=datetime.strptime(str(fecha_cita__lte), '%d/%m/%Y')

# 		for r in request.GET:

# 			if r=='agente__nombre':

# 				agente = request.GET['agente__nombre']

# 				my_filter['nombre'] = agente

# 			if r=='drf__fecha_cita__gte':

# 				fecha_cita__gte = request.GET['drf__fecha_cita__gte']

# 				fecha_cita__gte=datetime.strptime(str(fecha_cita__gte), '%d/%m/%Y')


# 			if r=='drf__fecha_cita__lte':

# 				fecha_cita__lte = request.GET['drf__fecha_cita__lte']

# 				fecha_cita__lte=datetime.strptime(str(fecha_cita__lte), '%d/%m/%Y')




# 		c  = Agente.objects.filter(**my_filter).values('id','nombre','apellidos','equipo').order_by('nombre')

# 		response = HttpResponse(content_type='text/csv')

# 		response['Content-Disposition'] = 'attachment; filename="Citas.csv'

# 		writer = csv.writer(response)

# 		writer.writerow(['Agente','# Nuevos Prospectos','# Citas Equipo ','# Seguimiento','# POS','# Cierre','#Entrega'])

# 		for i in range(len(c)):

# 			c[i]['nombre'] = c[i]['nombre'].encode('ascii','ignore')

# 			c[i]['nombre'] = c[i]['nombre'].encode('ascii','replace')


# 			c[i]['apellidos'] = c[i]['apellidos'].encode('ascii','ignore')

# 			c[i]['apellidos'] = c[i]['apellidos'].encode('ascii','replace')


# 			print fecha_cita__lte

# 			nuevos = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

# 			seguimiento = Citas.objects.filter(agente_id=c[i]['id'],tipo_seguimiento__nombre='Seguimiento').count()

# 			pos = Citas.objects.filter(agente_id=c[i]['id'],tipo_seguimiento__nombre='POS').count()

# 			cierre = Citas.objects.filter(agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre').count()

# 			entrega = Citas.objects.filter(agente_id=c[i]['id'],tipo_seguimiento__nombre='Entrega').count()

# 			citaequipo = Citas.objects.filter(agente_id=c[i]['id'],tipo_cita__nombre='Cita de Equipo').count()

# 			writer.writerow([c[i]['nombre'] +' '+c[i]['apellidos'] ,nuevos,citaequipo,seguimiento,pos,cierre,entrega])

# 		return response

# 	def get_propuesta_cliente(self, obj):

# 		if obj.propuesta_cliente:
# 			return obj.propuesta_cliente.ramo_compania_producto.ramo.nombre +'/'+obj.propuesta_cliente.ramo_compania_producto.compania.nombre+'/'+obj.propuesta_cliente.ramo_compania_producto.producto.nombre
# 		else:
# 			return ''


# 	def get_tipo_seguimiento(self, obj):
# 		return obj.tipo_seguimiento.nombre






