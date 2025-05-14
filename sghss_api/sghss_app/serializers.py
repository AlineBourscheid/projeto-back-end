from rest_framework import serializers
from .models import Paciente
from .models import Profissional
from .models import AgendamentoConsulta
from .models import Prontuario

class PacienteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Paciente
        fields = '__all__'

class ProfissionalSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profissional
        fields = '__all__'

class AgendamentoConsultaSerializer(serializers.ModelSerializer):

    class Meta:

        model = AgendamentoConsulta
        fields = '__all__'

class ProntuarioSerializer(serializers.ModelSerializer):

    class Meta:

        model = Prontuario
        fields = '__all__'
