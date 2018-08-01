#    ___       ___       ___       ___            ___       ___   
#   /\  \     /\__\     /\  \     /\__\          /\  \     /\  \  
#  /  \  \   / | _|_   /  \  \   |  L__L        _\ \  \   /  \  \ 
# /  \ \__\ /  |/\__\ / /\ \__\  |   \__\      /\/  \__\ / /\ \__\
# \/\  /  / \/|  /  / \ \/ /  /  /   /__/      \  /\/__/ \ \/ /  /
#   / /  /    | /  /   \  /  /   \/__/          \/__/     \  /  / 
#   \/__/     \/__/     \/__/                              \/__/

# email : joelunmsm@gmail.com
# web   : xiencias.com



from django.shortcuts import *
from django.template import RequestContext
from django.contrib.auth import *
from django.views.generic import View
from django.contrib.auth.models import Group, User
from django.core import serializers
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import Group, User
from jwt_auth.compat import json
from jwt_auth.mixins import JSONWebTokenAuthMixin
from django.template import RequestContext
import simplejson
from django.views.decorators.csrf import csrf_exempt
import xlrd
from django.db.models import Count,Sum
from app.models import *
from app.serializers import *
from django.db.models import Count,Sum
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer

from django.contrib.auth import authenticate
import time
from django.db.models import Func
import os
from datetime import datetime,timedelta,date
import os.path
import requests
import smtplib
from email.mime.text import MIMEText
from django.db.models import Count,Max
import datetime
import random
from django.db.models import Count,Sum
from PIL import Image
from resizeimage import resizeimage
import unicodecsv as csv
import pandas as pd


class Uploadphoto(JSONWebTokenAuthMixin, View):

	#Retorna datos del agente
	def post(self, request):

		caption = request.FILES['file']

		#Guarda foto

		id_user =request.user.id

		a = Agente.objects.get(user_id=id_user)

		a.photo = caption

		a.save()

		caption = '/home/capital/'+str(Agente.objects.get(user_id=id_user).photo)

		fd_img = open(caption, 'r')

		img = Image.open(fd_img)

		width, height = img.size

		img = resizeimage.resize_cover(img, [300, 300])

		img.save(caption, img.format)

		fd_img.close()

		a= simplejson.dumps('OK')
		
		return HttpResponse(a, content_type="application/json")




def mobile(request):
	"""Return True if the request comes from a mobile device."""
	MOBILE_AGENT_RE=re.compile(r".*(iphone|mobile|androidtouch)",re.IGNORECASE)
	if MOBILE_AGENT_RE.match(request.META['HTTP_USER_AGENT']):
		return True
	else:
		return False

def ValuesQuerySetToDict(vqs):

	return [item for item in vqs]

def traesemana(fecha_inicio):

	id =1

	if Semanas.objects.filter(fecha_inicio__lte=fecha_inicio,fecha_fin__gte=fecha_inicio).count()>0:

		id = Semanas.objects.get(fecha_inicio__lte=fecha_inicio,fecha_fin__gte=fecha_inicio).id

	else:

		id=58

	return id







	
	#Actualiza datos
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)
		telefono = None

		a = Agente.objects.get(user_id=id)

		for i in data:


			data['meta_requerida']=float(str(data['meta_requerida']).replace(',',''))
			data['meta_personal']=float(str(data['meta_personal']).replace(',',''))



			if i=='tipo_agente' :tipo_agente=data['tipo_agente']
			if i=='meta_personal' :a.meta_personal=data['meta_personal']
			if i=='meta_requerida' :a.meta_requerida=data['meta_requerida']
			if i=='correo_capital' :a.correo_capital=data['correo_capital']
			if i=='user__email' :email=data['user__email']
			if i=='photo' :a.photo=data['photo']
			if i=='user__direccion' :a.direccion=data['user__direccion']
			if i=='user__dni' :a.dni=data['user__dni']
			if i=='telefono':a.telefono=data['telefono']
			if i=='telefono_1':a.telefono_1=data['telefono_1']
			if i=='password':
				u = User.objects.get(id=id)
				u.set_password(data['password'])
				u.save()



			if i=='telefono':
				TelefonoUser(user_id=a.user.id,numero=data['telefono']).save()

	
		a.save()



		a= simplejson.dumps('OK')
		return HttpResponse(a, content_type="application/json")

	#Retorna datos del agente
	def get(self, request):



		
		id =request.user.id
		a = Agente.objects.filter(user_id=id).values('user','photo','id','estructura__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','photo','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username','pais__nombre','telefono_1','nivel__nombre','telefono')
		fmt = '%d %b %Y'
		for j in range(len(a)):

			if Agente.objects.get(id=a[j]['id']).fecha_ingreso:
				a[j]['fecha_ingreso'] = Agente.objects.get(id=a[j]['id']).fecha_ingreso.strftime(fmt)
			if Agente.objects.get(id=a[j]['id']).user.nacimiento:
				a[j]['fecha_nacimiento'] = Agente.objects.get(id=a[j]['id']).user.nacimiento

			a[j]['meta_requerida']="{:,}".format(a[j]['meta_requerida'])
			a[j]['meta_personal']="{:,}".format(a[j]['meta_personal'])


		a= simplejson.dumps(ValuesQuerySetToDict(a))
		return HttpResponse(a, content_type="application/json")


class Listacliente(JSONWebTokenAuthMixin, View):

	# Retorna datos del agente
	def get(self,request,cliente):

		#id_user_cliente = Cliente.objects.get(id=cliente).user.id

		a =Cliente.objects.filter(id=cliente).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','direccion','email','telefono','edad_conyuge')
		
		fmt = '%d/%m/%Y'
		
		for j in range(len(a)):

			if Cliente.objects.get(id=a[j]['id']).fecha_inicio: 
				a[j]['fecha_inicio'] = Cliente.objects.get(id=a[j]['id']).fecha_inicio.strftime(fmt)
			if Cliente.objects.get(id=a[j]['id']).fecha_nacimiento:

				if Cliente.objects.get(id=a[j]['id']).fecha_nacimiento > datetime.date(1900, 01, 01):

					a[j]['fecha_nacimiento'] = Cliente.objects.get(id=a[j]['id']).fecha_nacimiento.strftime(fmt)

				else:

					a[j]['fecha_nacimiento'] = '01/01/1901'

				#a[j]['fecha_nacimiento'] = Cliente.objects.get(id=a[j]['id']).fecha_nacimiento.strftime(fmt)

				act_year = datetime.datetime.today().year

				fecha_nacimiento = str(a[j]['fecha_nacimiento'])[0:10]

				fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento,'%d/%m/%Y')

				diff = (datetime.datetime.today() - fecha_nacimiento).days

				if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
					yeardays += 1
				else:
					yeardays = 365
					years = str(int(diff/yeardays))



				a[j]['edad'] = years
			
			if Cliente.objects.get(id=a[j]['id']).fecha_nacimiento_conyuge:
				a[j]['fecha_nacimiento_conyuge'] = Cliente.objects.get(id=a[j]['id']).fecha_nacimiento_conyuge.strftime(fmt)
			

			if Cliente.objects.get(id=a[j]['id']).conyuge:
				a[j]['conyugeflag']=True

			# if TelefonoUser.objects.filter(user_id=id_user_cliente).count()>0:
			#   a[j]['telefono'] = TelefonoUser.objects.filter(user_id=id_user_cliente).order_by('-id').values('numero')[0]

			p=ParientesCliente.objects.filter(cliente_id=cliente,relacion_id=2).values('id','nombre','edad','relacion__nombre')

			fmt = '%d/%m/%Y'

			for pa in range(len(p)):

				if ParientesCliente.objects.get(id=p[pa]['id']).fecha_nacimiento:

					p[pa]['fecha_nacimiento']=ParientesCliente.objects.get(id=p[pa]['id']).fecha_nacimiento.strftime(fmt)

			a[j]['parientes']=ValuesQuerySetToDict(p)

			a[j]['numero_hijos']=p.count()

		a= simplejson.dumps(ValuesQuerySetToDict(a))

		return HttpResponse(a, content_type="application/json")

