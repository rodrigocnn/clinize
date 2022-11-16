
from django.urls import path

from colaboradores.views import index, create, store, edit, update, delete

urlpatterns = [
    path('', index, name="colaborares_home"),
    path('create', create),
    path('store', store, name="colaborador_store"),
    path('edit/<int:paciente_id>', edit, name="colaborador_edit"),
    path('update', update, name="colaborador_update"),
    path('delete/<int:paciente_id>', delete, name="colaborador_delete"),
]
