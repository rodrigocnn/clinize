
from django.urls import path

from tipolancamentos.views import index, create, store, edit, update, delete

urlpatterns = [
    path('', index, name="tipo_lancamento_home"),
    path('create', create, name="tipo_lancamento_create"),
    path('store', store, name="tipo_lancamento_store"),
    path('edit/<int:lancamento_id>', edit, name="tipo_lancamento_edit"),
    path('update', update, name="tipo_lancamento_update"),
    path('delete/<int:lancamento_id>', delete, name="tipo_lancamento_delete"),

]
