from modelo.exceptions import EspecialidadNoEncontrada, TurnoOcupado, DiaNoDisponible


class Turnos:
    turnos_ocupados = []

    def __init__(self, paciente, especialidad, medico, dia, hora):
        self.paciente = paciente
        self.especialidad = especialidad
        self.medico = medico
        self.dia = dia
        self.hora = hora
    
        especialidad_encontrada = False
    
        for e in medico.especialidades:
            # Verificar si atiende ese día
            try:
                e.verificar_disponible(dia)
                especialidad_encontrada = True
                break
            except DiaNoDisponible:
                continue
        
        if not especialidad_encontrada:
            raise EspecialidadNoEncontrada(f"El medico no atiende los dias {dia}")
        
        if (dia, hora) in Turnos.turnos_ocupados:
            raise TurnoOcupado(f"Turno ocupado el {dia}, a las {hora}")
        
        Turnos.turnos_ocupados.append((dia, hora))
