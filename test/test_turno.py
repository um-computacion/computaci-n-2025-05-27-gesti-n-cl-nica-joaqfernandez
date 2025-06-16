import unittest
from modelo.turno import Turnos
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad
from modelo.exceptions import EspecialidadNoEncontrada, TurnoOcupado

class testTurnos(unittest.TestCase):
    def setUp(self):
        self.pac = Paciente("Joaquin", "Fernandez", 21, 423312351)
        self.e = Especialidad("Pediatría", ["Lunes", "Martes"])
        self.med = Medico("Marcela", "Leuzzi", 56643128, 2145, [self.e])
        Turnos.turnos_ocupados = [] 
        print(self.med.__dict__)


    def test_nuevo_turno(self):
        tur = Turnos(self.pac, self.e, self.med, "Lunes", "10:00")
        self.assertEqual(tur.dia, "Lunes")
        self.assertEqual(tur.hora, "10:00")

    def test_especialidad_dia_no_disponible(self):
        with self.assertRaises(EspecialidadNoEncontrada):
            Turnos(self.pac, self.e, self.med, "Miércoles", "12:00")

    def test_turno_ocupado(self):
        Turnos(self.pac, self.e, self.med, "Lunes", "10:00")
        with self.assertRaises(TurnoOcupado):
            Turnos(self.pac, self.e, self.med, "Lunes", "10:00")

if __name__ == '__main__':
    unittest.main()
