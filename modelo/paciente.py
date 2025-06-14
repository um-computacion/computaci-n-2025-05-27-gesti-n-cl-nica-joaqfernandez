class Paciente:
    def __init__(self, nombre, apellido, edad, dni, ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def __str__(self):
        return f"{self.nombre} {self.apellido}, EDAD: {self.edad} DNI: {self.dni}"
