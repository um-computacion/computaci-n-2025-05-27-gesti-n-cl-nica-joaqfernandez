class Medico():
    def __init__(self, nombre, apellido, dni, matricula):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.matricula = matricula

    def __str__(self):
        return f"{self.nombre} {self.apellido}, MATRICULA: {self.matricula} DNI: {self.dni}"
    