class Citasagente(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def get(self, request):

		id =request.user.id

		id_agente = Agente.objects.get(user_id=id).id

		c =Citas.objects.filter(agente_id=id_agente).exclude(cliente_antiguo='Yes').values('id','tipo_cita__nombre','tipo_seguimiento__nombre','cliente__nombre','cliente__apellido','propuesta_cliente__ramo_compania_producto__ramo__nombre','propuesta_cliente__ramo_compania_producto__compania__nombre','propuesta_cliente__ramo_compania_producto__producto__nombre','propuesta_cliente__interes').order_by('-id')

		#d =Citas.objects.filter(agente_cita_equipo_id=id_agente,tipo_cita__nombre='Cita de Equipo').exclude(cliente_antiguo='Yes').values('id','tipo_cita__nombre','tipo_seguimiento__nombre','cliente__nombre','cliente__apellido','propuesta_cliente__ramo_compania_producto__ramo__nombre','propuesta_cliente__ramo_compania_producto__compania__nombre','propuesta_cliente__ramo_compania_producto__producto__nombre').order_by('-id')

		#'cliente__user__first_name','agente__user__first_name','tipo_cita__nombre','',,,'tipo_seguimiento__nombre','observacion','prima_target','modalidad__nombre','prima_anual')
		
		fmt = '%d/%m/%Y'

		#'observacion','id','prima_target','modalidad__nombre','prima_anual','inforce','tipo_cita__nombre','tipo_seguimiento__nombre',

		for j in range(len(c)):


			if c[j]['tipo_cita__nombre'] == 'Cita de Equipo':

				if Citas.objects.get(id=c[j]['id']).ramo_compania_producto!=None:

					c[j]['propuesta_cliente__ramo_compania_producto__ramo__nombre'] =Citas.objects.get(id=c[j]['id']).ramo_compania_producto.ramo.nombre

					c[j]['propuesta_cliente__ramo_compania_producto__compania__nombre'] =Citas.objects.get(id=c[j]['id']).ramo_compania_producto.compania.nombre

					c[j]['propuesta_cliente__ramo_compania_producto__producto__nombre'] =Citas.objects.get(id=c[j]['id']).ramo_compania_producto.producto.nombre

					c[j]['cliente__nombre'] = Citas.objects.get(id=c[j]['id']).cliente_cita_equipo


			if Citas.objects.filter(id=c[j]['id']).count()>0:

				#print c[j]['cliente__nombre']

				#print c[j]['id']

				#print c[j]['propuesta_cliente__ramo_compania_producto__ramo__nombre']

				#print 'prima_anual....',Citas.objects.get(id=c[j]['id']).prima_anual


				if Citas.objects.get(id=c[j]['id']).fecha_cita:

					c[j]['fecha_cita'] = Citas.objects.get(id=c[j]['id']).fecha_cita.strftime(fmt)

				if Citas.objects.get(id=c[j]['id']).fecha_solicitud:

					c[j]['fecha_solicitud'] = Citas.objects.get(id=c[j]['id']).fecha_solicitud.strftime(fmt)

				if Citas.objects.get(id=c[j]['id']).fecha_poliza:

					c[j]['fecha_poliza'] = Citas.objects.get(id=c[j]['id']).fecha_poliza.strftime(fmt)

				if Citas.objects.get(id=c[j]['id']).observacion:

					c[j]['observacion'] = Citas.objects.get(id=c[j]['id']).observacion

				if Citas.objects.get(id=c[j]['id']).prima_target:

					primatar = Citas.objects.get(id=c[j]['id']).prima_target.split('.')

					if len(primatar)==2:

						primatar = int(Citas.objects.get(id=c[j]['id']).prima_target.split('.')[0])

					else:

						primatar = int(Citas.objects.get(id=c[j]['id']).prima_target)

					c[j]['prima_target'] = primatar

					c[j]['prima_target_label'] = "{:,}".format(int(c[j]['prima_target']))

				if Citas.objects.filter(id=c[j]['id']).values('modalidad__nombre'):

					c[j]['modalidad__nombre'] = Citas.objects.filter(id=c[j]['id']).values('modalidad__nombre')[0]['modalidad__nombre']

				if Citas.objects.get(id=c[j]['id']).prima_anual:


					print 'Entre....'

					primatar = Citas.objects.get(id=c[j]['id']).prima_anual.split('.')

					if len(primatar)==2:

						primatar = int(Citas.objects.get(id=c[j]['id']).prima_anual.split('.')[0])

					else:

						primatar = int(Citas.objects.get(id=c[j]['id']).prima_anual)


					print 'prima_anual....',primatar

					c[j]['prima_anual'] = primatar

					c[j]['prima_anual_label'] = "{:,}".format(int(c[j]['prima_anual']))

				if Citas.objects.get(id=c[j]['id']).inforce:

					c[j]['inforce'] = Citas.objects.get(id=c[j]['id']).inforce

				if Citas.objects.get(id=c[j]['id']).tipo_cita:

					c[j]['tipo_cita__nombre'] = Citas.objects.get(id=c[j]['id']).tipo_cita.nombre

				if Citas.objects.get(id=c[j]['id']).tipo_cita.nombre=='Nuevo Prospecto de Cliente':

					c[j]['tipo_cita__nombre'] = 'NP'

				if Citas.objects.get(id=c[j]['id']).tipo_seguimiento.nombre=='Entrega':

					c[j]['tipo_cita__nombre'] = 'EP'


				


				c[j]['muestralabel']=True

				c[j]['muestranumero']=False


		v=ValuesQuerySetToDict(c)

		c= simplejson.dumps(v)

		return HttpResponse(c, content_type="application/json")

class Termometro(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def get(self, request):

		id =request.user.id

		agente = Agente.objects.get(user_id=id).id

		con = 0

		#ncitasreal = Citas.objects.filter(agente_id=agente,tipo_cita__nombre='Nuevo Prospecto de Cliente').annotate(total=Count('cliente')).count()

		cli = Cliente.objects.filter(agente_id=agente)

		for i in cli:



			if Citas.objects.filter(cliente_id=i.id,tipo_cita__nombre='Nuevo Prospecto de Cliente').exclude(cliente_antiguo='Yes').count()>0:

				con = con+1

		ncitasreal = con

		#ncitasreal = Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='Nuevo').count()

		#totalcitasesperado = (4*4+5)*5  #total de citas al anio # 260

		totalcitasesperado = 260


		nsem = sacasemana(str(datetime.datetime.today())[0:10])

		citaesperadoafecha = nsem*5

		porcentajeesperado = citaesperadoafecha*100/totalcitasesperado

		porcentareal = float(ncitasreal*100)/float(totalcitasesperado)



		alertanumero = ncitasreal*100/float(nsem*5)

		if int(porcentareal)<int(porcentajeesperado):
			estado='alerta'
		else:
			estado='exito'

		if int(porcentareal)==int(porcentajeesperado):
			estado='umbral'

		data={'estado':estado,'porcentaje':porcentareal,'porcentajeesperado':porcentajeesperado,'totalcitasesperado':totalcitasesperado}

		c= simplejson.dumps(data)
		return HttpResponse(c, content_type="application/json")


class Updatecita(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def post(self, request):

		data = json.loads(request.body)

		id_agente = Agente.objects.get(user_id=request.user.id).id

		# cit_ = Citas.objects.all()

		# for ci in cit_:

		# 	if int(Semanas.objects.filter(fecha_inicio__lte=ci.fecha_cita,fecha_fin__gte=ci.fecha_cita).count())==1:

		# 		se = Semanas.objects.get(fecha_inicio__lte=ci.fecha_cita,fecha_fin__gte=ci.fecha_cita)

		# 		ci.semana_id=se.id

		# 		ci.save()

		if Citas.objects.filter(id=data['id']).count()>0:

			c = Citas.objects.get(id=data['id'])

			pro = Citas.objects.get(id=data['id']).propuesta_cliente.id

			fecha_cita=None
			prima_target=None
			prima_anual=None
			fecha_solicitud=None
			fecha_poliza=None


			for da in data:

			 	if da=='fecha_cita': fecha_cita= data['fecha_cita']
			 	if da=='prima_target': prima_target=data['prima_target']
			 	if da=='prima_anual': prima_anual=data['prima_anual']
			 	if da=='fecha_solicitud': fecha_solicitud=data['fecha_solicitud']
			 	if da=='fecha_poliza': fecha_poliza=data['fecha_poliza']

			Citas.objects.filter(propuesta_cliente_id=pro,agente_id=id_agente).update(fecha_cita=fecha_cita,prima_target=prima_target,prima_anual=prima_anual,fecha_poliza=fecha_poliza)

			for d in data:

				if d =='fecha_cita': c.fecha_cita = data['fecha_cita']
				if d =='observacion': c.observacion = data['observacion']
				if d =='prima_target': c.prima_target = data['prima_target']
				if d =='prima_anual': c.prima_anual = data['prima_anual']
				if d =='fecha_solicitud': c.fecha_solicitud = data['fecha_solicitud']
				if d =='fecha_poliza': c.fecha_poliza = data['fecha_poliza']

			#print len(c.fecha_cita.split('/'))

			#if len(c.fecha_cita.split('/'))==1:

			c.save()

			return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

		else:

			return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Buscaarchivos(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def post(self, request):

		if request.body:

			data = json.loads(request.body)

			pais = Agente.objects.get(user_id=request.user.id).pais.nombre

			my_filter={}

			#my_filter['pais__nombre'] = pais

			if pais=='Ecuador':

				my_filter['ecuador']=1

			if pais=='Bolivia':

				my_filter['bolivia']=1

			if pais=='Estados Unidos':

				my_filter['estados_unidos']=1

			if pais=='Peru':

				my_filter['peru']=1

			if pais=='Colombia':

				my_filter['colombia']=1

			#{u'pais': u'Ecuador', u'cia': 2, u'ramo': {u'nombre': u'Vida', u'id': 1}, u'tipo_documento': u'Formularios'}

			for d in data:

				if d=='cia' : cia = data['cia']; my_filter['compania_id'] = cia
				if d=='ramo' : ramo = data['ramo']['id']; my_filter['ramo'] = ramo
				if d=='tipo_documento': tipo_documento = data['tipo_documento']; my_filter['tipo_archivo'] = tipo_documento

			_archivos = Archivo.objects.filter(**my_filter).values('nombre','ruta','ramo__nombre','compania__nombre').order_by('nombre')

			a= simplejson.dumps(ValuesQuerySetToDict(_archivos))

			return HttpResponse(a, content_type="application/json")

		else:

			pais = Agente.objects.get(user_id=request.user.id).pais.nombre

			my_filter={}

			#my_filter['pais__nombre'] = pais

			if pais=='Ecuador':

				my_filter['ecuador']=1

			if pais=='Bolivia':

				my_filter['bolivia']=1

			if pais=='Estados Unidos':

				my_filter['estados_unidos']=1

			if pais=='Peru':

				my_filter['peru']=1

			if pais=='Colombia':

				my_filter['colombia']=1

			_archivos = Archivo.objects.filter(**my_filter).values('nombre','ruta','ramo__nombre','compania__nombre').order_by('nombre')

			a= simplejson.dumps(ValuesQuerySetToDict(_archivos))

			return HttpResponse(a, content_type="application/json")




@csrf_exempt
def asignanotificacion(request):


	os.system('/bin/sh /home/capital/devices.sh')

	archivo = open("/home/capital/data.txt", 'r') 

	i=0

	for linea in archivo.readlines():
		i=i+1
		if int(i)==22:     
			t=linea

	player = json.loads(t)['players']

	onesignal_player_ids = []

	lista_clientes_id = []

	faltantes =[]

	##Lista modelos

	for p in player:

		modelo = p['device_model']

		version_movil = p['device_os']

		cl = Agente.objects.filter(modelo=modelo,version_movil=version_movil)

		if cl.count()>0:

			print 'Guardando'

			for s in cl:

				s.codigo = p['id']
				s.save()





	# 	onesignal_player_ids.insert(1,p['id']) 

	# for _cli in Cliente.objects.all():

	# 	lista_clientes_id.insert(1,_cli.numero_notificacion)

	# for f in onesignal_player_ids:

	# 	x = f in lista_clientes_id

	# 	if x ==False:

	# 		faltantes.insert(1,f)

	# #Enviando notificaciones faltantes:

	# print 'faltantes',faltantes

	# for _f in faltantes:

	# 	print 'faltantes..',_f

	# 	header = {"Content-Type": "application/json; charset=utf-8","Authorization": "Basic OGQyNTllMmUtMmY2Ny00ZGQxLWEzNWMtMjM5NTdlNjM0ZTc3"}
	# 	payload = {"app_id": "6d06ccb5-60c3-4a76-83d5-9363fbf6b40a","include_player_ids": [_f],"contents": {"en": "Bienvenida a My Look Xpress"},"data":{'codigo': _f}}
	# 	req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
	# 	print(req.status_code, req.reason)


	c= simplejson.dumps('ok')

	return HttpResponse(c, content_type="application/json")




class Eliminacliente(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def post(self, request):

		data = json.loads(request.body)

		ParientesCliente.objects.filter(cliente_id=data['id']).delete()

		Citas.objects.filter(cliente_id=data['id']).delete()

		PropuestaCliente.objects.filter(cliente_id=data['id']).delete()

		Cliente.objects.get(id=data['id']).delete()

		a= simplejson.dumps('ok')

		return HttpResponse(a, content_type="application/json")



class Updatepropuesta(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def post(self, request):

		data = json.loads(request.body)



		pro =PropuestaCliente.objects.get(id=data['id'])

		for p in data:

			#if p =='fecha': pro.fecha = data['fecha']
			if p =='observacion': pro.observacion = data['observacion']

		pro.save()



		#Citas.objects.filter(propuesta_cliente_id=data['id']).update(prima_anual=data['prima_anual'],prima_target=data['prima_target'])

		# for d in data:

		#     if d =='fecha_cita': c.fecha_cita = data['fecha_cita']
		#     if d =='observacion': c.observacion = data['observacion']
		#     if d =='prima_target': c.prima_target = data['prima_target']
		#     if d =='prima_anual': c.prima_anual = data['prima_anual']
		#     if d =='fecha_solicitud': c.fecha_solicitud = data['fecha_solicitud']
		#     if d =='fecha_poliza': c.fecha_poliza = data['fecha_poliza']

		# c.save()


		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")



class Eliminarpropuesta(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request,id):

		Citas.objects.filter(propuesta_cliente_id=id).delete()

		PropuestaCliente.objects.get(id=id).delete()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Version(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request,version):

		id_agente=request.user.id
		ag = Agente.objects.get(user_id=id_agente)
		ag.version = version
		ag.save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Asignamovil(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request,movil):

		id=request.user.id
		a = Agente.objects.get(user_id=id)

		if movil ==0:

			
			a.tipo_movil = 'android'

		else:

			a.tipo_movil='ios'

		a.save()

		agen = Agente.objects.get(user_id=request.user.id)

		file = open('/var/www/html/devices.txt','a') 

		file.write(str(agen.id)+'-'+str(datetime.datetime.today())+str('\r\n')) 

		file.close() 


		# header = {"Content-Type": "application/json; charset=utf-8",
		# 		  "Authorization": "Basic ZTI5YjZhMWYtZTJkYS00OWJiLTkyZTAtMDRjMjIzOWNiOTBi"}

		# payload = {"app_id": "ff177554-db1d-4280-bf67-5f5a7602ba5c",
		# 		   "include_player_ids": ['d568d296-9163-46c4-a6f1-d7b0624adda1'],
		# 		   "contents": {"en": 'Un usuario ingreso al sistema '+str(agen.id)+'-'+str(agen.nombre)+'ingresar su codigo en el admin atravez de Onesignal'}}
		 
		# req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
		 
		# print req



		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Verificaversion(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request):

		id_user=request.user.id

		a = Agente.objects.get(user_id=id_user)
		version = a.version

		data ='Actualizado'

		if version:

			if int(version) ==54:
				data  ='Actualizado'
			else:
				data ='Sin actualizar'

		data = 'Actualizado'
		
		return HttpResponse(simplejson.dumps(data), content_type="application/json")


# class Enviasms(JSONWebTokenAuthMixin, View):

	
#     ## Agrega telefonos
#     def get(self, request):

#         id_user=request.user.id

		

#         audience = {numero:mensaje}

#         dato = bulksms(audience)

#         return HttpResponse(simplejson.dumps('OK'), content_type="application/json")



# def bulksms(audience):

#     url ="http://smsbulk.pe/SmsBulk/rest/ws/bulkSms"
#     username = 'xiencias'
#     password = '9nG4SB'


#     for recipient in audience:
		
#         phone_number = recipient

#         message = audience[recipient]

#         if phone_number[:2] != '51':

#             phone_number = '51%s' % phone_number

#         params = {'usr' : username,'pas' : password,'msg' : message ,'num' : phone_number}

#         reply = requests.get(url, params=params)

#         result1 = reply.text

#         return result1










class Creacitaequipo(JSONWebTokenAuthMixin, View):

	#{u'interes': u'Seguimiento', u'fecha_inicio': u'2018-01-18T05:00:00.000Z', u'apellido': u'232', u'nombre': u'32', u'user__first_name': {u'user__direccion': None, u'correo_capital': u'mhervas@capitalprts.com', u'user__username': u'mhervas', u'photo': u'static/Foto_App_I2ngkRM.PNG', u'id': 47, u'estructura__nombre': u'In House', u'user__email': u'mhervas@capitalprts.com', u'user__first_name': u'Mar\xeda Teresa', u'equipo__nombre': u'VERDE', u'telefono_1': u'', u'tipo_agente__nombre': u'Relationship Manager', u'user': 214, u'user__dni': None, u'meta_personal': 100000, u'nivel__nombre': u'GERENTE', u'meta_requerida': 125000, u'pais__nombre': u'Ecuador', u'user__last_name': u'Hervas'}}
	## Agrega telefonos
	def post(self, request):

		data = json.loads(request.body)

		id_ramo = 1

		for d in data:



			if d=='propuestajson':

				producto = data['propuestajson']['producto']['producto']
				cia = data['propuestajson']['cia']['c']
				ramo = data['propuestajson']['ramo']['id']


				

				id_ramo = RamoCompaniaProducto.objects.get(producto_id=producto,compania_id=cia,ramo_id=ramo).id

		id =request.user.id
		id_agente = Agente.objects.get(user_id=id).id

		fecha_inicio=None
		agente_equipo=None
		tipo_seguimiento=None

		for da in data:

			if da=='fecha_inicio':

				fecha_inicio = data['fecha_inicio']

			if da=='agente':

				agente_equipo = data['agente']['id']

			if da=='tipo_seguimiento':
		
				tipo_seguimiento = data['tipo_seguimiento']

		if fecha_inicio:

			fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%dT%H:%M:%S.%fZ')-timedelta(hours=5)



		propuesta_cita_equipo =''
		cliente_cita_equipo = ''
		propuesta=None
		observacion= None

		for d in data:


			if d =='cliente':

				cliente=data['cliente']['id']

			if d =='propuesta_cita_equipo':

				propuesta_cita_equipo=data['propuesta_cita_equipo']

			if d =='cliente_cita_equipo':

				cliente_cita_equipo = data['cliente_cita_equipo']

			if d =='propuesta':

				propuesta = data['propuesta']['id']

			if d =='observacion':

				observacion = data['observacion']


		sem= traesemana(fecha_inicio)

		Citas(ramo_compania_producto_id=id_ramo,agente_cita_equipo_id=agente_equipo,propuesta_cita_equipo=propuesta_cita_equipo,cliente_cita_equipo=cliente_cita_equipo,agente_equipo=agente_equipo,observacion=observacion,semana_id=sem,tipo_cita_id=4,fecha_cita=fecha_inicio,agente_id=id_agente,tipo_seguimiento_id=tipo_seguimiento).save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")



class Agenterest(JSONWebTokenAuthMixin, View):

	
	#Actualiza datos
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)
		telefono = None




		a = Agente.objects.get(user_id=id)

		for i in data:
			
			if i=='tipo_agente' :tipo_agente=data['tipo_agente']
			if i=='meta_personal' :a.meta_personal=data['meta_personal']
			if i=='meta_requerida' :

				a.meta_requerida=data['meta_requerida'].replace(',','')



			if i=='correo_capital' :a.correo_capital=data['correo_capital']
			if i=='photo' :a.photo=data['photo']
			if i=='user__direccion' :a.direccion=data['user__direccion']
			if i=='dni' :a.dni=data['dni']
			if i=='relacion_contacto':a.relacion_contacto=data['relacion_contacto']
			if i=='telefono_contacto_emergencia':a.telefono_contacto_emergencia=data['telefono_contacto_emergencia']
			if i=='contacto_emergencia':a.contacto_emergencia=data['contacto_emergencia']
			if i=='correo_personal':a.correo_personal=data['correo_personal']
			#if i=='fecha_nacimiento':a.fecha_nacimiento=data['fecha_nacimiento']
			if i=='telefono':a.telefono=data['telefono']
			if i=='telefono_1':a.telefono_1=data['telefono_1']
			if i=='direccion':a.direccion=data['direccion']
			if i=='meta_equipo':a.meta_equipo=data['meta_equipo']
			if i=='password':
				u = User.objects.get(id=id)
				u.set_password(data['password'])
				u.save()



			if i=='telefono':
				TelefonoUser(user_id=a.user.id,numero=data['telefono']).save()

	
		a.save()

		au = AuthUser.objects.get(id=id)
		au.email = a.correo_capital
		au.direccion = a.direccion
		au.dni= a.dni
		au.telefono=telefono
		au.save()

		a= simplejson.dumps('OK')
		return HttpResponse(a, content_type="application/json")

	#Retorna datos del agente
	def get(self, request):

		
		id =request.user.id

		if Agente.objects.get(user_id=request.user.id).nivel.nombre == 'PRIVATE CLIENT ADVISOR':

			a = Agente.objects.filter(user_id=id).values('meta_equipo','user','dni','photo','id','estructura__nombre','user__pais__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','photo','correo_personal','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username','direccion','contacto_emergencia','relacion_contacto','telefono_contacto_emergencia','telefono','pais__nombre','nivel__nombre')
		
		else:

			a = Agente.objects.filter(user_id=id).values('meta_equipo','user','dni','photo','id','estructura__nombre','user__pais__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','correo_personal','photo','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username','nivel__nombre','direccion','contacto_emergencia','relacion_contacto','telefono_contacto_emergencia','telefono_1','pais__nombre','nivel__nombre')
	
		fmt = '%Y-%m-%d'

		for j in range(len(a)):

			if Agente.objects.get(id=a[j]['id']).fecha_ingreso:
				a[j]['fecha_ingreso'] = Agente.objects.get(id=a[j]['id']).fecha_ingreso.strftime(fmt)
			if Agente.objects.get(id=a[j]['id']).user.nacimiento:
				a[j]['fecha_nacimiento'] = Agente.objects.get(id=a[j]['id']).user.nacimiento
			if TelefonoUser.objects.filter(user_id=a[j]['user']):
				a[j]['telefono']=TelefonoUser.objects.filter(user_id=a[j]['user']).values('numero').order_by('-id')[0]['numero']

			a[j]['meta_requerida'] = "{:,}".format(a[j]['meta_requerida'])

			if a[j]['meta_personal']:
				a[j]['meta_personal_label'] = "{:,}".format(a[j]['meta_personal'])

			if a[j]['meta_equipo']:

				a[j]['meta_equipo_label'] = "{:,}".format(a[j]['meta_equipo'])

		a= simplejson.dumps(ValuesQuerySetToDict(a))
		return HttpResponse(a, content_type="application/json")


class Eliminarcita(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request,id):


		if Citas.objects.filter(id=id).count()>0:
		
			Citas.objects.get(id=id).delete()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Guardanoti(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def post(self,request):


		data = json.loads(request.body)

		




		# agen = Agente.objects.get(user_id=request.user.id)


		# header = {"Content-Type": "application/json; charset=utf-8",
		# 		  "Authorization": "Basic ZTI5YjZhMWYtZTJkYS00OWJiLTkyZTAtMDRjMjIzOWNiOTBi"}

		# payload = {"app_id": "ff177554-db1d-4280-bf67-5f5a7602ba5c",
		# 		   "include_player_ids": ['d568d296-9163-46c4-a6f1-d7b0624adda1'],
		# 		   "contents": {"en": 'Un usuario ingreso al sistema '+str(agen.id)+'-'+str(agen.nombre)+'ingresar su codigo en el admin atravez de Onesignal'}}
		 
		# req = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
		 
		# print req

		codigo = data['codigo']

		notification = codigo['notification']

		codigo = notification['payload']['additionalData']['codigo']



		# rawPayload = notification['rawPayload']

		# custom =  rawPayload["custom"]

		# codigo = custom["a"]

		# additionalData = notification['additionalData']

		# codigo = additionalData['codigo']




		a = Agente.objects.get(user_id=request.user.id)
		a.codigo = codigo
		a.save()

		#{u'codigo': {u'action': {}, u'notification': {u'displayType': 1, u'shown': True, u'isAppInFocus': True, u'payload': {u'sound': u'default', u'body': u'2121', u'subtitle': u'212', u'title': u'2221', u'actionButtons': [], u'rawPayload': {u'aps': {u'sound': u'default', u'alert': {u'body': u'2121', u'subtitle': u'212', u'title': u'2221'}}, u'custom': {u'i': u'13ed0193-859d-44ed-ac2f-05db3f3931f0'}}, u'notificationID': u'13ed0193-859d-44ed-ac2f-05db3f3931f0'}}}}

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")



class Agentesequipo(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def get(self, request):




		tipo_agente = Agente.objects.get(user_id=request.user.id).tipo_agente.nombre

		nivel_agente = Agente.objects.get(user_id=request.user.id).nivel.nombre

		agente_id = Agente.objects.get(user_id=request.user.id).id

		pais = Agente.objects.get(user_id=request.user.id).pais



		country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(country_manager)):

			country_manager[c]['id']= country_manager[c]['agente_id']

			country_manager[c]['user__first_name']= country_manager[c]['agente__nombre']

		country_manager = ValuesQuerySetToDict(country_manager)
		
		bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')



		for c in range(len(bussiness_partner)):

			bussiness_partner[c]['id']= bussiness_partner[c]['agente_id']

			bussiness_partner[c]['user__first_name']= bussiness_partner[c]['agente__nombre']

		bussiness_partner = ValuesQuerySetToDict(bussiness_partner)

		relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_ship_director)):

			relation_ship_director[c]['id']= relation_ship_director[c]['agente_id']

			relation_ship_director[c]['user__first_name']= relation_ship_director[c]['agente__nombre']

		relation_ship_director = ValuesQuerySetToDict(relation_ship_director)

		relation_management = Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management)):

			relation_management[c]['id']= relation_management[c]['agente_id']

			relation_management[c]['user__first_name']= relation_management[c]['agente__nombre']

		relation_management = ValuesQuerySetToDict(relation_management)

		relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management_senior)):

			relation_management_senior[c]['id']= relation_management_senior[c]['agente_id']

			relation_management_senior[c]['user__first_name']= relation_management_senior[c]['agente__nombre']

		relation_management_senior = ValuesQuerySetToDict(relation_management_senior)

		private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client)):

			private_client[c]['id']= private_client[c]['agente_id']

			private_client[c]['user__first_name']= private_client[c]['agente__nombre']

		private_client = ValuesQuerySetToDict(private_client)

		private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client_senior)):

			private_client_senior[c]['id']= private_client_senior[c]['agente_id']

			private_client_senior[c]['user__first_name']= private_client_senior[c]['agente__nombre']

		private_client_senior = ValuesQuerySetToDict(private_client_senior)



		equipo_gerente = Agente.objects.get(user_id=request.user.id).equipo.id

		agen =  country_manager +bussiness_partner+relation_ship_director+relation_management+relation_management_senior+private_client+private_client_senior




		if nivel_agente=='GERENTE GENERAL':

			agen = Agente.objects.filter(equipo_id=equipo_gerente,pais__nombre=pais).values('user','photo','id','estructura__nombre','user__email','tipo_agente__nombre','meta_personal','meta_requerida','correo_capital','photo','user__first_name','user__last_name','user__dni','user__direccion','equipo__nombre','user__username','pais__nombre','telefono_1','nivel__nombre')

		r= simplejson.dumps(agen)

		return HttpResponse(r, content_type="application/json")



