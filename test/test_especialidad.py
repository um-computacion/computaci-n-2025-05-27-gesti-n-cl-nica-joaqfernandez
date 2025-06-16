import unittest
from modelo.especialidad import Especialidad
from modelo.exceptions import EspecialidadNoEncontrada

class testEspecialidad(unittest.TestCase):
    def test_especialidad_disponible(self):
        e = Especialidad("Pediatra", ["lunes", "martes", "viernes"])
        self.assertEqual(e.nombre, "Pediatra")
        self.assertEqual(e.dia, ["lunes", "martes", "viernes"])


if __name__ == '__main__':
    unittest.main()