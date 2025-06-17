from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.turno import Turno
from src.modelo.receta import Receta
from src.modelo.historia_clinica import HistoriaClinica
from src.modelo.especialidad import Especialidad
from src.modelo.exceptions import *
from datetime import datetime

class Clinica:
    def __init__(self):
        self.__pacientes = {}  # DNI -> Paciente
        self.__medicos = {}    # Matricula -> Medico
        self.__turnos = []
        self.__historias_clinicas = {}  # DNI -> HistoriaClinica
    
    def agregar_paciente(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise ValueError("Debe ser una instancia de Paciente")
        
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise ValueError(f"Paciente con DNI {dni} ya existe")
        
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)
        print(f"Paciente {paciente} registrado exitosamente")
    
    def agregar_medico(self, medico: Medico):
        if not isinstance(medico, Medico):
            raise ValueError("Debe ser una instancia de Medico")
        
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise ValueError(f"Médico con matrícula {matricula} ya existe")
        
        self.__medicos[matricula] = medico
        print(f"Médico {medico} registrado exitosamente")
    
    def agendar_turno(self, dni: str, matricula: str, especialidad: str, fecha_hora: datetime):
        # Validar existencia de paciente y médico
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        
        # Validar turno no duplicado
        self.validar_turno_no_duplicado(matricula, fecha_hora)
        
        # Validar que el médico atienda esa especialidad ese día
        dia_semana = self.obtener_dia_semana_en_espanol(fecha_hora)
        self.validar_especialidad_en_dia(medico, especialidad, dia_semana)
        
        # Crear el turno
        turno = Turno(paciente, medico, fecha_hora, especialidad)
        
        # Agregar a la lista de turnos y historia clínica
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)
        
        print(f"Turno agendado: {paciente} con {medico} el {fecha_hora} para {especialidad}")
        return turno
    
    def emitir_receta(self, dni: str, matricula: str, medicamentos: list[str]):
        # Validar existencia de paciente y médico
        self.validar_existencia_paciente(dni)
        self.validar_existencia_medico(matricula)
        
        if not medicamentos:
            raise RecetaInvalidaException("Debe especificar al menos un medicamento")
        
        paciente = self.__pacientes[dni]
        medico = self.__medicos[matricula]
        
        # Crear y agregar receta
        receta = Receta(paciente, medico, medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)
        
        print(f"Receta emitida para {paciente}")
        return receta
    
    def obtener_pacientes(self) -> list[Paciente]:
        return list(self.__pacientes.values())
    
    def obtener_medicos(self) -> list[Medico]:
        return list(self.__medicos.values())
    
    def obtener_medico_por_matricula(self, matricula: str) -> Medico:
        if matricula not in self.__medicos:
            raise PacienteNoEncontradoException(f"Médico con matrícula {matricula} no encontrado")
        return self.__medicos[matricula]
    
    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()
    
    def obtener_historia_clinica_por_dni(self, dni: str) -> HistoriaClinica:
        if dni not in self.__historias_clinicas:
            raise PacienteNoEncontradoException(f"Paciente con DNI {dni} no encontrado")
        return self.__historias_clinicas[dni]
    
    def validar_existencia_paciente(self, dni: str):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException(f"Paciente con DNI {dni} no encontrado")
        return True
    
    def validar_existencia_medico(self, matricula: str):
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException(f"Médico con matrícula {matricula} no encontrado")
        return True
    
    def validar_turno_no_duplicado(self, matricula: str, fecha_hora: datetime):
        for turno in self.__turnos:
            if (turno.obtener_medico().obtener_matricula() == matricula and 
                turno.obtener_fecha_hora() == fecha_hora):
                raise TurnoOcupadoException(f"El médico ya tiene un turno agendado para {fecha_hora}")
        return True
    
    def obtener_dia_semana_en_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]
    
    def obtener_especialidad_disponible(self, medico: Medico, dia_semana: str) -> str:
        return medico.obtener_especialidad_para_dia(dia_semana)
    
    def validar_especialidad_en_dia(self, medico: Medico, especialidad_solicitada: str, dia_semana: str):
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        
        if not especialidad_disponible:
            raise MedicoNoDisponibleException(f"El médico no atiende los {dia_semana}")
        
        if especialidad_disponible.lower() != especialidad_solicitada.lower():
            raise MedicoNoDisponibleException(f"El médico no atiende {especialidad_solicitada} los {dia_semana}")
        
        return True