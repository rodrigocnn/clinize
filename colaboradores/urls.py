
from django.urls import path

from colaboradores.views import index, create, store, edit, update, delete

urlpatterns = [
    path('', index, name="colaboradores_home"),
    path('create', create, name="colaborador_create"),
    path('store', store, name="colaborador_store"),
    path('edit/<int:colaborador_id>', edit, name="colaborador_edit"),
    path('update', update, name="colaborador_update"),
    path('delete/<int:colaborador_id>', delete, name="colaborador_delete"),
]
