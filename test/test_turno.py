import unittest
from modelo.turno import Turnos
from modelo.medico import Medico
from modelo.paciente import Paciente
from modelo.especialidad import Especialidad
from modelo.exceptions import EspecialidadNoEncontrada, TurnoOcupado


class testTurnos(unittest.TestCase):
    def setUp(self):
        self.pac = Paciente("Joaquin", "Fernandez", 21, 423312351)
        self.e = Especialidad("Pediatra", ["lunes", "martes", "viernes"])
        self.med = Medico("Marcela", "Leuzzi", 56643128, 2145, self.e)
    
    def test_nuevo_turno(self):
        tur = Turnos(self.pac, self.med, "Lunes", "10:00")
        self.assertEqual(tur.dia, "Lunes")
        self.assertEqual(tur.hora, "10:00")
    
    def test_especialidad_dia_no_disponible(self):
        with self.assertRaises(EspecialidadNoEncontrada):
            Turnos(self.pac, self.med, "Miercoles", "12:00")

    def test_turno_ocupado(self):
        Turnos.turnos_ocupados = []
        with self.assertRaises(TurnoOcupado):
            Turnos(self.pac, self.med, "Lunes", "10:00")



if __name__ == '__main__':
    unittest.main()