from src.modelo.especialidad import Especialidad
from typing import Optional


class Medico:
    def __init__(self, nombre: str, matricula: str, especialidades: list = None):
        # Validaciones
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not matricula or not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía")
        
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = especialidades if especialidades else []

    def agregar_especialidad(self, especialidad: Especialidad):
        # Validar que no exista ya la especialidad
        for esp in self.__especialidades:
            if esp.obtener_especialidad() == especialidad.obtener_especialidad():
                raise ValueError(f"La especialidad {especialidad.obtener_especialidad()} ya existe para este médico")
        
        self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> Optional[str]:
        dia_lower = dia.lower()
        for especialidad in self.__especialidades:
            if especialidad.verificar_dia(dia_lower):
                return especialidad.obtener_especialidad()
        return None

    def __str__(self) -> str:
        especialidades_str = ", ".join([f"{esp.obtener_especialidad()} (Días: {', '.join(esp._Especialidad__dias)})" 
                                       for esp in self.__especialidades])
        return f"{self.__nombre}, {self.__matricula}, [{especialidades_str}]"