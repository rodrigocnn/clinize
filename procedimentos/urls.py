
from django.urls import path

from procedimentos.views import index, create, store, edit, update, delete

urlpatterns = [
    path('', index, name="procedimentos_home"),
    path('create', create, name="procedimento_create"),
    path('store', store, name="procedimento_store"),
    path('edit/<int:procedimento_id>', edit, name="procedimento_edit"),
    path('update', update, name="procedimento_update"),
    path('delete/<int:procedimento_id>', delete, name="procedimento_delete"),
]