def sacasemana(fecha):



	s = fecha
	args = time.strptime(s, "%Y-%m-%d")[:3]
	date = datetime.date(*args)
	weeknum = date.isocalendar()[1]

	return weeknum


class Sacareportepropuestas(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def post(self, request):


		data = json.loads(request.body)



		estructura = False

		for dd in data:

			if dd=='estructura':

				estructura = data['estructura']



		inicio =data['inicio']

		fin = data['fin']

		finlabel = data['fin']

		#datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%SZ') 

		fin = fin[0:10]

		fin = datetime.datetime.strptime(fin, '%Y-%m-%d') +timedelta(days=1)

		#+timedelta(days=1)

		id = request.user.id

		ag = Agente.objects.get(user_id=id).id

		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Citascliente.csv'

		writer = csv.writer(response)

		with open('/var/www/filecliente.csv', 'wb') as result:

			writer = csv.writer(result, delimiter=";")

			writer.writerow( ('Reporte de Prospectos ',) )

			writer.writerow( ('Inicio : ',str(inicio)[0:10]) )

			writer.writerow( ('Fin : ',str(finlabel)[0:10]) )

			writer.writerow( () )

			writer.writerow( ('Agente','Prospecto','Ramo','Compania','Producto','Fecha Creacion Propuesta','Observacion','Telefono','Direccion','Correo','Cumpleanos','Edad','Estado Civil','No Hijos','Conyuge') )

			ci = Cliente.objects.filter(agente_id=ag,fecha_inicio__gte=inicio,fecha_inicio__lt=fin)

			for c in ci:

				# Recorre ramos

				email = '_'
				telefono='_'
				direccion=''
				numero_hijos='_'
				estado_civil='_'
				apellido ='_'
				edad='_'
				fecha_nacimiento = '_'
				apellido ='_'
				conyuge='_'


				nh = ParientesCliente.objects.filter(cliente_id=c.id,relacion__nombre='Hijo').count()
				numero_hijos=nh
				c.numero_hijos=nh
				c.save()



				if c.email: email = c.email
				if c.telefono: telefono = c.telefono
				if c.direccion: direccion = c.direccion
				
				if c.estado_civil : estado_civil=c.estado_civil.nombre
				if c.fecha_nacimiento : fecha_nacimiento=c.fecha_nacimiento
				if c.apellido:apellido=c.apellido
				if c.conyuge: conyuge = c.conyuge

				act_year = datetime.datetime.today().year

				if c.fecha_nacimiento:


					fecha_nacimiento = str(c.fecha_nacimiento)[0:10]

					fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')

					diff = (datetime.datetime.today() - fecha_nacimiento).days

					if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
						yeardays += 1
					else:
						yeardays = 365
						edad = str(int(diff/yeardays))

				rcp = PropuestaCliente.objects.filter(cliente=c.id)

				for _rcp in rcp:

					prima_anual ='_'
					prima_target='_'
					numero_poliza='_'
					fecha_efectiva='_'
					modalidad='_'


					yeardays = 365

					act_year = datetime.datetime.today().year



 
					__citas = Citas.objects.filter(propuesta_cliente_id=_rcp.id,tipo_seguimiento__nombre='Cierre').order_by('-id')

					if __citas.count()==0:

						writer.writerow( (c.agente,c.nombre+' '+c.apellido,_rcp.ramo_compania_producto.ramo.nombre,_rcp.ramo_compania_producto.compania.nombre,(_rcp.ramo_compania_producto.producto.nombre).encode('utf8'),str(c.fecha_inicio)[0:10],_rcp.observacion,telefono,direccion,email,str(fecha_nacimiento)[0:10],edad,estado_civil,numero_hijos,conyuge) )


			# Detalle de citas de equipo

			agente_id = Agente.objects.get(user_id=request.user.id).id

			_agentes = []

			country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(country_manager)):

				_agentes.append(country_manager[je]['agente_id'])

			bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(bussiness_partner)):

				_agentes.append(bussiness_partner[je]['agente_id'])

			relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(relation_ship_director)):

				_agentes.append(relation_ship_director[je]['agente_id'])

			relation_management= Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(relation_management)):

				_agentes.append(relation_management[je]['agente_id'])

			relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(relation_management_senior)):

				_agentes.append(relation_management_senior[je]['agente_id'])

			private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(private_client)):

				_agentes.append(private_client[je]['agente_id'])

			private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

			for je in range(len(private_client_senior)):

				_agentes.append(private_client[je]['agente_id'])


			my_filter ={}

			my_filter['id__in'] = _agentes

			age  = Agente.objects.filter(**my_filter).order_by('nombre')

			for _ag in age:


				ci = Cliente.objects.filter(agente_id=_ag.id,fecha_inicio__gte=inicio,fecha_inicio__lt=fin)

				for c in ci:

					# Recorre ramos

					email = '_'
					telefono='_'
					direccion=''
					numero_hijos='_'
					estado_civil='_'
					edad='_'

					if c.email: email = c.email
					if c.telefono: telefono = c.telefono
					if c.direccion: direccion = c.direccion
					if c.numero_hijos:numero_hijos = c.numero_hijos
					if c.estado_civil : estado_civil=c.estado_civil.nombre
					if c.fecha_nacimiento : fecha_nacimiento=c.fecha_nacimiento

					rcp = PropuestaCliente.objects.filter(cliente=c.id)

					for _rcp in rcp:

						prima_anual ='_'
						prima_target='_'
						numero_poliza='_'
						fecha_efectiva='_'
						modalidad='_'



						yeardays = 365

						act_year = datetime.datetime.today().year

						fecha_nacimiento = '_'

						conyuge ='_'

						if c.fecha_nacimiento:


							fecha_nacimiento = str(c.fecha_nacimiento)[0:10]

							fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')

							diff = (datetime.datetime.today() - fecha_nacimiento).days

							if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
								yeardays += 1
							else:
								yeardays = 365
								edad = str(int(diff/yeardays))


						if estructura == True:

							writer.writerow( (c.agente,c.nombre,_rcp.ramo_compania_producto.ramo.nombre,_rcp.ramo_compania_producto.compania.nombre,(_rcp.ramo_compania_producto.producto.nombre).encode('utf8'),str(_rcp.fecha)[0:10],_rcp.observacion,telefono,direccion,email,str(fecha_nacimiento)[0:10],edad) )




		

		return response



class Sacareportepos(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def post(self, request):


		data = json.loads(request.body)


		print 'data',data

		fecha_inicio = '-0'+str(datetime.datetime.today().month)+'-01'
		fecha_fin = '-0'+str(datetime.datetime.today().month+1)+'-01'



		for d in data:

			if d=='enero':
				
				if data['enero']==True:

					fecha_inicio='-01-01'
					fecha_fin='-02-01'


			if d=='febrero':


				if data['febrero']==True:

					fecha_inicio='-02-01'
					fecha_fin='-03-01'

			if d=='marzo':


				if data['marzo']==True:

					fecha_inicio='-03-01'
					fecha_fin='-04-01'

			if d=='abril':


				if data['abril']==True:

					fecha_inicio='-04-01'
					fecha_fin='-05-01'

			if d=='mayo':


				if data['mayo']==True:

					fecha_inicio='-05-01'
					fecha_fin='-06-01'

			if d=='junio':


				if data['junio']==True:

					fecha_inicio='-06-01'
					fecha_fin='-07-01'


		for dd in data:

			if dd=='estructura':

				estructura = data['estructura']


		id = request.user.id

		ag = Agente.objects.get(user_id=id).id

		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Citascliente.csv'

		writer = csv.writer(response)

		with open('/var/www/filecliente.csv', 'wb') as result:

			writer = csv.writer(result, delimiter=";")

			writer.writerow( ('Reporte de POS ',) )

			writer.writerow( () )

			writer.writerow( ('Asesor Inicial','Asesor Responsable','Cliente','Ramo','Compania','Producto','Poliza','Fecha Vigencia','Modalidad','Estatus'))

			

			for a in range(1990,2020):

				print a

				fecha_inicio_1=str(a)+fecha_inicio

				fecha_fin_1=str(a)+fecha_fin


				cita = Citas.objects.filter(agente_id=ag,fecha_poliza__gte=fecha_inicio_1,fecha_poliza__lte=fecha_fin_1,tipo_cita__nombre='POS',upload_csv=1)

				for ci in cita:

					asesor_responsable=ci.agente.nombre+'_'+ci.agente.apellidos

					nombre_cli='_'
					ape_cli='_'
					ramo='_'
					compania='_'
					producto='_'

					if ci.cliente:

						if ci.cliente.nombre:

							nombre_cli = ci.cliente.nombre

						if ci.cliente.apellido:

							ape_cli =ci.cliente.apellido

						cli = nombre_cli.replace(',','')

					if ci.propuesta_cliente:

						ramo = ci.propuesta_cliente.ramo_compania_producto.ramo.nombre

						compania = ci.propuesta_cliente.ramo_compania_producto.compania.nombre

						producto = ci.propuesta_cliente.ramo_compania_producto.producto.nombre

					poliza = ci.numero_poliza

					fecha_vigencia = ci.fecha_poliza

					modalidad = ci.modalidad.nombre

					estatus= ci.status_poliza.nombre

					fecha_contacto = ci.fecha_cita

					observacion = ci.observacion

					asesor_anterior = ci.asesor_anterior
				
					writer.writerow( (asesor_anterior,asesor_responsable,cli,ramo,compania,producto,poliza,str(fecha_vigencia)[0:10],modalidad,estatus) )


			for d in data:

				if d=='enero':
					
					if data['enero']==True:

						fecha_inicio='-07-01'
						fecha_fin='-08-01'


				if d=='febrero':


					if data['febrero']==True:

						fecha_inicio='-08-01'
						fecha_fin='-09-01'

				if d=='marzo':


					if data['marzo']==True:

						fecha_inicio='-09-01'
						fecha_fin='-10-01'

				if d=='abril':


					if data['abril']==True:

						fecha_inicio='-10-01'
						fecha_fin='-11-01'

				if d=='mayo':


					if data['mayo']==True:

						fecha_inicio='-11-01'
						fecha_fin='-12-01'

				if d=='junio':


					if data['junio']==True:

						fecha_inicio='-12-01'
						fecha_fin='-12-31'





			for a in range(1990,2020):

				print a

				fecha_inicio_1=str(a)+fecha_inicio

				fecha_fin_1=str(a)+fecha_fin

				cita = Citas.objects.filter(agente_id=ag,fecha_poliza__gte=fecha_inicio_1,fecha_poliza__lte=fecha_fin_1,tipo_cita__nombre='POS',upload_csv=1)

				for ci in cita:

					asesor_responsable=ci.agente.nombre+'_'+ci.agente.apellidos

					nombre_cli='_'
					ape_cli='_'
					ramo='_'
					compania='_'
					producto='_'

					if ci.cliente:

						if ci.cliente.nombre:

							nombre_cli = ci.cliente.nombre

						if ci.cliente.apellido:

							ape_cli =ci.cliente.apellido

						cli = nombre_cli.replace(',','')

					if ci.propuesta_cliente:

						ramo = ci.propuesta_cliente.ramo_compania_producto.ramo.nombre

						compania = ci.propuesta_cliente.ramo_compania_producto.compania.nombre

						producto = ci.propuesta_cliente.ramo_compania_producto.producto.nombre

					poliza = ci.numero_poliza

					fecha_vigencia = ci.fecha_poliza

					modalidad = ci.modalidad.nombre

					estatus= ci.status_poliza.nombre

					fecha_contacto = ci.fecha_cita

					observacion = ci.observacion

					asesor_anterior = ci.asesor_anterior
				
					writer.writerow( (asesor_anterior,asesor_responsable,cli,ramo,compania,producto,poliza,str(fecha_vigencia)[0:10],modalidad,estatus) )


		return response		


class Sacareporteclientereal(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def post(self, request):


		data = json.loads(request.body)

		# print data

		# estructura = False

		# for dd in data:

		# 	if dd=='estructura':

		# 		estructura = data['estructura']

		# print 'estructura',estructura

		# inicio =data['inicio']

		# fin = data['fin']

		# finlabel =data['fin']

		#datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%SZ') 

		# fin = fin[0:10]

		# fin = datetime.datetime.strptime(fin, '%Y-%m-%d') +timedelta(days=1)

		#+timedelta(days=1)

		id = request.user.id

		ag = Agente.objects.get(user_id=id).id

		nivel = Agente.objects.get(user_id=id).nivel.nombre

		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Citascliente.csv'

		writer = csv.writer(response)

		with open('/var/www/filecliente.csv', 'wb') as result:

			writer = csv.writer(result, delimiter=";")

			writer.writerow( ('Reporte de Clientes ',) )

			writer.writerow( ('Agente','Cliente','Ramo','Compania','Producto','Fecha Efectiva','Prima Anual','Prima Target','No Poliza','Modalidad','Telefono','Correo','Direccion','Estado Civil','No Hijos','Fecha Nacimiento','Edad','Nombre Conyuge','Fecha Nac. Conyuge') )

			ci = Cliente.objects.filter(agente_id=ag)

			if Agente.objects.get(user_id=id).user.username=='andy':

				ci=Cliente.objects.all()

			for c in ci:

				# Recorre ramos



				email = '_'
				telefono='_'
				direccion=''
				numero_hijos='_'
				estado_civil='_'
				apellido ='_'


				nh = ParientesCliente.objects.filter(cliente_id=c.id,relacion__nombre='Hijo').count()
				numero_hijos=nh
				c.numero_hijos=nh
				c.save()

				if c.email: email = c.email
				if c.telefono: telefono = c.telefono
				if c.direccion: direccion = c.direccion
				
				if c.estado_civil : estado_civil=c.estado_civil.nombre
				if c.fecha_nacimiento : fecha_nacimiento=c.fecha_nacimiento
				if c.apellido: apellido= c.apellido


				#Numero de Hijos



				rcp = PropuestaCliente.objects.filter(cliente=c.id)

				for _rcp in rcp:

					prima_anual ='_'
					prima_target='_'
					numero_poliza='_'
					fecha_efectiva='_'
					modalidad='_'
					edad='_'

					
					# Fecha efectiva

					__citas_efe =Citas.objects.filter(propuesta_cliente_id=_rcp.id,tipo_seguimiento__nombre='Entrega').order_by('-id')

					if __citas_efe.count()>0:

						fecha_efectiva= __citas_efe[0].fecha_poliza



					__citas = Citas.objects.filter(propuesta_cliente_id=_rcp.id,tipo_seguimiento__nombre='Cierre').order_by('-id')

					if __citas.count()>0:


						prima_anual = __citas[0].prima_anual

						prima_target = __citas[0].prima_target

						if __citas[0].numero_poliza:

							numero_poliza = __citas[0].numero_poliza

						else:

							numero_poliza = '_'

						if __citas[0].modalidad:

							modalidad = __citas[0].modalidad.nombre
					
						yeardays = 365

						act_year = datetime.datetime.today().year

						fecha_nacimiento = '_'

						conyuge ='_'

						if c.fecha_nacimiento:

							fecha_nacimiento = str(c.fecha_nacimiento)[0:10]

							fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')

							diff = (datetime.datetime.today() - fecha_nacimiento).days

							if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
								yeardays += 1
							else:
								yeardays = 365
								edad = str(int(diff/yeardays))




						if c.conyuge==None: c.conyuge='_'
						if c.fecha_nacimiento_conyuge==None: c.fecha_nacimiento_conyuge='_'
						if c.apellido==None:c.apellido='_'
						if prima_anual==None:prima_anual='_'
						if prima_target==None:prima_target=''




						writer.writerow( (c.agente,c.nombre+' '+c.apellido,_rcp.ramo_compania_producto.ramo.nombre,_rcp.ramo_compania_producto.compania.nombre,(_rcp.ramo_compania_producto.producto.nombre).encode('utf8'),str(fecha_efectiva)[0:10],prima_anual,prima_target,numero_poliza,modalidad,telefono,email,direccion,estado_civil,numero_hijos,str(fecha_nacimiento)[0:10],edad,c.conyuge,str(c.fecha_nacimiento_conyuge)[0:10]) )



			# Detalle de citas de equipo

			if nivel != 'PRIVATE CLIENT ADVISOR':

				agente_id = Agente.objects.get(user_id=request.user.id).id

				_agentes = []

				country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(country_manager)):

					_agentes.append(country_manager[je]['agente_id'])

				bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(bussiness_partner)):

					_agentes.append(bussiness_partner[je]['agente_id'])

				relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(relation_ship_director)):

					_agentes.append(relation_ship_director[je]['agente_id'])

				relation_management= Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(relation_management)):

					_agentes.append(relation_management[je]['agente_id'])

				relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(relation_management_senior)):

					_agentes.append(relation_management_senior[je]['agente_id'])

				private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(private_client)):

					_agentes.append(private_client[je]['agente_id'])

				private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for je in range(len(private_client_senior)):

					_agentes.append(private_client[je]['agente_id'])


				my_filter ={}

				my_filter['id__in'] = _agentes

				age  = Agente.objects.filter(**my_filter).order_by('nombre')

				for _ag in age:

					ci = Cliente.objects.filter(agente_id=_ag.id)

					for c in ci:

						# Recorre ramos

						email = '_'
						telefono='_'
						direccion=''
						numero_hijos='_'
						estado_civil='_'
						edad='_'
						conyuge ='_'

						if c.email: email = c.email
						if c.telefono: telefono = c.telefono
						if c.direccion: direccion = c.direccion.encode('utf8')
						if c.numero_hijos:numero_hijos = c.numero_hijos
						if c.estado_civil : estado_civil=c.estado_civil.nombre
						if c.fecha_nacimiento : fecha_nacimiento=c.fecha_nacimiento
						if c.conyuge :conyuge=c.conyuge.encode('utf8')

						rcp = PropuestaCliente.objects.filter(cliente=c.id)

						for _rcp in rcp:

							prima_anual ='_'
							prima_target='_'
							numero_poliza='_'
							fecha_efectiva='_'
							modalidad='_'

							# Fecha efectiva

							__citas_efe =Citas.objects.filter(propuesta_cliente_id=_rcp.id,tipo_seguimiento__nombre='Entrega').order_by('-id')

							# if __citas_efe.count()>0:

							# 	fecha_efectiva= __citas_efe[0].fecha_efectiva

							__citas = Citas.objects.filter(propuesta_cliente_id=_rcp.id,tipo_seguimiento__nombre='Cierre').order_by('-id')

							if __citas.count()>0:

								
								prima_anual = __citas[0].prima_anual

								prima_target = __citas[0].prima_target

								if __citas[0].numero_poliza:

									numero_poliza = __citas[0].numero_poliza

								else:

									numero_poliza = '_'

								if __citas[0].modalidad:

									modalidad = __citas[0].modalidad.nombre

								else:

									modalidad ='_'

							
								yeardays = 365

								act_year = datetime.datetime.today().year

								fecha_nacimiento = '_'

							
								if c.fecha_nacimiento:


									fecha_nacimiento = str(c.fecha_nacimiento)[0:10]

									fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')

									diff = (datetime.datetime.today() - fecha_nacimiento).days

									if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
										yeardays += 1
									else:
										yeardays = 365
										edad = str(int(diff/yeardays))

								writer.writerow( (c.agente,(c.nombre).encode('utf8'),(_rcp.ramo_compania_producto.ramo.nombre).encode('utf8'),(_rcp.ramo_compania_producto.compania.nombre).encode('utf8'),(_rcp.ramo_compania_producto.producto.nombre).encode('utf8'),str(fecha_efectiva)[0:10],prima_anual,prima_target,numero_poliza,modalidad,telefono,email,direccion,estado_civil,numero_hijos,str(fecha_nacimiento)[0:10],edad,conyuge,c.fecha_nacimiento_conyuge) )


		return response


