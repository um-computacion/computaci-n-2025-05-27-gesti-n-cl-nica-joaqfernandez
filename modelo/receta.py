from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        self.__paciente = paciente
        self.__medico = medico
        self. __medicamentos = medicamentos
        self.fecha = datetime.now()

    def __str___(self):
        return f"El paciente {self.__paciente}: se lo ha recetado para los medicamentos {self.__medicamentos}. Medico {self.__medico}"