
from django.urls import path

from usuarios.views import index, create, store, edit, update, delete, login, logout

urlpatterns = [
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('', index, name="usuario_home"),
    path('create', create, name="usuario_create"),
    path('store', store, name="usuario_store"),
    path('edit/<int:usuario_id>', edit, name="usuario_edit"),
    path('update', update, name="usuario_update"),
    path('delete/<int:usuario_id>', delete, name="usuario_delete"),
]