class Sacareportecitas(JSONWebTokenAuthMixin, View):

	
	## Agrega telefonos
	def post(self, request):


		data = json.loads(request.body)

		inicio =data['inicio']

		fin = data['fin']

		finlabel = data['fin']

		#datetime.strptime(date_posted, '%Y-%m-%dT%H:%M:%SZ') 

		fin = fin[0:10]

		fin = datetime.datetime.strptime(fin, '%Y-%m-%d') +timedelta(days=1)

		#+timedelta(days=1)

		id = request.user.id

		ag = Agente.objects.get(user_id=id).id

		nivel = Agente.objects.get(user_id=id).nivel.nombre

		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Citascliente.csv'

		writer = csv.writer(response, encoding='utf-8')

		with open('/var/www/filecliente.csv', 'wb') as result:

			writer = csv.writer(result, delimiter=";")

			writer.writerow( ('Reporte de Citas ',) )

			writer.writerow( ('Fecha Generada : ',str(datetime.datetime.now())[0:10]) )

			writer.writerow( ('Nombre : ', Agente.objects.get(user_id=id).nombre ))

			writer.writerow( ('Tipo Agente : ', Agente.objects.get(user_id=id).tipo_agente ))

			writer.writerow( ('Inicio : ',str(inicio)[0:10]) )

			writer.writerow( ('Fin : ',str(finlabel)[0:10]) )

			writer.writerow( () )

			writer.writerow( ('Detalle de Citas Personales',) )

			writer.writerow( ('Semana','Fecha','Cliente','Tipo de Cita','Interes','Ramo','Compania','Producto','Tel. Movil','Direccion','Observaciones') )

			ci = Citas.objects.filter(agente_id=ag,fecha_cita__gte=inicio,fecha_cita__lt=fin,cliente_antiguo='No').values('id','semana__numero','fecha_cita','cliente_id','cliente__nombre','cliente__apellido','tipo_cita__nombre','propuesta_cliente__ramo_compania_producto__ramo__nombre','propuesta_cliente__ramo_compania_producto__compania__nombre','propuesta_cliente__ramo_compania_producto__producto__nombre','cliente__telefono','cliente__direccion','propuesta_cliente__observacion','tipo_seguimiento__nombre','propuesta_cliente__interes','observacion').exclude(tipo_cita__nombre='Cita de Equipo').order_by('fecha_cita')

		
			#ci_e = Citas.objects.filter(agente_cita_equipo_id=ag,fecha_cita__gte=inicio,fecha_cita__lte=fin,cliente_antiguo='No').values('id','semana__numero','fecha_cita','cliente__nombre','cliente__apellido','tipo_cita__nombre','propuesta_cliente__interes','propuesta_cliente__ramo_compania_producto__ramo__nombre','propuesta_cliente__ramo_compania_producto__compania__nombre','propuesta_cliente__ramo_compania_producto__producto__nombre','cliente__telefono','cliente__direccion','propuesta_cliente__observacion','tipo_seguimiento__nombre').order_by('semana__numero').order_by('semana__numero','fecha_cita')

			todos = ValuesQuerySetToDict(ci)

			for i in range(len(todos)):

				interes ="_"

				detalleseg=" "

				if todos[i]['tipo_cita__nombre']=='Nuevo Prospecto de Cliente' and todos[i]['tipo_seguimiento__nombre']=='Seguimiento':

					detalleseg = 'Nueva Propuesta'

				if todos[i]['tipo_seguimiento__nombre']=='Nuevo':

					todos[i]['tipo_seguimiento__nombre']='NP'

					interes = todos[i]['propuesta_cliente__interes']

					todos[i]['propuesta_cliente__observacion'] = todos[i]['propuesta_cliente__observacion'].encode('ascii','ignore').encode('ascii','replace')

				else:

					if todos[i]['observacion']:

						todos[i]['propuesta_cliente__observacion'] = todos[i]['observacion'].encode('ascii','ignore').encode('ascii','replace')

					else:

						todos[i]['propuesta_cliente__observacion'] = None

				if todos[i]['tipo_seguimiento__nombre']=='Seguimiento':

					todos[i]['tipo_seguimiento__nombre']='Seg'

				if todos[i]['semana__numero']:

					todos[i]['semana__numero'] = todos[i]['semana__numero'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['semana__numero']= None
				
				todos[i]['cliente__nombre'] = todos[i]['cliente__nombre'].encode('ascii','ignore').encode('ascii','replace')

				if todos[i]['cliente__apellido']:

					todos[i]['cliente__apellido'] = todos[i]['cliente__apellido'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['cliente__apellido'] ='_'

				todos[i]['tipo_cita__nombre'] = todos[i]['tipo_seguimiento__nombre'].encode('ascii','ignore').encode('ascii','replace')


				if todos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre']:

					todos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre'] = todos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre']= None

				if todos[i]['propuesta_cliente__ramo_compania_producto__compania__nombre']:

					todos[i]['propuesta_cliente__ramo_compania_producto__compania__nombre'] = todos[i]['propuesta_cliente__ramo_compania_producto__compania__nombre'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['propuesta_cliente__ramo_compania_producto__compania__nombre']= None

				if todos[i]['propuesta_cliente__ramo_compania_producto__producto__nombre']:

					todos[i]['propuesta_cliente__ramo_compania_producto__producto__nombre'] = todos[i]['propuesta_cliente__ramo_compania_producto__producto__nombre'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['propuesta_cliente__ramo_compania_producto__producto__nombre']=None

				if todos[i]['cliente__telefono']:

					todos[i]['cliente__telefono'] = todos[i]['cliente__telefono'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['cliente__telefono']= None
				

				if todos[i]['cliente__direccion']:

					todos[i]['cliente__direccion'] = todos[i]['cliente__direccion'].encode('ascii','ignore').encode('ascii','replace')

				else:

					todos[i]['cliente__direccion']= None

			
				writer.writerow( (todos[i]['semana__numero'],str(todos[i]['fecha_cita'])[0:11],todos[i]['cliente__nombre']+' '+todos[i]['cliente__apellido'],todos[i]['tipo_cita__nombre']+' '+detalleseg,interes,todos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre'],todos[i]['propuesta_cliente__ramo_compania_producto__compania__nombre'],todos[i]['propuesta_cliente__ramo_compania_producto__producto__nombre'],"'"+str(todos[i]['cliente__telefono']),todos[i]['cliente__direccion'],todos[i]['propuesta_cliente__observacion']) )

			
			if nivel != 'PRIVATE CLIENT ADVISOR':

				ci_e = Citas.objects.filter(agente_id=ag,fecha_cita__gte=inicio,fecha_cita__lt=fin,tipo_cita__nombre='Cita de Equipo').values('agente_cita_equipo__nombre','agente_cita_equipo__apellidos','semana__numero','fecha_cita','cliente_cita_equipo','tipo_cita__nombre','propuesta_cliente__interes','ramo_compania_producto__ramo__nombre','ramo_compania_producto__compania__nombre','ramo_compania_producto__producto__nombre','cliente__telefono','cliente__direccion','propuesta_cliente__observacion','tipo_seguimiento__nombre','observacion').order_by('semana__numero').order_by('fecha_cita')

				writer.writerow( () )
					
				writer.writerow( ('Detalle de Citas de Acompanamiento',) )

				writer.writerow( ('Semana','Fecha','Agente','Cliente','Tipo de Cita','Ramo','Compania','Producto','Observaciones') )


				todos = ValuesQuerySetToDict(ci_e) 

				for i in range(len(todos)):




					if todos[i]['tipo_seguimiento__nombre']=='Nuevo':

						todos[i]['tipo_seguimiento__nombre']='NP'

					if todos[i]['tipo_seguimiento__nombre']=='Seguimiento':

						todos[i]['tipo_seguimiento__nombre']='Seg'


					if todos[i]['semana__numero']:

						todos[i]['semana__numero'] = todos[i]['semana__numero'].encode('ascii','ignore').encode('ascii','replace')
					else:

						todos[i]['semana__numero']= None
					
					if todos[i]['cliente_cita_equipo']:

						todos[i]['cliente_cita_equipo'] = todos[i]['cliente_cita_equipo'].encode('ascii','ignore').encode('ascii','replace')

					else:

						todos[i]['cliente_cita_equipo']  = None

					todos[i]['agente_cita_equipo__nombre'] = todos[i]['agente_cita_equipo__nombre'].encode('ascii','ignore').encode('ascii','replace')




					writer.writerow( (todos[i]['semana__numero'],str(todos[i]['fecha_cita'])[0:11],todos[i]['agente_cita_equipo__nombre']+' '+todos[i]['agente_cita_equipo__apellidos'],todos[i]['cliente_cita_equipo'],todos[i]['tipo_seguimiento__nombre'],todos[i]['ramo_compania_producto__ramo__nombre'],todos[i]['ramo_compania_producto__compania__nombre'],todos[i]['ramo_compania_producto__producto__nombre'],todos[i]['observacion']) )


				writer.writerow( ())

				writer.writerow( ('Detalle de Citas de Equipo',))



				writer.writerow( ('Semana','Fecha','Agente','Cliente','Tipo de Cita','Interes','Ramo','Compania','Producto','Telefono','Direccion','Observacion'))

				# Detalle de citas de equipo

				agente_id = Agente.objects.get(user_id=request.user.id).id

				_agentes = []

				country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(country_manager)):

					_agentes.append(country_manager[c]['agente_id'])

				bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(bussiness_partner)):

					_agentes.append(bussiness_partner[c]['agente_id'])

				relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(relation_ship_director)):

					_agentes.append(relation_ship_director[c]['agente_id'])

				relation_management= Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(relation_management)):

					_agentes.append(relation_management[c]['agente_id'])

				relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(relation_management_senior)):

					_agentes.append(relation_management_senior[c]['agente_id'])

				private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(private_client)):

					_agentes.append(private_client[c]['agente_id'])

				private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

				for c in range(len(private_client_senior)):

					_agentes.append(private_client[c]['agente_id'])


				my_filter ={}

				my_filter['id__in'] = _agentes

				sunivel = Agente.objects.get(user_id=request.user.id).nivel.nombre

				c  = Agente.objects.filter(**my_filter).values('id','nombre','apellidos','equipo','pais__nombre').order_by('nombre')

				for i in range(len(c)):

					c[i]['nombre'] = c[i]['nombre'].encode('ascii','ignore')

					c[i]['nombre'] = c[i]['nombre'].encode('ascii','replace')

					c[i]['apellidos'] = c[i]['apellidos'].encode('ascii','ignore')

					c[i]['apellidos'] = c[i]['apellidos'].encode('ascii','replace')

					# Sacando jerarquia

					if Agentejerarquia.objects.filter(agente_id=c[i]['id']).count()==1:

						age = Agentejerarquia.objects.get(agente_id=c[i]['id'])

						bp = age.bussiness_partner.nombre + ' '+age.bussiness_partner.apellidos

						bp = bp.encode('ascii','ignore')

						bp = bp.encode('ascii','replace')

						rd = age.relation_ship_director.nombre+ ' '+age.relation_ship_director.apellidos

						rd = rd.encode('ascii','ignore')

						rd = rd.encode('ascii','replace')

						rm = age.relation_management.nombre+' '+age.relation_management.apellidos

						rm = rm.encode('ascii','ignore')

						rm = rm.encode('ascii','replace')

						if rm=='Sin Asignar': rm='NA'
						if rd=='Sin Asignar': rd='NA'
						if bp=='Sin Asignar': bp='NA'


						# Saca reporte gerente

						#writer.writerow( ('Semana','Fecha','Agente','Cliente','Tipo de Cita','Interes','Ramo','Compania','Producto','Telefono','Direccion','Observacion'))


						x = Citas.objects.filter(fecha_cita__lt=fin,fecha_cita__gte=inicio,agente_id=c[i]['id']).exclude(cliente_antiguo='Yes').exclude(tipo_cita__nombre='Cita de equipo').exclude(agente_id=agente_id).order_by('fecha_cita')

						for __cli in x:

							

							telefono = '_'
							direccion = '_'
							nombre = ' '
							apellido = '_'
							nombrecliente='_'
							interes = '_'
							observacion='_'
							agentenombre='_'
							agenteapellido='_'
							detalleseg='_'

							if __cli.cliente.telefono: telefono=__cli.cliente.telefono
							if __cli.cliente.direccion: direccion=__cli.cliente.direccion
							if __cli.cliente.nombre : 

								
								nombre=__cli.cliente.nombre

							
							if __cli.cliente.apellido : apellido=__cli.cliente.apellido
							if __cli.agente.nombre : agentenombre = __cli.agente.nombre
							if __cli.agente.apellidos : agenteapellido = __cli.agente.apellidos


							nombrecliente = nombre+' '+apellido
							agentenombretotal = agentenombre+' '+agenteapellido

							tipo_cita = __cli.tipo_seguimiento.nombre

							if __cli.tipo_seguimiento.nombre=='Nuevo':tipo_cita='NP'
							if __cli.tipo_seguimiento.nombre=='Seguimiento':tipo_cita='Seg'

							if __cli.tipo_seguimiento.nombre=='Seguimiento' and __cli.tipo_cita.nombre=='Nuevo Prospecto de Cliente':

								detalleseg = 'Nuevo Propuesta'


							if __cli.propuesta_cliente.interes and __cli.tipo_seguimiento.nombre=='Nuevo': 

								interes = __cli.propuesta_cliente.interes


							ramo = __cli.propuesta_cliente.ramo_compania_producto.ramo.nombre
							cia = __cli.propuesta_cliente.ramo_compania_producto.compania.nombre
							producto = __cli.propuesta_cliente.ramo_compania_producto.producto.nombre
							
							if __cli.observacion:
								observacion = __cli.observacion

							
							

							writer.writerow( (__cli.semana.numero,str(__cli.fecha_cita)[0:11],agentenombretotal,nombrecliente,tipo_cita+' '+detalleseg,interes,ramo,cia,producto,telefono,direccion,observacion))








		return response

