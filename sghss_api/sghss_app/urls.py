from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^paciente/$', views.PacienteList.as_view(), name='paciente-list'),
    re_path(r'^profissional/$', views.ProfissionalList.as_view(), name='profissional-list'),
    re_path(r'^agendamentoconsulta/$', views.AgendamentoConsultaList.as_view(), name='agendamentoconsulta-list'),
    re_path(r'^prontuario/$', views.ProntuarioList.as_view(), name='prontuario-list'),
    path('paciente/<int:pk>/', views.PacienteDetail.as_view(), name='paciente-detail'),
    path('profissional/<int:pk>/', views.ProfissionalDetail.as_view(), name='profissional-detail'),
    path('agendamentoconsulta/<int:pk>/', views.AgendamentoConsultaDetail.as_view(), name='agendamentoconsulta-detail'),
    path('prontuario/<int:pk>/', views.ProntuarioDetail.as_view(), name='prontuario-detail'),
    re_path(r'^signup/$', views.UserCreateView.as_view(), name='signup'),

]
