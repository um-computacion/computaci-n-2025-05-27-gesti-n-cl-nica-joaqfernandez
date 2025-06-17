import unittest
from src.modelo.paciente import Paciente


class testPaciente(unittest.TestCase):
    def test_paciente(self):
        pac = Paciente("Joaquin", "Fernandez", 21, 423312351)
        self.assertEqual(pac.nombre, "Joaquin")
        self.assertEqual(pac.apellido, "Fernandez")
        self.assertEqual(pac.edad, 21)
        self.assertEqual(pac.dni, 423312351)

if __name__ == '__main__':
    unittest.main()