class Sacareportegerente(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def post(self, request):


		#Sacando reporte...

		 

		agente_id = Agente.objects.get(user_id=request.user.id).id
 

		_agentes = []

		country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(country_manager)):

			_agentes.append(country_manager[c]['agente_id'])

		bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(bussiness_partner)):

			_agentes.append(bussiness_partner[c]['agente_id'])

		relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_ship_director)):

			_agentes.append(relation_ship_director[c]['agente_id'])

		relation_management= Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management)):

			_agentes.append(relation_management[c]['agente_id'])

		relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management_senior)):

			_agentes.append(relation_management_senior[c]['agente_id'])

		private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client)):

			_agentes.append(private_client[c]['agente_id'])

		private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client_senior)):

			_agentes.append(private_client[c]['agente_id'])

		########

		data = json.loads(request.body)

		# {u'fin': u'2018-03-18T05:00:00.000Z', u'inicio': u'2018-03-01T05:00:00.000Z'}

		# grupo = User.objects.get(pk=request.user.id).groups.get()

		equipo = Agente.objects.get(user_id=request.user.id).equipo.nombre

		my_filter={}

		# if str(grupo)!='ADMIN':

		#     my_filter['equipo__nombre'] = equipo


		# print 'grupo',grupo

		# fecha_cita__gte = '1/1/1000'

		# fecha_cita__lte = '1/12/4000'

		# fecha_cita__gte=datetime.strptime(str(fecha_cita__gte), '%d/%m/%Y')

		# fecha_cita__lte=datetime.strptime(str(fecha_cita__lte), '%d/%m/%Y')

		for r in json.loads(request.body):

			if r=='agente__nombre':

				agente = data['agente__nombre']

				my_filter['nombre'] = agente

			if r=='inicio':

				fecha_cita__gte = data['inicio']


				


				#fecha_cita__gte=datetime.strptime(str(fecha_cita__gte), '%d/%m/%Y')

			if r=='fin':

				fecha_cita__lte = data['fin']

				fecha_cita__lte = data['fin'][0:10]

				fecha_cita__lte_label = data['fin'][0:10]

				fecha_cita__lte = datetime.datetime.strptime(fecha_cita__lte,'%Y-%m-%d') +timedelta(days=1)

		# semanainicio= sacasemana(str(fecha_cita__gte)[0:10])

		# semanafinal= sacasemana(str(fecha_cita__lte)[0:10])

		# numerosemanas = semanafinal - semanainicio + 1

		# totalnumerosemanas = 5*numerosemanas

		#### totalcitasesperado = 260


		# nsem = sacasemana(str(datetime.datetime.today())[0:10])

		# citaesperadoafecha = nsem*5

		# porcentajeesperado = citaesperadoafecha*100/totalcitasesperado

		# porcentareal = float(ncitasreal*100)/float(totalcitasesperado)

		######

		my_filter['id__in'] = _agentes

		sunivel = Agente.objects.get(user_id=request.user.id).nivel.nombre

		supais = Agente.objects.get(user_id=request.user.id).pais.nombre

		c  = Agente.objects.filter(**my_filter).values('id','nombre','apellidos','equipo','pais__nombre').order_by('nombre')

		if sunivel=='GERENTE GENERAL':

			c  = Agente.objects.filter(pais__nombre=supais).values('id','nombre','apellidos','equipo','pais__nombre').order_by('nombre')
 
		response = HttpResponse(content_type='text/csv')

		response['Content-Disposition'] = 'attachment; filename="Citas.csv'

		writer = csv.writer(response)

		#writer.writerow(['Agente','# Nuevos Prospectos','# Citas Equipo ','# Seguimiento','# POS';'# Cierre','#Entrega'])

		_nombres = []
		_nuevos = []
		_seguimiento = []
		_pos =[]
		_cierre =[]
		_entrega = []
		_citaequipo = []
		_vida=[]
		_salud=[]
		_investiments=[]
		_ramosgenerales=[]
		_bp = []
		_rd = []
		_rm = []
		_pais = []
		_efectividad=[]
		_citas_esperadas = []
		_porcentareal = []
		_produccion=[]
		_produccion_inforce=[]
		_totalcierres=[]

		with open('/var/www/file.csv', 'wb') as result:

			writer = csv.writer(result, delimiter=";")



   
			writer.writerow((''))

			writer.writerow(('Reporte de Resultados de Equipo',))

			writer.writerow(('Fecha Inicio:',str(fecha_cita__gte)[0:10]))

			writer.writerow(('Fecha Fin:',str(fecha_cita__lte_label)[0:10]))

			#writer.writerow(('# Semanas:',numerosemanas))

			writer.writerow((''))

			writer.writerow( ('','','','','','CITAS','','','PROPUESTAS','','','','','','CIERRES','','','','','PRODUCCION SOMETIDA US$','','','','','TOTAL PRODUCCION INFORCE US$') )

			writer.writerow( ('Agente','Pais','BP','RD','RM','Nuevos Prospectos','Seguimiento','Cierre','Entrega','POS','Total Propuestas','Vida','Salud','Inversiones','Ramos Generales','CFP','Total Cierres','Vida','Salud','Inversiones','Ramos Generales','Total Produccion Sometida','Vida','Salud','Investments','Ramos Generales','Total Produccion Inforce','Vida','Salud','Investiments','Ramos Generales','%Efectividad','%Termometro Nuevos Prospectos','Entrega' ) )

			#writer.writerow( ('_nombres', 'pais','bp','rd','rm','nuevos','seguimiento','pos','nuevos','vida','salud','investiments','totalcierres','vidacerrados','saludcerrados','inversioncerrados','produccion','produccion_inforce','vidainforce','saludinforce','inversioninforce','efectividad','porcentareal','entrega') )

		   
			for i in range(len(c)):

				c[i]['nombre'] = c[i]['nombre'].encode('ascii','ignore')

				c[i]['nombre'] = c[i]['nombre'].encode('ascii','replace')

				c[i]['apellidos'] = c[i]['apellidos'].encode('ascii','ignore')

				c[i]['apellidos'] = c[i]['apellidos'].encode('ascii','replace')



				if Agentejerarquia.objects.filter(agente_id=c[i]['id']).count()==1:

					age = Agentejerarquia.objects.get(agente_id=c[i]['id'])

					bp = age.bussiness_partner.nombre + ' '+age.bussiness_partner.apellidos

					bp = bp.encode('ascii','ignore')

					bp = bp.encode('ascii','replace')

					rd = age.relation_ship_director.nombre+ ' '+age.relation_ship_director.apellidos

					rd = rd.encode('ascii','ignore')

					rd = rd.encode('ascii','replace')

					rm = age.relation_management.nombre+' '+age.relation_management.apellidos

					rm = rm.encode('ascii','ignore')

					rm = rm.encode('ascii','replace')

					if rm=='Sin Asignar': rm='NA'
					if rd=='Sin Asignar': rd='NA'
					if bp=='Sin Asignar': bp='NA'

					# if !rd: rd = age.relation_ship_senior.director.nombre+ ' '+age.relation_ship_director_senior.apellido

					# if !rm: rm = age.relation_management_senior.director.nombre+ ' '+age.relation_management_senior.apellido

					_bp.append(bp)

					_rm.append(rm)

					_rd.append(rd)

					# Pais

					pais = c[i]['pais__nombre']

					pais = pais.encode('ascii','ignore')

					pais = pais.encode('ascii','replace')

					# Saca reporte gerente

					x = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes')

					totalcierres = x.count()


					totalcitas = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Nuevo').exclude(cliente_antiguo='Yes').count()

					if totalcitas==0:

						efectividad = 0

					else:

						efectividad = totalcierres*100/totalcitas


					_pais.append(pais)

					# Reporte 

					cli = Cliente.objects.filter(agente_id=c[i]['id'])

					con=0

					for o in cli:

						if Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,cliente_id=o.id,tipo_cita__nombre='Nuevo Prospecto de Cliente').exclude(cliente_antiguo='Yes').count()>0:

							con = con+1

					ncitasreal = con

					totalcitasesperado = 260

					porcentareal = int(float(ncitasreal*100)/float(totalcitasesperado))

					_nombres = c[i]['nombre']+' ' +c[i]['apellidos']
					
					#Produccion mensual

					produccion = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes').exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					#produccion_inforce = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',inforce=1).aggregate(produccion_inforce=Sum('prima_target'))['produccion_inforce']
					
					nuevos = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente',cliente_antiguo='No').values('cliente_id').annotate(total=Count('cliente_id')).count()
					
					#nuevos = Citas.objects.filter(agente_id=c.id,tipo_cita__nombre='Nuevo Prospecto de Cliente',cliente_antiguo='No').values('cliente_id').order_by('cliente_id').annotate(total=Count('cliente_id')).count()

					seguimiento = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Seguimiento',cliente_antiguo='No').exclude(tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

					pos = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='POS').exclude(cliente_antiguo='Yes').count()

					cierre = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes').count()

					entrega = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Entrega').exclude(cliente_antiguo='Yes').count()

					
					#vida = PropuestaCliente.objects.filter(fecha__lte=fecha_cita__lte,fecha__gte=fecha_cita__gte,agente_id=c[i]['id'],ramo_compania_producto__ramo__nombre='Vida').exclude(cliente__fecha_inicio=None).count()

					vida = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente',propuesta_cliente__ramo_compania_producto__ramo__nombre='Vida',cliente_antiguo='No').count()
					
					salud = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente',propuesta_cliente__ramo_compania_producto__ramo__nombre='Salud',cliente_antiguo='No').count()
					
					#salud = PropuestaCliente.objects.filter(fecha__lte=fecha_cita__lte,fecha__gte=fecha_cita__gte,agente_id=c[i]['id'],ramo_compania_producto__ramo__nombre='Salud').exclude(cliente__fecha_inicio=None).count()

					#investiments = PropuestaCliente.objects.filter(fecha__lte=fecha_cita__lte,fecha__gte=fecha_cita__gte,agente_id=c[i]['id'],ramo_compania_producto__ramo__nombre='Investments').exclude(cliente__fecha_inicio=None).count()

					investiments = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente',propuesta_cliente__ramo_compania_producto__ramo__nombre='Investments',cliente_antiguo='No').count()
					
					#ramosgeneralespropuestas = PropuestaCliente.objects.filter(fecha__lte=fecha_cita__lte,fecha__gte=fecha_cita__gte,agente_id=c[i]['id'],ramo_compania_producto__ramo__nombre='Ramos Generales').exclude(cliente__fecha_inicio=None).count()

					ramosgeneralespropuestas = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente',propuesta_cliente__ramo_compania_producto__ramo__nombre='Ramos Generales',cliente_antiguo='No').count()
					
					cfp = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente',propuesta_cliente__ramo_compania_producto__ramo__nombre='CFP',cliente_antiguo='No').count()
					
					
					#cfp = PropuestaCliente.objects.filter(fecha__lte=fecha_cita__lte,fecha__gte=fecha_cita__gte,agente_id=c[i]['id'],ramo_compania_producto__ramo__nombre='CFP').exclude(cliente__fecha_inicio=None).count()

					totalpropuestas =vida+salud+investiments+ramosgeneralespropuestas+cfp

					ramosgenerales = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],propuesta_cliente__ramo_compania_producto__ramo__nombre='Ramos Generales').exclude(cliente_antiguo='Yes').count()

					vidacerrados =  Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Vida').exclude(cliente_antiguo='Yes').count()

					saludcerrados = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Salud').exclude(cliente_antiguo='Yes').count()

					inversioncerrados = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Investiments').exclude(cliente_antiguo='Yes').count()
		   
		   			ramosgeneralescerrados = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Ramos Generales').exclude(cliente_antiguo='Yes').count()
		   
		   			cfpcerrados = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='CFP').exclude(cliente_antiguo='Yes').count()
		   
					totalcierres = vidacerrados + saludcerrados + inversioncerrados +ramosgeneralescerrados +cfpcerrados

					# Cierres Monto

					vidamonto =  Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Vida').exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					saludmonto = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Salud').exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					inversionmonto = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Investiments').exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					ramosgeneralesmonto = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Investiments').exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					
					if vidamonto == None: vidamonto=0
					if saludmonto == None: saludmonto=0
					if inversionmonto == None:  inversionmonto =0
					if ramosgeneralesmonto == None: ramosgeneralesmonto = 0

					# Inforce Primas
					
					vidainforce =  Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Vida',inforce=1).exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					saludinforce = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Salud',inforce=1).exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					inversioninforce = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Investiments',inforce=1).exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					ramosgeneralesinforce = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre='Ramos Generales',inforce=1).exclude(cliente_antiguo='Yes').aggregate(produccion=Sum('prima_target'))['produccion']

					

					if vidainforce == None: vidainforce=0
					if saludinforce == None: saludinforce=0
					if inversioninforce == None: inversioninforce=0
					if ramosgeneralesinforce == None: ramosgeneralesinforce=0
					

					produccion_inforce = vidainforce+saludinforce+inversioninforce+ramosgeneralesinforce


					#writer.writerow( ('Agente','Pais','BP','RD','RM','Nuevos Prospectos','Seguimiento','POS','Total Propuestas','Vida','Salud','Inversiones','Total Cierres','Vida','Salud','Inversiones','Total Produccion Sometida','Total Produccion Inforce','Vida','Salud','Investiments','Efectividad','%Termometro Nuevos Prospectos','Entrega' ) )

					# if totalpropuestas ==0:

					# 	efectividad=0

					# else:

					# 	efectividad = totalcierres*100/float(totalpropuestas)

					# 	efectividad = float("{0:.2f}".format(efectividad))

					if nuevos==0:

						efectividad=0

					else:

						efectividad = totalcierres*100/nuevos

					nsem = sacasemana(str(datetime.datetime.today())[0:10])

					citaesperadoafecha = nsem*5


					porcentareal = float(nuevos*100)/float(citaesperadoafecha)

					porcentareal = float("{0:.2f}".format(porcentareal))




					writer.writerow( (_nombres, pais,bp,rd,rm,nuevos,seguimiento,cierre,entrega,pos,totalpropuestas,vida,salud,investiments,ramosgeneralespropuestas,cfp,totalcierres,vidacerrados,saludcerrados,inversioncerrados,ramosgeneralescerrados,produccion,vidamonto,saludmonto,inversionmonto,ramosgeneralesmonto,produccion_inforce,vidainforce,saludinforce,inversioninforce,ramosgeneralesinforce,efectividad,porcentareal,entrega) )


		#df = pandas.DataFrame(data={"0 Agente": _nombres,"1 Pais":_pais,"2 BP":_bp,"2.1 RD":_rd,"2.2 RM":_rm,"3 #Total Casos Cerados ":_totalcierres,"3.1 # Nuevos Prospectos":_nuevos,"3.2 # Seguimiento":_seguimiento,"3.3 POS":_pos,"3.4 Total Propuestas":_nuevos,"8.1 Total Produccion Sometida":_produccion,"8.2 Total Produccion Inforce":_produccion_inforce,"9.1 Vida":_vida,"9.2 Salud":_salud,"9.3 Inversiones":_investiments,"9.4 Efectividad":_efectividad,"9.5 %Termometro Nuevos Prospectos":_porcentareal,"9.6 Entrega":_entrega})
	
		#df.to_csv("/var/www/file.csv", sep=';',index=True)


			#writer.writerow([c[i]['nombre'] +' '+c[i]['apellidos'] ,nuevos,citaequipo,seguimiento,pos,cierre,entrega])

		



		return response





class Userfono(JSONWebTokenAuthMixin, View):

	## Agrega telefonos
	def post(self, request):

		data = json.loads(request.body)
		telefono=data['id']
		numero=data['numero']
		TelefonoUser(user_id=id,numero=numero).save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

	## Lista los telefonos
	def get(self,request):

		t=TelefonoUser.objects.filter('numero').values('numero')
		t= simplejson.dumps(ValuesQuerySetToDict(t))
	
		return HttpResponse(t, content_type="application/json")

	## Elimina telefono
	def delete(self,request):

		TelefonoUser.objects.get(id=telefono).delete()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

	#Actualiza telefono
	def put(self,request):

		t=TelefonoUser.objects.get(id=telefono)
		t.numero= numero
		t.save()

		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")


class CreaPariente(JSONWebTokenAuthMixin, View):

	#Crea nuevo cliente
	def post(self, request):

		data = json.loads(request.body)



		#Calculando edad

		yeardays = 365

		act_year = datetime.datetime.today().year

		fecha_nacimiento = str(data['fecha_nacimiento'])[0:10]

		data['fecha_nacimiento'] = datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')

		diff = (datetime.datetime.today() - data['fecha_nacimiento']).days
		if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
			yeardays += 1
		else:
			yeardays = 365
			years = str(int(diff/yeardays))
		

		#fin de edad

		if int(data['relacion']) == 1:

			cliente = Cliente.objects.get(id=data['cliente'])
			cliente.conyuge=data['nombre']
			cliente.fecha_nacimiento_conyuge = data['fecha_nacimiento']
			cliente.edad_conyuge=years
			

			cliente.save()

		ParientesCliente(edad=years,nombre=data['nombre'],fecha_nacimiento=data['fecha_nacimiento'],cliente_id=data['cliente'],relacion_id=data['relacion']).save()


		return HttpResponse(simplejson.dumps('cliente_id'), content_type="application/json")





