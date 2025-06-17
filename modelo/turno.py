from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Turno:
    def __init__(self, paciente: Paciente, medico: Medico, fecha_hora: datetime, especialidad: str):
        # Validaciones
        if not isinstance(paciente, Paciente):
            raise ValueError("El paciente debe ser una instancia de la clase Paciente")
        if not isinstance(medico, Medico):
            raise ValueError("El médico debe ser una instancia de la clase Medico")
        if not isinstance(fecha_hora, datetime):
            raise ValueError("La fecha y hora debe ser un objeto datetime")
        if not especialidad or not especialidad.strip():
            raise ValueError("La especialidad no puede estar vacía")
        
        # Validar que el médico atienda esa especialidad ese día
        dia_semana = self._obtener_dia_semana_espanol(fecha_hora)
        especialidad_disponible = medico.obtener_especialidad_para_dia(dia_semana)
        
        if not especialidad_disponible:
            raise ValueError(f"El médico no atiende los {dia_semana}")
        
        if especialidad_disponible.lower() != especialidad.lower():
            raise ValueError(f"El médico no atiende {especialidad} los {dia_semana}")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self) -> Medico:
        return self.__medico

    def obtener_fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def _obtener_dia_semana_espanol(self, fecha_hora: datetime) -> str:
        dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        return dias[fecha_hora.weekday()]

    def __str__(self) -> str:
        return f"Turno({self.__paciente}, {self.__medico}, {self.__fecha_hora}, {self.__especialidad})"