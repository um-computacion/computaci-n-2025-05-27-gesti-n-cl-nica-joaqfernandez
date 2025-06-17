import unittest
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad

class testMedico(unittest.TestCase):
    def test_medico(self):
        esp = Especialidad("Pediatra", ["Lunes", "Martes"])
        med = Medico("Marcela", "Leuzzi", 56643128, 2145, [esp])
        self.assertEqual(med.nombre, "Marcela")
        self.assertEqual(med.apellido, "Leuzzi")
        self.assertEqual(med.matricula, 2145)
        self.assertEqual(med.dni, 56643128)
        self.assertEqual(med.especialidades[0].nombre, "Pediatra")


if __name__ == '__main__':
    unittest.main()