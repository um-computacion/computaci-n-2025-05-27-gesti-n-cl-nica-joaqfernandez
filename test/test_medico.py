import unittest
from modelo.medico import Medico

class testMedico(unittest.TestCase):
    def test_medico(self):
        med = Medico("Marcela", "Leuzzi", 56643128, 2145 )
        self.assertEqual(med.nombre, "Marcela")
        self.assertEqual(med.apellido, "Leuzzi")
        self.assertEqual(med.matricula, 2145)
        self.assertEqual(med.dni, 56643128)

if __name__ == '__main__':
    unittest.main()