
from django.urls import path

from lancamentos.views import create, store, index, edit, update, delete

urlpatterns = [
    path('fluxo-de-caixa', index, name="fluxo_caixa_home"),
    path('fluxo-de-caixa/create', create, name="fluxo_caixa_create"),
    path('fluxo-de-caixa/store', store, name="fluxo_caixa_store"),
    path('fluxo-de-caixa/edit/<int:lancamento_id>', edit, name="fluxo_caixa_edit"),
    path('fluxo-de-caixa/update', update, name="fluxo_caixa_update"),
    path('fluxo-de-caixa/delete/<int:lancamento_id>', delete, name="fluxo_caixa_delete"),
]
