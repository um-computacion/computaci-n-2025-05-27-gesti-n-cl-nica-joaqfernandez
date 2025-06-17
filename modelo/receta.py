from datetime import datetime
from modelo.paciente import Paciente
from modelo.medico import Medico

class Receta:
    def __init__(self, paciente: Paciente, medico: Medico, medicamentos: list[str]):
        # Validaciones
        if not isinstance(paciente, Paciente):
            raise ValueError("El paciente debe ser una instancia de la clase Paciente")
        if not isinstance(medico, Medico):
            raise ValueError("El médico debe ser una instancia de la clase Medico")
        if not medicamentos or len(medicamentos) == 0:
            raise ValueError("Debe especificar al menos un medicamento")
        
        # Validar que todos los medicamentos sean strings no vacíos
        for med in medicamentos:
            if not med or not med.strip():
                raise ValueError("Los medicamentos no pueden estar vacíos")
        
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self) -> str:
        medicamentos_str = ", ".join(self.__medicamentos)
        return f"Receta({self.__paciente}, {self.__medico}, [{medicamentos_str}], {self.__fecha})"