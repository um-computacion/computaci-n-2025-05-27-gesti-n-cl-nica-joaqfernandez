import unittest
from modelo.especialidad import Especialidad
from modelo.exceptions import EspecialidadNoEncontrada

class TestEspecialidad(unittest.TestCase):
    def especialidad_disponible(self):
        e = Especialidad("Pediatra", ["lunes", "martes", "viernes"])
        self.assertEqual(e.tipo, "Pediatra")
        self.assertEqual(e.dia, ["lunes", "martes", "viernes"]) 