from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.turno import Turnos
from modelo.receta import Receta
from modelo.historia_clinica import HistoriaClinica
from modelo.especialidad import Especialidad
from modelo.exceptions import *
from datetime import datetime

class Clinica:
    def __init__(self):
        self.pacientes = {}  # DNI -> Paciente
        self.medicos = {}    # Matricula -> Medico
        self.turnos = []
        self.historias_clinicas = {}  # DNI -> HistoriaClinica
    
    def agregar_paciente(self, paciente):
        if paciente.dni in self.pacientes:
            raise Exception(f"Paciente con DNI {paciente.dni} ya existe")
        
        self.pacientes[paciente.dni] = paciente
        self.historias_clinicas[paciente.dni] = HistoriaClinica(paciente)
        print(f"Paciente {paciente.nombre} {paciente.apellido} registrado exitosamente")
    
    def agregar_medico(self, medico):
        if medico.matricula in self.medicos:
            raise Exception(f"Médico con matrícula {medico.matricula} ya existe")
        
        self.medicos[medico.matricula] = medico
        print(f"Médico {medico.nombre} {medico.apellido} registrado exitosamente")
    
    def agendar_turno(self, dni, matricula, especialidad, dia, hora):
        # Validar que paciente existe
        if dni not in self.pacientes:
            raise PacienteNoEncontrado(f"Paciente con DNI {dni} no encontrado")
        
        # Validar que médico existe
        if matricula not in self.medicos:
            raise Exception(f"Médico con matrícula {matricula} no encontrado")
        
        paciente = self.pacientes[dni]
        medico = self.medicos[matricula]
        
        # Crear el turno (esto ya valida disponibilidad)
        turno = Turnos(paciente, especialidad, medico, dia, hora)
        
        # Agregar a la lista de turnos y historia clínica
        self.turnos.append(turno)
        self.historias_clinicas[dni].agregar_turno(turno)
        
        print(f"Turno agendado: {paciente.nombre} con {medico.nombre} el {dia} a las {hora}")
        return turno
    
    def emitir_receta(self, dni, matricula, medicamentos):
        # Validar que paciente y médico existen
        if dni not in self.pacientes:
            raise PacienteNoEncontrado(f"Paciente con DNI {dni} no encontrado")
        
        if matricula not in self.medicos:
            raise Exception(f"Médico con matrícula {matricula} no encontrado")
        
        if not medicamentos:
            raise Exception("Debe especificar al menos un medicamento")
        
        paciente = self.pacientes[dni]
        medico = self.medicos[matricula]
        
        # Crear y agregar receta
        receta = Receta(paciente, medico, medicamentos)
        self.historias_clinicas[dni].agregar_receta(receta)
        
        print(f"Receta emitida para {paciente.nombre} {paciente.apellido}")
        return receta
    
    def obtener_pacientes(self):
        return list(self.pacientes.values())
    
    def obtener_medicos(self):
        return list(self.medicos.values())
    
    def obtener_turnos(self):
        return self.turnos.copy()
    
    def obtener_historia_clinica_por_dni(self, dni):
        if dni not in self.historias_clinicas:
            raise PacienteNoEncontrado(f"Paciente con DNI {dni} no encontrado")
        return self.historias_clinicas[dni]
    
    def obtener_medico_por_matricula(self, matricula):
        if matricula not in self.medicos:
            raise Exception(f"Médico con matrícula {matricula} no encontrado")
        return self.medicos[matricula]
    
    def validar_existencia_paciente(self, dni):
        return dni in self.pacientes
    
    def validar_existencia_medico(self, matricula):
        return matricula in self.medicos
