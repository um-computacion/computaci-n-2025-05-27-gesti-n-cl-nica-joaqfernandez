from modelo.especialidad import Especialidad

class Medico:
    def __init__(self, nombre, apellido, dni, matricula, especialidades):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.matricula = matricula
        self.especialidades = especialidades


    def __str__(self):
        return f"{self.nombre} {self.apellido}, MATRICULA: {self.matricula} DNI: {self.dni}"
    