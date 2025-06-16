from datetime import datetime

class Receta:
    

    def __init__(self, paciente, medico, medicamentos):
        self.paciente = paciente
        self.medico = medico
        self.medicamentos = medicamentos
        self.fecha = datetime.now().date()

    def __str___(self):
        return f"El paciente {self.paciente}: se lo ha recetado para los medicamentos {self.medicamentos}. Medico {self.medico}. {self.fecha}"