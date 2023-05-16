
from django.urls import path
from app_cad_usuarios import views


urlpatterns = [
    # rota, view resposável, nome de referencia
    #criar links. o que vem após o a / final EX:path('aps') youtube.com/aps
    path('',views.home, name='home'), 

    path('usuarios/',views.usuarios, name='listagem_usuarios'),

    path('usuarios/',views.deletar, name='listagem_usuarios')
]