class Creacliente(JSONWebTokenAuthMixin, View):

	#Crea nuevo cliente
	def post(self, request):

		id =request.user.id

		id_agente = Agente.objects.get(user_id=id).id

		#id_equipo = Agente.objects.get(id=request.user.id).equipo.id

		data = json.loads(request.body)

		for i in data:

			print i

		fecha_inicio= None
		estado_civil= None
		numero_hijos= None
		first_name= None
		last_name= None
		email= None
		pais= None
		nacimiento= None
		dni= None
		direccion= None
		id_cliente= None
		telefono=None
		for i in data:

			print i

			if i=='fecha_inicio' : fecha_inicio = data['fecha_inicio']
			if i=='estado_civil' : estado_civil = data['estado_civil']
			if i=='numero_hijos' : numero_hijos = data['numero_hijos']
			if i=='first_name' : first_name = data['first_name']
			if i=='last_name' : last_name = data['last_name']
			if i=='email' : email = data['email']
			if i=='pais' : pais = data['pais']
			if i=='nacimiento' : nacimiento = data['nacimiento']
			if i=='dni' : dni = data['dni']
			if i=='direccion' : direccion = data['direccion']
			if i=='telefono' : telefono = data['telefono']




		if fecha_inicio:

			fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%dT%H:%M:%S.%fZ')-timedelta(hours=5)

		else:

			fecha_inicio = None


		# print nacimiento
		
		# nacimiento = datetime.datetime.strptime(nacimiento, '%Y-%m-%dT%H:%M:%S.%fZ')

		# 2017-09-06T05:00:00.000Z

		# nacimiento = nacimiento.strftime('%Y-%m-%d')

		# Telefono del usuario

		# TelefonoUser(user_id=u_id,numero=telefono).save()

		c=Cliente(agente_id=id_agente,nombre=first_name,fecha_inicio=fecha_inicio,estado_civil=estado_civil,numero_hijos=numero_hijos,apellido=last_name,direccion=direccion,telefono=telefono).save()
		
		cliente_id = Cliente.objects.all().values('id').order_by('-id')[0]['id']
		
		Agentecliente(agente_id=id_agente,cliente_id=cliente_id).save()

		return HttpResponse(simplejson.dumps(cliente_id), content_type="application/json")

	#Actualiza cliente
	def put(self, request):

		id =request.user.id
		data = json.loads(request.body)

		print 'put..',data

		# parientes': [{u'edad': 0, u'nombre': u'1212', u'id': 294, u'relacion__nombre': u'Hijo', 
		# u'fecha_nacimiento': None}, {u'edad': 0, u'nombre': u'212', u'id': 295, u'relacion__nombre': 
		# u'Hijo', u'fecha_nacimiento': None}], u'fecha_nacimiento': u'2018

		fecha_nacimiento = '1900-01-01'
		conyuge= None
		nombre = None
		apellido = None
		email = None
		telefono = None
		direccion = None
		estado_civil_id = None

		cliente = data['id']
		c=Cliente.objects.get(id=cliente)

		for i in data:

			if i=='fecha_nacimiento':

				if data['fecha_nacimiento']!=None:

					
					fecha_nacimiento = str(data['fecha_nacimiento'])[0:10]

					if len(fecha_nacimiento.split('-'))==3:

						c.fecha_nacimiento=fecha_nacimiento

					else:

						c.fecha_nacimiento='1900-01-01'

			if i=='fecha_nacimiento_conyuge':

				if data['fecha_nacimiento_conyuge']!=None:
					
					fecha_nacimiento_conyuge = str(data['fecha_nacimiento_conyuge'])[0:10]
					c.fecha_nacimiento_conyuge=fecha_nacimiento_conyuge


			if i=='conyuge':
				conyuge = data['conyuge']
				c.conyuge=conyuge
			if i=='nombre':
				nombre = data['nombre']
				c.nombre=nombre

			if i=='edad_conyuge':
				edad_conyuge = data['edad_conyuge']
				c.edad_conyuge=edad_conyuge
			if i=='apellido':
				apellido = data['apellido']
				c.apellido=apellido
			if i=='email':
				email = data['email']
				c.email=email
			if i=='telefono':
				telefono = data['telefono']
				c.telefono=telefono
			if i=='direccion':
				direccion = data['direccion']
				c.direccion=direccion
			if i=='estado_civil':
				estado_civil_id=data['estado_civil']
				c.estado_civil_id=estado_civil_id

			if i=='parientes':

				for p in data['parientes']:

					yeardays = 365

					act_year = datetime.datetime.today().year

					h = ParientesCliente.objects.get(id=p['id'])
					
					h.nombre=p['nombre']

					# fecha_nacimiento = str(p['fecha_nacimiento'])[0:10]

					# data['fecha_nacimiento'] = datetime.datetime.strptime(fecha_nacimiento,'%Y-%m-%d')

					# diff = (datetime.datetime.today() - data['fecha_nacimiento']).days
					# if act_year / 4 == 0 and act_year != 100 or act_year / 400 == 0:
					#     yeardays += 1
					# else:
					#     yeardays = 365
					#     years = str(int(diff/yeardays))

					# print 'edad..',years

					# h.edad=years

					# if p['edad']:

					h.edad=p['edad']

					# if p=='fecha_nacimiento':

					h.save()


		c.save()

		


		
		
		
		


		
		
		
		
		

		# au =AuthUser.objects.get(id=c.user_id)





		# for i in data:

		#   if i=='estado_civil' :c.estado_civil_id=data['estado_civil']
		#   if i=='numero_hijos' : c.numero_hijos=data['numero_hijos']
		#   if i=='first_name' : au.first_name=data['nombre']
		#   if i=='last_name' : au.last_name=data['apellido']
		#   if i=='email' : au.email=data['email']
		#   if i=='pais' : au.pais=data['pais']
		#   if i=='nacimiento' : au.nacimiento=data['user__nacimiento']
		#   if i=='telefono' : telefono=data['telefono']['numero']
		#   if i=='dni' : au.dni=data['user__dni']
		#   if i=='user__direccion' : au.direccion=data['user__direccion']


		# c.save()
		# au.save()




		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

		
	
	#Informacion del cliente
	def get(self,request):

		data = json.loads(request.body)
		cliente=data['cliente']

		c =Cliente.objects.filter(id=cliente).values('fecha_inicio','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__nacimiento','user__dni','user__direccion','conyuge')
		c= simplejson.dumps(ValuesQuerySetToDict(c))
		return HttpResponse(c, content_type="application/json")


class TodosClientes(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):


		id_agente = Agente.objects.get(user_id=request.user.id).id

		perfil = Agente.objects.get(user_id=request.user.id).nivel.nombre

		equipo = Agente.objects.get(user_id=request.user.id).equipo.nombre

		if perfil=='IFA':

			c =Cliente.objects.filter(agente_id=id_agente).values('id','estado_civil','numero_hijos','dni','direccion','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')
		
			for cli in range(len(c)):

				prospecto = PropuestaCliente.objects.filter(cliente_id=c[cli]['id']).values('cliente__nombre','ramo_compania_producto__ramo__nombre')

				c[cli]['propuesta']= ValuesQuerySetToDict(prospecto)

		if perfil=='ADMINISTRADOR':

			c =Cliente.objects.all().values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')
		
		if perfil=='GERENTE':

			# if Agente.objects.get(user_id=request.user.id).subgrupo:

			# 	subgrupo = Agente.objects.get(user_id=request.user.id).subgrupo.nombre

			# 	c =Cliente.objects.filter(agente__subgrupo__nombre=subgrupo).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')
		
			# else:

			c =Cliente.objects.filter(agente_id=id_agente).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')
		

		if perfil=='GERENTE GENERAL':

			c =Cliente.objects.filter(agente_id=id_agente).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')

		if perfil=='DIRECTOR':

			c =Cliente.objects.filter(agente_id=id_agente).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')
		

			# if Agente.objects.get(user_id=request.user.id).grupo:

			#     c =Cliente.objects.filter(agente__grupo__nombre=grupo).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email')
			
			# else:

			#     c =Cliente.objects.filter(agente__equipo__nombre=equipo).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email')
			
		

		if perfil=='PRIVATE CLIENT ADVISOR':

			c =Cliente.objects.filter(agente_id=id_agente).values('id','estado_civil','numero_hijos','dni','conyuge','nombre','apellido','telefono','direccion','email').order_by('-id')
		
		for i in range(len(c)):

			#if Citas.objects.filter(inforce=1,cliente_id=c[i]['id']).count()>0:

			if Citas.objects.filter(cliente_id=c[i]['id'],tipo_seguimiento__nombre='Cierre').count()>0:


				c[i]['cierre'] = True

			else:

				c[i]['cierre'] = False

		#c =Cliente.objects.all().values('id','estado_civil','numero_hijos','user__first_name','user__last_name','user__email','user__pais','user__dni','user__direccion')

		c= simplejson.dumps(ValuesQuerySetToDict(c))

		return HttpResponse(c, content_type="application/json")

class Resumen(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self,request):

		id_agente =Agente.objects.get(user=request.user.id).id

		data = json.loads(request.body)

		s= data['semana']

		se = Semana.objects.filter(numero=s)

		nuevasvisitas=Citas.objects.filter(fecha_cita__gte=se.fecha_inicio,fecha_cita__lte=se.fecha_fin,agente_id=id_agente,tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

		seguimiento=Citas.objects.filter(fecha_cita__gte=se.fecha_inicio,fecha_cita__lte=se.fecha_fin,agente_id=id_agente,tipo_cita__nombre='Seguimiento').count()

		pos=Citas.objects.filter(fecha_cita__gte=se.fecha_inicio,fecha_cita__lte=se.fecha_fin,agente_id=id_agente,tipo_cita__nombre='POS').count()

		
		mes =data['mes']

		nvm = Citas.objects.filter(fecha_cita__month__gte=mes,agente_id=id_agente,tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

		segm = Citas.objects.filter(fecha_cita__month__gte=mes,agente_id=id_agente,tipo_cita__nombre='Seguimiento').count()

		posm = Citas.objects.filter(fecha_cita__month__gte=mes,agente_id=id_agente,tipo_cita__nombre='POS').count()

		produccionmensual=[]

		montomensual = []

		for mes in range(12):

			produccionmensual.push(Citas.objects.filter(fecha_cita__month__gte=mes,tipo_seguimiento__nombre='Cierre').count())
			
			m = Citas.objects.filter(fecha_cita__month__gte=mes,tipo_seguimiento__nombre='Cierre')

			mm =0

			for x in m:
			
				mm=mm+Citas.objects.get(fecha_cita__month__gte=mes,tipo_seguimiento__nombre='Cierre').prima_target
			
			montomensual.push(mm)
			
		data ={'produccionmensual':produccionmensual,'nvm':nvm,'segm':segm,'posm':posm,'nuevasvisitas':nuevasvisitas,'seguimiento':seguimiento,'pos':pos}

		c= simplejson.dumps(data)

		return HttpResponse(c, content_type="application/json")


class Produccionxcia(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		c =Agente.objects.get(user_id=request.user.id)

		c =Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__compania__nombre').annotate(citas=Count('propuesta_cliente__ramo_compania_producto__compania__nombre'))

		c= simplejson.dumps(data)

		return HttpResponse(c, content_type="application/json")


class Calculapropuestasporramo(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		id_agente = Agente.objects.get(user_id=request.user.id).id
		
		r=PropuestaCliente.objects.filter(agente_id=id_agente).values('ramo_compania_producto__ramo__nombre').annotate(total=Count('ramo_compania_producto__ramo__nombre'))
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Calculaproduccionporramoequipo(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):


		agente_id = Agente.objects.get(user_id=request.user.id).id

		_agentes = []

		country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(country_manager)):

			_agentes.append(country_manager[c]['agente_id'])

		bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(bussiness_partner)):

			_agentes.append(bussiness_partner[c]['agente_id'])

		relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_ship_director)):

			_agentes.append(relation_ship_director[c]['agente_id'])

		relation_management= Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management)):

			_agentes.append(relation_management[c]['agente_id'])

		relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management_senior)):

			_agentes.append(relation_management_senior[c]['agente_id'])

		private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client)):

			_agentes.append(private_client[c]['agente_id'])

		private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client_senior)):

			_agentes.append(private_client[c]['agente_id'])

		id_agente = Agente.objects.get(user_id=request.user.id).id

		r = Ramo.objects.all().values('id','nombre')

		for i in range(len(r)):

			pt=Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre=r[i]['nombre']).values('propuesta_cliente__ramo_compania_producto__ramo__nombre').exclude(cliente_antiguo='Yes').annotate(total= Sum('prima_target'))

			r[i]['prima_target'] = ValuesQuerySetToDict(pt)

		r= simplejson.dumps(ValuesQuerySetToDict(r))

		return HttpResponse(r, content_type="application/json")



class Calculaproduccionporramo(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		id_agente = Agente.objects.get(user_id=request.user.id).id

		r = Ramo.objects.all().values('id','nombre')

		for i in range(len(r)):

			pt=Citas.objects.filter(agente_id=id_agente,tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre=r[i]['nombre']).values('propuesta_cliente__ramo_compania_producto__ramo__nombre').exclude(cliente_antiguo='Yes').annotate(total= Sum('prima_target'))

			r[i]['prima_target'] = ValuesQuerySetToDict(pt)

		r= simplejson.dumps(ValuesQuerySetToDict(r))

		return HttpResponse(r, content_type="application/json")



class Produccionxramo(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):

		c =Agente.objects.get(user_id=request.user.id)

		c =Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(citas=Count('propuesta_cliente__ramo_compania_producto__ramo__nombre'))

		c= simplejson.dumps(data)

		return HttpResponse(c, content_type="application/json")




class Month(Func):
	function = 'EXTRACT'
	template = '%(function)s(MONTH from %(expressions)s)'
	output_field = models.IntegerField()    

class MiGestion(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):


		c =Agente.objects.get(user_id=request.user.id)

		avance = c.meta_personal

		x = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes')

		totalcierres = x.count()

		totalcitas = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Nuevo').exclude(cliente_antiguo='Yes').count()

		#totalcitas = Citas.objects.filter(agente_id=c.id,tipo_cita__nombre='Nuevo Prospecto de Cliente').values('cliente').exclude(cliente_antiguo='Yes').annotate(total=Count('cliente')).count()


		if totalcitas==0:

			efectividad = 0

		else:

			efectividad = totalcierres*100/totalcitas

		ytd=0

		for n in x:

			if n.prima_target:
				ytd =ytd+float(n.prima_target)

		

		#Produccion por compania

		cias = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes').values('propuesta_cliente__ramo_compania_producto__compania__nombre').order_by('propuesta_cliente__ramo_compania_producto__compania__nombre').annotate(contador=Sum('prima_target'),casos=Count('propuesta_cliente__ramo_compania_producto__compania'))
		
		for i in range(len(cias)):

			produccion_cias = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__compania__nombre=cias[i]['propuesta_cliente__ramo_compania_producto__compania__nombre'],inforce=1).exclude(cliente_antiguo='Yes').values('propuesta_cliente__ramo_compania_producto__compania').annotate(produccion=Sum('prima_target'))
			
			print 'produccion_cias',produccion_cias.count()

			if produccion_cias.count()>0:

				cias[i]['inforce'] = produccion_cias[0]['produccion']

			else:

				cias[i]['inforce']=0

		#Produccion por ramos

		ramos = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes').values('propuesta_cliente__ramo_compania_producto__ramo__nombre').order_by('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(contador=Sum('prima_target'),casos=Count('propuesta_cliente__ramo_compania_producto__ramo'))
		
		for i in range(len(ramos)):

			produccion_ramos = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre=ramos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre'],inforce=1).exclude(cliente_antiguo='Yes').values('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(produccion=Sum('prima_target'))
			
			

			if len(produccion_ramos)>0:

				ramos[i]['inforce'] = produccion_ramos[0]['produccion']

			else:

				ramos[i]['inforce']=0

			#ramos[i]['contador'] = "{:,}".format(ramos[i]['contador'])

		ramos = ValuesQuerySetToDict(ramos)

		cias = ValuesQuerySetToDict(cias)

		nuevosnegocios = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre',cliente_antiguo='No').count()

		#nuevosprospectos = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Nuevo').count()

		nuevosprospectos = Citas.objects.filter(agente_id=c.id,tipo_cita__nombre='Nuevo Prospecto de Cliente',cliente_antiguo='No').values('cliente_id').order_by('cliente_id').annotate(total=Count('cliente_id')).count()

		#nuevosprospectos = Citas.objects.filter(fecha_cita__lte=fecha_cita__lte,fecha_cita__gte=fecha_cita__gte,agente_id=c[i]['id'],tipo_cita__nombre='Nuevo Prospecto de Cliente').values('cliente__nombre').exclude(cliente_antiguo='Yes').annotate(total=Count('cliente__nombre')).count()
					

		#Produccion por compania

		if nuevosprospectos==0:

			efectividad=0

		else:

			efectividad = nuevosnegocios*100/nuevosprospectos

		produccionmensual = Citas.objects.filter(agente_id=c.id,tipo_seguimiento__nombre='Cierre').values('semana__mes__nombre').order_by('semana__mes__id').exclude(cliente_antiguo='Yes').annotate(produccion_cierre=Sum('prima_target'),casos=Count('semana__mes__nombre'))

		for i in range(len(produccionmensual)):

			produccion_inforce = Citas.objects.filter(semana__mes__nombre=produccionmensual[i]['semana__mes__nombre'],agente_id=c.id,tipo_seguimiento__nombre='Cierre',inforce=1).exclude(cliente_antiguo='Yes').values('semana__mes__nombre').order_by('semana__mes__id').annotate(produccion=Sum('prima_target'))
			
			

			if len(produccion_inforce)>0:

				produccionmensual[i]['inforce'] = produccion_inforce[0]['produccion']

			else:

				produccionmensual[i]['inforce'] = 0


		produccionmensual = ValuesQuerySetToDict(produccionmensual)

		ytdavance=ytd

		ytd="{:,}".format(ytd)



		data={'nuevosnegocios':nuevosnegocios,'nuevosprospectos':nuevosprospectos,'ramos':ramos,'cias':cias,'produccionmensual':produccionmensual,'efectividad':efectividad,'ytdavance':ytdavance,'ytd':ytd,'meta_personal':c.meta_personal,'meta_requerida':c.meta_requerida,'avance':avance}
		data= simplejson.dumps(data)
		return HttpResponse(data, content_type="application/json")

