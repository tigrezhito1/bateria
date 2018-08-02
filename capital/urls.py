
from django.conf.urls import patterns, include, url

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from app.views import *

from django.contrib import admin


admin.site.site_header = 'Baterias al Toque'
from app.admin import admin_site

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', 'jwt_auth.views.obtain_jwt_token'),
    url(r'^pos/', admin_site.urls),
    url(r'api-token-refresh/', refresh_jwt_token),
    url(r'^login/', 'views.login2'),
    url(r'^agente/$', Agenterest.as_view()),
    url(r'^userfono/$', Userfono.as_view()),
    url(r'^creacliente/$', Creacliente.as_view()),
    url(r'^creapropuesta/$', Creapropuesta.as_view()),
    url(r'^listaramos/$', Listaramos.as_view()),
    url(r'^listacia/(\d+)$', Listacia.as_view()),
    url(r'^listaproducto/(\d+)/(\d+)$', Listaproducto.as_view()),
    url(r'^listapropuestas/(\d+)$', Listapropuestas.as_view()),
    url(r'^cliente/(\d+)$', Listacliente.as_view()),
    url(r'^clientes/$', TodosClientes.as_view()),
    url(r'^detallepropuesta/(\d+)$', Detallepropuesta.as_view()),
    url(r'^creacita/$', Creacita.as_view()),
    url(r'^citasagente/$', Citasagente.as_view()),
    url(r'^creacitaequipo/$', Creacitaequipo.as_view()),
    url(r'^iconos/$', IconosLista.as_view()),
    url(r'^termometro/$', Termometro.as_view()),
    url(r'^metricas/(\d+)/(\d+)/(\d+)/(\d+)$', Metricas.as_view()),
    url(r'^modalidad/$', ListaModalidad.as_view()),
    url(r'^pariente/$', CreaPariente.as_view()),
    url(r'^gestion/$', MiGestion.as_view()),
    url(r'^gestionequipo/$', MiGestionequipo.as_view()),
    url(r'^updatecita/$', Updatecita.as_view()),
    url(r'^updatepropuesta/$', Updatepropuesta.as_view()),
    url(r'^resumen/$', Resumen.as_view()),
    url(r'^creapos/$', Creapos.as_view()),
    url(r'^semanas/$', Semanasall.as_view()),
    url(r'^calculo/(\d+)$', Calculo.as_view()),
    url(r'^calculomes/$', Calculomes.as_view()),
    url(r'^calculacitas/(\d+)$', Calculacitas.as_view()),
    url(r'^agentesequipo/$', Agentesequipo.as_view()),
    url(r'^calculoanio/(\d+)$', Calculoanio.as_view()),
    url(r'^losarchivos/$', Losarchivos.as_view()),
    url(r'^uploadphoto/', Uploadphoto.as_view()),
    url(r'^eliminapropuesta/(\d+)', Eliminarpropuesta.as_view()),
    url(r'^eliminarcita/(\d+)', Eliminarcita.as_view()),
    url(r'^calculapropuestasporramo/', Calculapropuestasporramo.as_view()),
    url(r'^calculaproduccionporramo/', Calculaproduccionporramo.as_view()),
    url(r'^calculaproduccionporramoequipo/', Calculaproduccionporramoequipo.as_view()),
    url(r'^version/(\d+)', Version.as_view()),
    url(r'^guardanoti$', Guardanoti.as_view()),
    url(r'^asignamovil/(\d+)$', Asignamovil.as_view()),
    url(r'^verificaversion/$', Verificaversion.as_view()),
    url(r'^sacareportegerente$', Sacareportegerente.as_view()),
    url(r'^buscaarchivos$', Buscaarchivos.as_view()),
    url(r'^eliminacliente$', Eliminacliente.as_view()),
    url(r'^sacareportecliente/$', Sacareportecitas.as_view()),
    url(r'^sacareporteclientereal/$', Sacareporteclientereal.as_view()),
    url(r'^sacareportepropuestas/$', Sacareportepropuestas.as_view()),
    url(r'^sacareportepos/$', Sacareportepos.as_view()),
    url(r'^semanasresumen/$', Semanasresumen.as_view()),
    url(r'^subirarchivo/$', 'app.views.subirarchivo'),
    url(r'^subire/$', 'app.views.subire'),
    url(r'^asignanotificacion/$', 'app.views.asignanotificacion'),
    
    #url(r'^enviasms$', Enviasms.as_view()),

]
