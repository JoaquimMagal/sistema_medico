from django.contrib import admin
from intranet import models

@admin.register(models.Medico) # Registrando a classe Médico do Portal do python
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'especialidade','ativo')

@admin.register(models.Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'ativo',)

@admin.register(models.Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente_id', 'medico_id', 'status',)