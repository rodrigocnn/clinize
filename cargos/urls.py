
from django.urls import path

from cargos.views import create, store, index, edit, update, delete

urlpatterns = [
    path('', index, name="cargos_home"),
    path('create', create, name="cargos_create"),
    path('store', store, name="cargos_store"),
    path('edit/<int:cargo_id>', edit, name="cargos_edit"),
    path('update', update, name="cargos_update"),
    path('delete/<int:cargo_id>', delete, name="cargos_delete"),
]
