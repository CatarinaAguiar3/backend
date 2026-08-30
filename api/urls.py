from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health_check, name="health_check"),
    path("chat/", views.chat_endpoint, name="chat_endpoint"),
    path("alunos/", views.alunos_collection, name="alunos_collection"),
    path("alunos/<str:nome>/", views.aluno_detail, name="aluno_detail"),
    path("media-idade/", views.alunos_media_idade, name="alunos_media_idade"),
    path("contagem-alunos/", views.alunos_contagem, name="alunos_contagem"),
    path("professores/", views.professores_collection, name="professores_collection"),
    path("professores/<str:nome>/", views.professor_detail, name="professor_detail"),
    path("media-idade-professores/", views.professores_media_idade, name="professores_media_idade"),
    path("contagem-professores/", views.professores_contagem, name="professores_contagem"),
]
