
from django.db import models

# Create your models here.


class Paciente(models.Model):

    class Meta:

        db_table = 'Paciente'

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    

class Profissional(models.Model):

    class Meta:

        db_table = 'Profissional'

    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    registro_profissional = models.IntegerField()
    especialidade = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=200)
    
class AgendamentoConsulta(models.Model):

    class Meta:
 
        db_table = 'AgendamentoConsulta'

    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    
class Prontuario(models.Model):

    class Meta:

        db_table = 'Prontuario'

    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data_registro = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()



