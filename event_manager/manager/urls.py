from django.urls import path
from . import views

urlpatterns = [
    path ("", views.index, name="index"),
    path("cadastro", views.cadastro, name="cadastro"),
    path("cadastro_sala", views.cadastro_sala, name="cadastro_sala"),
    path("cadastro_cafe", views.cadastro_cafe, name="cadastro_cafe"),
    path("consulta", views.consulta, name="consulta")
] 