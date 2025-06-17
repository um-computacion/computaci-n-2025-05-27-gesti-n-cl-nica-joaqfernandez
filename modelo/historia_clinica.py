class HistoriaClinica:
    def __init__(self, paciente):
        self.paciente = paciente
        self.turnos = []
        self.receta = []
    
    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def agregar_receta(self, receta):
        self.receta.append(receta)

    def ver_turno(self, turno):
        return self.turno.copy()

    def ver_receta(self):
        return self.receta.copy()

    def __str__(self):
        turnos_str = "\n".join(f" - {turno}" for turno in self.turnos)
        receta_str = "\n".join(f" - {receta}" for receta in {self.receta})
        return f"Historia clinica del paciente {self.paciente}.: \nTurnos:\n{turnos_str}: \nRecetas:\n{receta_str}"