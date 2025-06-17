# Excepciones requeridas por la consigna
class PacienteNoEncontradoException(Exception):
    """Excepción lanzada cuando no se encuentra un paciente"""
    pass

class MedicoNoDisponibleException(Exception):
    """Excepción lanzada cuando un médico no está disponible"""
    pass

class TurnoOcupadoException(Exception):
    """Excepción lanzada cuando se intenta agendar un turno ya ocupado"""
    pass

class RecetaInvalidaException(Exception):
    """Excepción lanzada cuando una receta es inválida"""
    pass

# Excepciones adicionales para el funcionamiento
class TurnoOcupado(Exception):
    pass

class EspecialidadNoEncontrada(Exception):
    pass

class DiaNoDisponible(Exception):
    pass

class PacienteNoEncontrado(Exception):
    pass