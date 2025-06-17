import unittest
from src.modelo.receta import Receta
from src.modelo.medico import Medico
from src.modelo.paciente import Paciente
from src.modelo.especialidad import Especialidad
from datetime import datetime



class testTurno(unittest.TestCase):
    def setUp(self):
        self.__e__ = Especialidad("Pediatría", ["Lunes", "Martes"])
        self.__doc__ = Medico("Marcela", "Leuzzi", 56643128, 2145, [self.__e__])
        self.__pac__ = Paciente("Joaquin", "Fernandez", 21, 423312351)
       

    def test_Receta(self):
        rec = Receta(self.__pac__, self.__doc__, "Ibuprofeno 8mg")
        self.assertEqual(rec.medicamentos, "Ibuprofeno 8mg")

        self.assertEqual(rec.fecha, datetime.now().date()) 



if __name__ == '__main__':
    unittest.main()