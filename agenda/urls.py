
from django.urls import path

from agenda.views import index, create, store

urlpatterns = [
    path('', index, name="agenda_home"),
    path('create', create, name="agenda_create"),
    path('store', store, name="agenda_store"),
]
