from rest_framework import generics
from .models import Paciente, Profissional, AgendamentoConsulta, Prontuario
from .serializers import (
    PacienteSerializer,
    ProfissionalSerializer,
    AgendamentoConsultaSerializer,
    ProntuarioSerializer
)
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.generic import FormView
from django.core import serializers

class UserCreateView(FormView):
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        serialized_data = serializers.serialize('json', [user])
        return JsonResponse({'status': 'success'}, status=201)

    def form_invalid(self, form):
         return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

# Create your views here. PUT e GET
class PacienteList(generics.ListCreateAPIView):

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ProfissionalList(generics.ListCreateAPIView):

    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class AgendamentoConsultaList(generics.ListCreateAPIView):

    queryset = AgendamentoConsulta.objects.all()
    serializer_class = AgendamentoConsultaSerializer

class ProntuarioList(generics.ListCreateAPIView):

    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer

# GET, PUT, PATCH e DELETE
class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ProfissionalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class AgendamentoConsultaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgendamentoConsulta.objects.all()
    serializer_class = AgendamentoConsultaSerializer

class ProntuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer


