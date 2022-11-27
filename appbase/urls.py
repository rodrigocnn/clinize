
# from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from pacientes.urls import urlpatterns as url_pacientes
from lancamentos.urls import urlpatterns as url_lancamentos
from tipolancamentos.urls import urlpatterns as url_tipo_lancamentos
from usuarios.urls import urlpatterns as url_usuarios
from dashboard.urls import urlpatterns as url_dashboard
from colaboradores.urls import urlpatterns as url_colaboradores
from cargos.urls import urlpatterns as url_cargos
from agenda.urls import urlpatterns as url_agenda

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('usuarios/', include(url_usuarios)),
    path('pacientes/', include(url_pacientes)),
    path('lancamentos/', include(url_lancamentos)),
    path('tipo-lancamentos/', include(url_tipo_lancamentos)),
    path('dashboard/', include(url_dashboard)),
    path('colaboradores/', include(url_colaboradores)),
    path('cargos/', include(url_cargos)),
    path('agenda/', include(url_agenda))
]
