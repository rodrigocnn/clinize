
from django.urls import path

from pacientes.views import index, create, store, edit, update, delete

urlpatterns = [
    path('', index, name="pacientes_home"),
    path('create', create),
    path('store', store, name="paciente_store"),
    path('edit/<int:paciente_id>', edit, name="paciente_edit"),
    path('update', update, name="paciente_update"),
    path('delete/<int:paciente_id>', delete, name="paciente_delete"),
]