class MiGestionequipo(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request):


		#.....

		agente_id = Agente.objects.get(user_id=request.user.id).id

		_agentes = []

		_agentes.append(agente_id)

		country_manager= Agentejerarquia.objects.filter(country_manager_id=agente_id).exclude(country_manager_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(country_manager)):

			_agentes.append(country_manager[c]['agente_id'])

		bussiness_partner = Agentejerarquia.objects.filter(bussiness_partner_id=agente_id).exclude(bussiness_partner_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(bussiness_partner)):

			_agentes.append(bussiness_partner[c]['agente_id'])

		relation_ship_director = Agentejerarquia.objects.filter(relation_ship_director_id=agente_id).exclude(relation_ship_director_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_ship_director)):

			_agentes.append(relation_ship_director[c]['agente_id'])

		relation_management= Agentejerarquia.objects.filter(relation_management_id=agente_id).exclude(relation_management_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management)):

			_agentes.append(relation_management[c]['agente_id'])

		relation_management_senior= Agentejerarquia.objects.filter(relation_management_senior_id=agente_id).exclude(relation_management_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(relation_management_senior)):

			_agentes.append(relation_management_senior[c]['agente_id'])

		private_client = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client)):

			_agentes.append(private_client[c]['agente_id'])

		private_client_senior = Agentejerarquia.objects.filter(private_client_senior_id=agente_id).exclude(private_client_senior_id=142).values('id','agente_id','agente__nombre','agente__apellidos')

		for c in range(len(private_client_senior)):

			_agentes.append(private_client[c]['agente_id'])




		c =Agente.objects.get(user_id=request.user.id)

		avance = c.meta_personal

		x = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes')

		totalcierres = x.count()

		totalcitas = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Nuevo').exclude(cliente_antiguo='Yes').count()


		ytd=0

		for n in x:

			if n.prima_target:
				ytd =ytd+float(n.prima_target)

		

		#Produccion por compania

		cias = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__compania__nombre').exclude(cliente_antiguo='Yes').order_by('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(contador=Sum('prima_target'),casos=Count('propuesta_cliente__ramo_compania_producto__compania'))
		
		for i in range(len(cias)):

			produccion_cias = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__compania__nombre=cias[i]['propuesta_cliente__ramo_compania_producto__compania__nombre'],inforce=1).exclude(cliente_antiguo='Yes').values('propuesta_cliente__ramo_compania_producto__compania').order_by('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(produccion=Sum('prima_target'))
			
			

			if produccion_cias.count()>0:

				cias[i]['inforce'] = produccion_cias[0]['produccion']

			else:

				cias[i]['inforce']=0


		ramos = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre').values('propuesta_cliente__ramo_compania_producto__ramo__nombre').exclude(cliente_antiguo='Yes').order_by('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(contador=Sum('prima_target'),casos=Count('propuesta_cliente__ramo_compania_producto__ramo'))
		
		for i in range(len(ramos)):

			produccion_ramos = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre',propuesta_cliente__ramo_compania_producto__ramo__nombre=ramos[i]['propuesta_cliente__ramo_compania_producto__ramo__nombre'],inforce=1).values('propuesta_cliente__ramo_compania_producto__ramo__nombre').exclude(cliente_antiguo='Yes').order_by('propuesta_cliente__ramo_compania_producto__ramo__nombre').annotate(produccion=Sum('prima_target'))
			
			if produccion_ramos.count()>0:

				ramos[i]['inforce'] = produccion_ramos[0]['produccion']

			else:

				ramos[i]['inforce']=0

			#ramos[i]['contador'] = "{:,}".format(ramos[i]['contador'])

		ramos = ValuesQuerySetToDict(ramos)

		cias = ValuesQuerySetToDict(cias)

		nuevosnegocios = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre').exclude(cliente_antiguo='Yes').count()

		#nuevosprospectos = Citas.objects.filter(agente_id__in=_agentes,tipo_cita__nombre='Nuevo Prospecto de Cliente').exclude(cliente_antiguo='Yes').count()

		nuevosprospectos = Citas.objects.filter(agente_id__in=_agentes,tipo_cita__nombre='Nuevo Prospecto de Cliente',cliente_antiguo='No').values('cliente_id').order_by('cliente_id').annotate(total=Count('cliente_id')).count()

		#Produccion por compania

		if nuevosprospectos==0:

			efectividad=0

		else:

			efectividad= nuevosnegocios*100/nuevosprospectos

		produccionmensual = Citas.objects.filter(agente_id__in=_agentes,tipo_seguimiento__nombre='Cierre').values('semana__mes__nombre').order_by('semana__mes__nombre').exclude(cliente_antiguo='Yes').annotate(produccion_cierre=Sum('prima_target'),casos=Count('semana__mes__nombre'))

		for i in range(len(produccionmensual)):

			produccion_inforce = Citas.objects.filter(semana__mes__nombre=produccionmensual[i]['semana__mes__nombre'],agente_id=c.id,tipo_seguimiento__nombre='Cierre',inforce=1).values('semana__mes__nombre').order_by('semana_id').exclude(cliente_antiguo='Yes').annotate(produccion=Sum('prima_target'))
			
			if len(produccion_inforce)>0:

				produccionmensual[i]['inforce'] = produccion_inforce[0]['produccion']

			else:

				produccionmensual[i]['inforce'] = 0



		produccionmensual = ValuesQuerySetToDict(produccionmensual)

		ytdavance=ytd

		# ytd="{:,}".format(ytd)





		data={'nuevosnegocios':nuevosnegocios,'nuevosprospectos':nuevosprospectos,'ramos':ramos,'cias':cias,'produccionmensual':produccionmensual,'efectividad':efectividad,'ytdavance':ytdavance,'ytd':ytd,'meta_personal':c.meta_equipo,'meta_requerida':c.meta_requerida,'avance':avance}
		data= simplejson.dumps(data)
		return HttpResponse(data, content_type="application/json")

class Metricas(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def get(self,request,mes,dia,mes1,dia1):

		#Setiembre

		con =0

		if len(mes)==1:
			mes='0'+mes
		if len(dia)==1:
			dia='0'+dia
		if len(dia1)==1:
			dia1='0'+dia1
		if len(mes1)==1:
			mes1='0'+mes1

		inicio= '2018-'+str(mes)+'-'+str(dia)

		fin = '2018-'+str(mes1)+'-'+str(dia1)

		inicio = datetime.datetime.strptime(inicio, '%Y-%m-%d')

		fin = datetime.datetime.strptime(fin, '%Y-%m-%d')

		

		agente = Agente.objects.get(user_id=request.user.id).id

		c=Citas.objects.filter(agente_id=agente,fecha_cita__gte=inicio,fecha_cita__lt=fin,tipo_cita__nombre='Seguimiento de Prospectos').exclude(tipo_cita__nombre='Nuevo Prospecto de Cliente').exclude(cliente_antiguo='Yes').count() 

		ce=Citas.objects.filter(agente_id=agente,tipo_cita__nombre='Cita de Equipo',fecha_cita__gte=inicio,fecha_cita__lt=fin).exclude(cliente_antiguo='Yes').count() 

		p=Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='POS',fecha_cita__gte=inicio,fecha_cita__lt=fin).exclude(cliente_antiguo='Yes').count() 

		#n =Citas.objects.filter(agente_id=agente,fecha_cita__gte=inicio,fecha_cita__lte=fin,tipo_cita__nombre='Nuevo Prospecto de Cliente').count()

		cli = Cliente.objects.filter(agente_id=agente)

		for i in cli:

			if Citas.objects.filter(cliente_id=i.id,fecha_cita__gte=inicio,fecha_cita__lt=fin,tipo_cita__nombre='Nuevo Prospecto de Cliente').exclude(cliente_antiguo='Yes').count()>0:

				con = con+1


		n = con




		x={'ce':ce,'c':c,'n':n,'p':p,'t':int(c)+int(n)+int(p)}



		c= simplejson.dumps(x)



		return HttpResponse(c, content_type="application/json")

class Creacita(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self, request):

		data = json.loads(request.body)

		

		cliente=None
		tipo_cita=None
		propuesta_cliente=None
		tipo_seguimiento=None
		fecha_cita=None
		observacion=''
		fecha_solicitud=None
		prima_target=''
		modalidad=None
		prima_anual=''
		fecha_poliza=None
		seguimiento=None
		cierre=None
		poliza=None
		agente=Agente.objects.get(user=request.user.id).id

		for i in data:

			if i=='cliente': cliente=data['cliente']
			if i=='tipo_cita': tipo_cita=data['tipo_cita']
			if i=='tipo_seguimiento':tipo_seguimiento=data['tipo_seguimiento']
			if i=='propuesta': 

				propuesta_cliente=data['propuesta']['id']

				

			for f in data['form']:

				if f=='observacion':observacion=data['form']['observacion']
				if f=='prima_target':prima_target=data['form']['prima_target']
				if f=='prima_anual':prima_anual=data['form']['prima_anual']
				if f=='fecha_cita': fecha_cita=data['form']['fecha_cita']
				if f=='fecha_solicitud': fecha_solicitud=data['form']['fecha_solicitud']
				if f=='modalidad': modalidad=data['form']['modalidad']['id']
				if f=='fecha_poliza': fecha_poliza=data['form']['fecha_poliza']
				
			if i=='seguimiento': seguimiento=data['seguimiento']
			if i=='cierre': cierre=data['cierre']
			if i=='poliza': poliza=data['poliza']


			
			if tipo_seguimiento==2:

				print tipo_seguimiento



		# if fecha_cita==None:
		fecha_creacion=datetime.datetime.now()



		fecha_cita = datetime.datetime.strptime(fecha_cita, '%Y-%m-%dT%H:%M:%S.%fZ')-timedelta(hours=5)

		if fecha_solicitud:

			fecha_solicitud = datetime.datetime.strptime(fecha_solicitud, '%Y-%m-%dT%H:%M:%S.%fZ')-timedelta(hours=5)
		
		if fecha_poliza:

			fecha_poliza = datetime.datetime.strptime(fecha_poliza, '%Y-%m-%dT%H:%M:%S.%fZ')-timedelta(hours=5)

		print 'fecha_cita',fecha_cita

		#Cita... {u'seguimiento': 1, u'propuesta': {u'agente': None, u'ramo_compania_producto__compania__nombre': u'NWL', u'id': 8, u'ramo_compania_producto__producto__nombre': u'Index Select', u'cliente__user__first_name': u'Andy', u'ramo_compania_producto__ramo__nombre': u'Vida Int', u'cliente': 13}, u'cliente': u'13', u'form': {u'observacion': u'3232'}}

		if seguimiento==1: tipo_seguimiento=1
		if cierre==1:tipo_seguimiento=2
		if poliza==1:tipo_seguimiento=3

		tipo_cita= 2 ##Seguimiento

		if tipo_seguimiento ==3 :

			Citas.objects.filter(propuesta_cliente_id=propuesta_cliente,agente_id=agente).update(fecha_poliza=fecha_poliza,prima_target=prima_target,modalidad_id=modalidad,prima_anual=prima_anual)

		if tipo_seguimiento == 2 :

			Citas.objects.filter(propuesta_cliente_id=propuesta_cliente,agente_id=agente).update(prima_target=prima_target,modalidad_id=modalidad,prima_anual=prima_anual)

		sem= traesemana(fecha_cita)

		Citas(semana_id=sem,fecha_creacion=fecha_creacion,agente_id=agente,tipo_seguimiento_id=tipo_seguimiento,cliente_id=cliente,tipo_cita_id=tipo_cita,propuesta_cliente_id=propuesta_cliente,observacion=observacion,fecha_cita=fecha_cita,fecha_solicitud=fecha_solicitud,prima_target=prima_target,modalidad_id=modalidad,prima_anual=prima_anual,fecha_poliza=fecha_poliza).save()


		c= simplejson.dumps('cliente')
		return HttpResponse(c, content_type="application/json")


class Creapos(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self, request):

		data = json.loads(request.body)

		

		print ' Entre POS....'

		cliente=None
		tipo_cita=None
		propuesta_cliente=None
		tipo_seguimiento=None
		fecha_cita=None
		observacion=''
		fecha_solicitud=None
		prima_target=''
		modalidad=None
		prima_anual=''
		fecha_poliza=None
		seguimiento=None
		cierre=None
		poliza=None
		producto =None
		id_agente=Agente.objects.get(user=request.user.id).id

		
		for i in data:

			if i=='observacion': observacion=data['observacion']
			if i=='fecha_cita': fecha_cita=data['fecha_cita']
			if i=='pos':producto=data['pos']
			if i=='tipo_cita': tipo_cita=data['tipo_cita']
			if i=='cliente': id_cliente=data['cliente']

		tipo_cita= 3 # POS


		if producto==None:

			c= simplejson.dumps('OK')
			return HttpResponse(c, content_type="application/json")



		if fecha_cita:

			fecha_cita = datetime.datetime.strptime(fecha_cita, '%Y-%m-%dT%H:%M:%S.%fZ')-timedelta(hours=5)


		_pos=Citas.objects.filter(propuesta_cliente_id=producto,agente_id=id_agente,cliente_id=id_cliente)

		fecha_creacion=datetime.datetime.now()

		sem= traesemana(fecha_cita)

		Citas(semana_id=sem,tipo_seguimiento_id=4,fecha_creacion=fecha_creacion,agente_id=id_agente,cliente_id=id_cliente,tipo_cita_id=tipo_cita,propuesta_cliente_id=producto,observacion=observacion,fecha_cita=fecha_cita).save()

		if _pos.count()>0:

			asesor_anterior = _pos[0].asesor_anterior

			fecha_poliza=_pos[0].fecha_poliza

			numero_poliza=_pos[0].numero_poliza
			
			if _pos[0].modalidad:
				modalidad=_pos[0].modalidad.id
			status_poliza=_pos[0].status_poliza.id

			Citas.objects.filter(propuesta_cliente_id=producto,agente_id=id_agente,cliente_id=id_cliente).update(asesor_anterior=asesor_anterior,fecha_poliza=fecha_poliza,numero_poliza=numero_poliza,modalidad_id=modalidad,status_poliza_id=status_poliza)


		c= simplejson.dumps('cliente')
		return HttpResponse(c, content_type="application/json")


class Creapropuesta(JSONWebTokenAuthMixin, View):

	#Crea nuevo propuesta
	def post(self, request):



		data = json.loads(request.body)



		isChecked = False

		agente=Agente.objects.get(user=request.user.id).id

		cliente=None
		cia= None
		observacion=''
		compania= None
		producto=None
		rcp=None
		interes=''
		fecha_poliza=None
		fecha_solicitud=None
		prima_target=None
		sntp = None
		cliant = None
		prima_anual=None
		modalidad=None



		for i in data:

			if i=='cliente':cliente=data['cliente']
			if i=='observacion':observacion=data['observacion']
			if i=='cia':cia=data['cia']
			if i=='producto':producto=data['producto']
			if i=='ramo':ramo=data['ramo']['id']
			if i=='interes':interes=data['interes']['name']
			if i=='modalidad':modalidad=data['modalidad']['id']
			if i=='fecha_poliza':fecha_poliza=data['fecha_poliza']
			if i=='fecha_solicitud':fecha_solicitud=data['fecha_solicitud']
			if i=='prima_anual':prima_anual=data['prima_anual']
			if i=='prima_target':prima_target=data['prima_target']
			if i=='isChecked':isChecked=data['isChecked']

			if i=='seguimientonp':

				sntp = 1

			if i=='clienteantiguo':

				cliant = 1

		rcp=RamoCompaniaProducto.objects.get(compania_id=cia,ramo_id=ramo,producto_id=producto).id

		if cliente:

			PropuestaCliente(cliente_id=cliente,fecha=datetime.datetime.now(),agente_id=agente,observacion=observacion,ramo_compania_producto_id=rcp,interes=interes).save()
			
			id_propuesta=PropuestaCliente.objects.all().values('id').order_by('-id')[0]['id']

			fecha_inicio = Cliente.objects.get(id=cliente).fecha_inicio

			if fecha_inicio==None:

				fecha_inicio = datetime.datetime.now()



			sem= traesemana(fecha_inicio)

			if sntp == 1:

				Citas(semana_id=sem,tipo_seguimiento_id=1,fecha_creacion=datetime.datetime.now(),agente_id=agente,cliente_id=cliente,tipo_cita_id=1,propuesta_cliente_id=id_propuesta,observacion=observacion,fecha_cita=fecha_inicio).save()

			else:

				if cliant!=1:

					Citas(semana_id=sem,tipo_seguimiento_id=5,fecha_creacion=datetime.datetime.now(),agente_id=agente,cliente_id=cliente,tipo_cita_id=1,propuesta_cliente_id=id_propuesta,observacion=observacion,fecha_cita=fecha_inicio).save()

				else:

					print 'Es cliente antiguo'

			if isChecked==True:

				Citas(cliente_antiguo='Yes',fecha_poliza=fecha_poliza,fecha_solicitud=fecha_solicitud,prima_target=prima_target,modalidad_id=modalidad,prima_anual=prima_anual,semana_id=sem,tipo_seguimiento_id=2,fecha_creacion=datetime.datetime.now(),agente_id=agente,cliente_id=cliente,tipo_cita_id=2,propuesta_cliente_id=id_propuesta,observacion=observacion,fecha_cita=fecha_inicio).save()

				id_cita=Citas.objects.all().values('id').order_by('-id')[0]['id']

				ci = Citas.objects.get(id=id_cita)
				ci.inforce=1
				ci.save()

			c= simplejson.dumps(cliente)

			return HttpResponse(c, content_type="application/json")

		else:

			c= simplejson.dumps(cliente)

			return HttpResponse(c, content_type="application/json")



	#Actualizapropuesta
	def put(self, request):

		data = json.loads(request.body)
		propuesta = data['propuesta']

		p=PropuestaCliente.objects.get(id=propuesta)

		for i in data:
			if i=='cliente':p.cliente=data['cliente']
			if i=='agente':p.agente=data['agente']
			if i=='observacion':p.observacion=data['observacion']
			if i=='fecha':p.fecha=data['fecha']
			if i=='detalle':p.detalle=data['detalle']
			if i=='ramo_compania_producto':p.ramo_compania_producto=data['ramo_compania_producto']

		p.save()
		return HttpResponse(simplejson.dumps('OK'), content_type="application/json")

class Listaramos(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Ramo.objects.all().values('id','nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")

class ListaModalidad(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Modalidad.objects.all().values('id','nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Losarchivos(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Archivo.objects.all().values('id','nombre','ruta')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class IconosLista(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Iconos.objects.all().values('id','nombre','icono').order_by('id')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Semanasall(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		r=Semanas.objects.all().values('id','numero').order_by('-id')

		fmt = '%d %b'

		for j in range(len(r)):

			r[j]['fecha_inicio'] = Semanas.objects.get(id=r[j]['id']).fecha_inicio.strftime(fmt)
			r[j]['fecha_fin'] = Semanas.objects.get(id=r[j]['id']).fecha_fin.strftime(fmt)
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Semanasresumen(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

		age = Agente.objects.get(user_id=request.user.id).id

		meses = Mes.objects.all().values('id','nombre').order_by('id')

		fmt = '%d'

		for j in range(len(meses)):

			sem = Semanas.objects.filter(mes_id=meses[j]['id']).values('id','numero')

			for s in range(len(sem)):

				sem[s]['fecha_inicio'] = Semanas.objects.get(id=sem[s]['id']).fecha_inicio.strftime(fmt)
				
				sem[s]['fecha_fin'] = Semanas.objects.get(id=sem[s]['id']).fecha_fin.strftime(fmt)

				sem[s]['nuevos'] = Citas.objects.filter(agente_id=age,semana__numero=sem[s]['numero'],tipo_cita__nombre='Nuevo Prospecto de Cliente').values('cliente').order_by('cliente_id').exclude(cliente_antiguo='Yes').annotate(total=Count('cliente')).count()

				sem[s]['seguimiento']= Citas.objects.filter(agente_id=age,semana__numero=sem[s]['numero'],tipo_cita__nombre='Seguimiento de Prospectos').exclude(cliente_antiguo='Yes').count()

				sem[s]['pos']=Citas.objects.filter(agente_id=age,semana__numero=sem[s]['numero'],tipo_cita__nombre='POS').exclude(cliente_antiguo='Yes').count()

				sem[s]['citaequipo']=Citas.objects.filter(agente_id=age,semana__numero=sem[s]['numero'],tipo_cita__nombre='Cita de Equipo').exclude(cliente_antiguo='Yes').count()


				sem[s]['total']=sem[s]['nuevos']+sem[s]['seguimiento']+sem[s]['pos']+sem[s]['citaequipo']

			meses[j]['semanas']=ValuesQuerySetToDict(sem)

		r= simplejson.dumps(ValuesQuerySetToDict(meses))




		return HttpResponse(r, content_type="application/json")

class Calculacitas(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,mes):

		age=Agente.objects.get(user=request.user.id).id


		_sem = Semanas.objects.filter(mes_id=mes)

		se = []

		for s in _sem:


			se.append(s.id)


		nn = Citas.objects.filter(agente_id=age,semana_id__in=se,tipo_cita__nombre='Nuevo Prospecto de Cliente').values('cliente').exclude(cliente_antiguo='Yes').annotate(total=Count('cliente')).count()

		ncitasmes = nn


		nseguimientomes = Citas.objects.filter(agente_id=age,tipo_cita__nombre='Seguimiento de Prospectos',semana_id__in=se).exclude(cliente_antiguo='Yes').count()

		nposmes = Citas.objects.filter(agente_id=age,tipo_cita__nombre='POS',semana_id__in=se).exclude(cliente_antiguo='Yes').count()

		ncitasequipo = Citas.objects.filter(agente_id=age,tipo_cita__nombre='Cita de Equipo',semana_id__in=se).exclude(cliente_antiguo='Yes').count()



		r={'ncitasmes':ncitasmes,'nseguimientomes':nseguimientomes,'nposmes':nposmes,'ncitasequipo':ncitasequipo}

		r= simplejson.dumps(r)
		return HttpResponse(r, content_type="application/json")



class Calculomes(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request):

	
		agente=Agente.objects.get(user=request.user.id).id

		cli = Cliente.objects.filter(agente_id=agente)


		# for c in cli:

		#     if Citas.objects.filter(tipo_cita__nombre='Nuevo Prospecto Cliente').count()

		# Por mes

		ncitasmes = (Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='Nuevo')
					  .annotate(m=Month('fecha_cita'))
					  .values('m')
					  .annotate(total=Count('cliente'))
					  .annotate(produccion=Sum('prima_target'))
					  .order_by())

		ncitasmes= simplejson.dumps(ValuesQuerySetToDict(ncitasmes))

		nseguimientomes = (Citas.objects.filter(agente_id=agente,tipo_cita__nombre='Seguimiento de Prospectos')
					  .annotate(m=Month('fecha_cita'))
					  .values('m')
					  .annotate(total=Count('cliente'))
					  .annotate(produccion=Sum('prima_target'))
					  .order_by())

		nseguimientomes= simplejson.dumps(ValuesQuerySetToDict(nseguimientomes))

		nposmes = (Citas.objects.filter(agente_id=agente,tipo_cita__nombre='POS')
					  .annotate(m=Month('fecha_cita'))
					  .values('m')
					  .annotate(total=Count('cliente'))
					  .annotate(produccion=Sum('prima_target'))
					  .order_by())

		nposmes= simplejson.dumps(ValuesQuerySetToDict(nposmes))


		r={'ncitasmes':ncitasmes,'nseguimientomes':nseguimientomes,'nposmes':nposmes}

		r= simplejson.dumps(r)
		return HttpResponse(r, content_type="application/json")


class Calculoanio(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self,request,anio):

	
		agente=Agente.objects.get(user=request.user.id).id

		# Por anio

		ncitas2018nuevo = Citas.objects.filter(agente_id=agente,fecha_cita__gte='2018-01-01',fecha_cita__lte='2018-12-31',tipo_seguimiento__nombre='Nuevo').values('cliente').annotate(total=Count('cliente')).count()

		ncitas2018seguimiento = Citas.objects.filter(agente_id=agente,fecha_cita__gte='2018-01-01',fecha_cita__lte='2018-12-31',tipo_cita__nombre='Seguimiento de Prospectos').count()

		ncitas2018pos = Citas.objects.filter(agente_id=agente,fecha_cita__gte='2018-01-01',fecha_cita__lte='2018-12-31',tipo_cita__nombre='POS').count()


		ncitas2018equipo = Citas.objects.filter(agente_id=agente,fecha_cita__gte='2018-01-01',fecha_cita__lte='2018-12-31',tipo_cita__nombre='Cita de Equipo').count()


		r={'ncitas2018equipo':ncitas2018equipo,'ncitas2018nuevo':ncitas2018nuevo,'ncitas2018seguimiento':ncitas2018seguimiento,'ncitas2018pos':ncitas2018pos}

		r= simplejson.dumps(r)

		return HttpResponse(r, content_type="application/json")


class Calculo(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,semana):

		s=Semanas.objects.get(numero=semana)


		agente=Agente.objects.get(user=request.user.id).id

		#Intervalos de fechas

		nuevascitas = Citas.objects.filter(agente_id=agente,tipo_seguimiento__nombre='Nuevo',fecha_cita__gte=s.fecha_inicio,fecha_cita__lte=s.fecha_fin).count()

		nseguimiento = Citas.objects.filter(agente_id=agente,tipo_cita__nombre='Seguimiento de Prospectos',fecha_cita__gte=s.fecha_inicio,fecha_cita__lte=s.fecha_fin).count()

		npos = Citas.objects.filter(agente_id=agente,tipo_cita__nombre='POS',fecha_cita__gte=s.fecha_inicio,fecha_cita__lte=s.fecha_fin).count()




		r={'ncitas':nuevascitas,'nseguimiento':nseguimiento,'npos':npos}

		r= simplejson.dumps(r)
		return HttpResponse(r, content_type="application/json")


class Detallepropuesta(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,id):

		r=PropuestaCliente.objects.filter(id=id).values('observacion','id','agente','cliente','ramo_compania_producto__ramo__nombre','ramo_compania_producto__compania__nombre','ramo_compania_producto__producto__nombre','cliente__nombre','cliente__id','interes')
		
		fmt = '%Y-%m-%d'

		for j in range(len(r)):


			r[j]['cierretitulo'] = 'Detalle de Propuesta'

			
			_historialcitas = Citas.objects.filter(propuesta_cliente_id=r[j]['id']).values('id','numero_poliza','tipo_cita__nombre','tipo_seguimiento__nombre','cliente__nombre','prima_target','prima_anual','modalidad__nombre','observacion').order_by('id')
			
			fmt = '%d/%m/%Y'

			for x in range(len(_historialcitas)):

				_historialcitas[x]['fecha'] = Citas.objects.get(id=_historialcitas[x]['id']).fecha_cita.strftime(fmt)



			r[j]['historialcitas'] = ValuesQuerySetToDict(_historialcitas)

			r[j]['cierrehistorial'] = 'Historial de Propuestas'

			_citas = Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre').values('id','numero_poliza','tipo_seguimiento__nombre','cliente__nombre','prima_target','prima_anual','modalidad__nombre').order_by('-id')
			
			if _citas.count()>0:


				r[j]['cierretitulo'] = 'Producto Cerrado'

				r[j]['cierrehistorial'] = 'Historial de Negocio'

				_citas = _citas[0]

				if _citas['prima_anual']:

					prianu = _citas['prima_anual'].split('.')

					if len(prianu)==2:

						prianu = int(_citas['prima_anual'].split('.')[0])

					else:

						prianu = int(_citas['prima_anual'])

					r[j]['prima_anual'] = prianu

				if _citas['prima_target']:

					primatar = _citas['prima_target'].split('.')

					print 'primatar.......',len(primatar)

					if len(primatar)==2:

						primatar=int(_citas['prima_target'].split('.')[0])

					else:

						primatar = int(_citas['prima_target'])

					r[j]['prima_target'] = primatar

				r[j]['modalidad'] = _citas['modalidad__nombre']

				r[j]['numero_poliza'] = _citas['numero_poliza']

				if Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre').order_by('-id')[0].fecha_solicitud:

					r[j]['fecha_solicitud'] = Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre').order_by('-id')[0].fecha_solicitud.strftime(fmt)

				if Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre').order_by('-id')[0].fecha_poliza:

					r[j]['fecha_poliza'] = Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre').order_by('-id')[0].fecha_poliza.strftime(fmt)


			if PropuestaCliente.objects.get(id=r[j]['id']).fecha:

				r[j]['fecha'] = PropuestaCliente.objects.get(id=r[j]['id']).fecha.strftime(fmt)

		r= simplejson.dumps(ValuesQuerySetToDict(r))

		return HttpResponse(r, content_type="application/json")





@csrf_exempt
def subire(request):


	df = pd.read_csv('/home/capital/subire.csv')

	base = []

	todos = []


	nombre= ''

	# for i in range(df.shape[0]):

	# 	#Agente

	# 	print i

	# 	asesor_anterior = df['Asesor Inicial'][i]

	# 	asesor = df['Asesor Responsable'][i]

	# 	dni = df['ID']


	# 	a = Agente.objects.filter(user__username__contains=asesor)

	# 	if a.count()>0:

	# 		age = a[0].id

	# 	else:

	# 		print df['Asesor Responsable'][i]

	# 	#Cliente

	# 	clien = df['Cliente'][i]

	# 	ramo = df['Ramo'][i]

	# 	compania = df['Compana'][i]

	# 	producto = df['Producto'][i]

	# 	print ramo,compania,producto

	# 	rcp = RamoCompaniaProducto.objects.filter(ramo__nombre=ramo,compania__nombre=compania,producto__nombre=producto)

	# 	print 'Rama encontrada...',rcp.count()

	# 	numero_poliza=df['Poliza'][i]

	# 	fecha_poliza=df['Fecha Vigencia'][i]

	# 	_modalidad = df['Modalidad'][i]

	# 	## Si el cliente existe

	# 	if Cliente.objects.filter(nombre=clien).count() > 0:

	# 		#
	# 		id_cliente = Cliente.objects.get(nombre=clien).id

	# 	else:

	# 		##

	# 		Cliente(agente_id=age,nombre=clien,upload_ene_jul_2019_ecu=1,dni=dni).save()

	# 		id_cliente=Cliente.objects.all().values('id').order_by('-id')[0]['id']


	# 	print '_modalidad',_modalidad

	# 	if _modalidad:

	# 		_modalidad = _modalidad.capitalize()

	# 	else:

	# 		_modalidad = 'Anual'

	# 	mo = Modalidad.objects.filter(nombre__contains=_modalidad)

	# 	print _modalidad,mo

	# 	if mo.count()>0:

	# 		modalidaddato = mo[0].id

	# 	else:

	# 		print _modalidad


	# 	fecha_poliza = datetime.datetime.strptime(fecha_poliza, '%d/%m/%Y')
		
	# 	status = df['Estatus'][i]

	# 	ss =Statuspoliza.objects.filter(nombre__contains=status)

	# 	if ss.count()>0:

	# 		es = ss[0].id

	# 	else:

	# 		es=1

	# 	PropuestaCliente(cliente_id=id_cliente,ramo_compania_producto_id=rcp[0].id,agente_id=age,upload_csv_julio_enero_2019=1,fecha=fecha_poliza).save()

	# 	id_propuesta=PropuestaCliente.objects.all().values('id').order_by('-id')[0]['id']

	# 	Citas(tipo_cita_id=2,tipo_seguimiento_id=2,cliente_id=id_cliente,propuesta_cliente_id=id_propuesta,agente_id=age,numero_poliza=numero_poliza,fecha_poliza=fecha_poliza,status_poliza_id=es,cliente_antiguo='Yes',upload_ene_jul_2019_ecu=1,fecha_cita=fecha_poliza,modalidad_id=modalidaddato,asesor_anterior=asesor_anterior).save()

	# 	Citas(tipo_cita_id=3,tipo_seguimiento_id=4,cliente_id=id_cliente,propuesta_cliente_id=id_propuesta,agente_id=age,numero_poliza=numero_poliza,fecha_poliza=fecha_poliza,status_poliza_id=es,cliente_antiguo='Yes',upload_ene_jul_2019_ecu=1,fecha_cita=fecha_poliza,modalidad_id=modalidaddato,asesor_anterior=asesor_anterior).save()


	print 'encontrados',len(todos)

	return HttpResponse('ok', content_type="application/json")









































@csrf_exempt
def subirarchivo(request):


	df = pd.read_csv('/home/capital/pos_julio_enero_2019_ecuador.csv')

	base = []

	todos = []

	asesor_anterior= ''

	for i in range(df.shape[0]):

		#Agente

		print i

		asesor_anterior = df['Asesor Inicial'][i]

		asesor = df['Asesor Responsable'][i]

		dni = df['ID']


		a = Agente.objects.filter(user__username__contains=asesor)

		if a.count()>0:

			age = a[0].id

		else:

			print df['Asesor Responsable'][i]

		#Cliente

		clien = df['Cliente'][i]

		ramo = df['Ramo'][i]

		compania = df['Compana'][i]

		producto = df['Producto'][i]

		print ramo,compania,producto

		rcp = RamoCompaniaProducto.objects.filter(ramo__nombre=ramo,compania__nombre=compania,producto__nombre=producto)

		print 'Rama encontrada...',rcp.count()

		numero_poliza=df['Poliza'][i]

		fecha_poliza=df['Fecha Vigencia'][i]

		_modalidad = df['Modalidad'][i]

		## Si el cliente existe

		if Cliente.objects.filter(nombre=clien).count() > 0:

			#
			id_cliente = Cliente.objects.get(nombre=clien).id

		else:

			##

			Cliente(agente_id=age,nombre=clien,upload_ene_jul_2019_ecu=1,dni=dni).save()

			id_cliente=Cliente.objects.all().values('id').order_by('-id')[0]['id']


		print '_modalidad',_modalidad

		if _modalidad:

			_modalidad = _modalidad.capitalize()

		else:

			_modalidad = 'Anual'

		mo = Modalidad.objects.filter(nombre__contains=_modalidad)

		print _modalidad,mo

		if mo.count()>0:

			modalidaddato = mo[0].id

		else:

			print _modalidad


		fecha_poliza = datetime.datetime.strptime(fecha_poliza, '%d/%m/%Y')
		
		status = df['Estatus'][i]

		ss =Statuspoliza.objects.filter(nombre__contains=status)

		if ss.count()>0:

			es = ss[0].id

		else:

			es=1

		PropuestaCliente(cliente_id=id_cliente,ramo_compania_producto_id=rcp[0].id,agente_id=age,upload_csv_julio_enero_2019=1,fecha=fecha_poliza).save()

		id_propuesta=PropuestaCliente.objects.all().values('id').order_by('-id')[0]['id']

		Citas(tipo_cita_id=2,tipo_seguimiento_id=2,cliente_id=id_cliente,propuesta_cliente_id=id_propuesta,agente_id=age,numero_poliza=numero_poliza,fecha_poliza=fecha_poliza,status_poliza_id=es,cliente_antiguo='Yes',upload_ene_jul_2019_ecu=1,fecha_cita=fecha_poliza,modalidad_id=modalidaddato,asesor_anterior=asesor_anterior).save()

		Citas(tipo_cita_id=3,tipo_seguimiento_id=4,cliente_id=id_cliente,propuesta_cliente_id=id_propuesta,agente_id=age,numero_poliza=numero_poliza,fecha_poliza=fecha_poliza,status_poliza_id=es,cliente_antiguo='Yes',upload_ene_jul_2019_ecu=1,fecha_cita=fecha_poliza,modalidad_id=modalidaddato,asesor_anterior=asesor_anterior).save()


	print 'encontrados',len(todos)

	return HttpResponse('ok', content_type="application/json")



class Listacia(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,ramo):

		r=RamoCompaniaProducto.objects.filter(ramo_id=ramo).values('compania','compania__nombre').exclude(antiguo=1).annotate(c=Max('compania'))
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Listaproducto(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,ramo,cia):

		r=RamoCompaniaProducto.objects.filter(ramo_id=ramo,compania_id=cia).exclude(antiguo=1).values('id','producto','producto__nombre')
		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")


class Listapropuestas(JSONWebTokenAuthMixin, View):

	#Lista ramo cia producto
	def get(self, request,cliente):

		r=PropuestaCliente.objects.filter(cliente_id=cliente).values('id','cliente','agente','ramo_compania_producto__ramo__nombre','ramo_compania_producto__compania__nombre','ramo_compania_producto__producto__nombre')
		
		for j in range(len(r)):


			Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre').values('id',)

			if Citas.objects.filter(propuesta_cliente_id=r[j]['id'],tipo_seguimiento__nombre='Cierre'):

				r[j]['cierre']=1

			else:

				r[j]['cierre']=0


		r= simplejson.dumps(ValuesQuerySetToDict(r))
		return HttpResponse(r, content_type="application/json")
