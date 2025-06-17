import unittest
from src.modelo.clinica import Clinica
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad


class testClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Juan", "Pérez", 30, "12345678")
        self.especialidad = Especialidad("Pediatría", ["Lunes", "Miércoles"])
        self.medico = Medico("Dr. García", "López", "87654321", "MED001", [self.especialidad])

    def test_agregar_paciente(self):
        self.clinica.agregar_paciente(self.paciente)
        self.assertTrue(self.clinica.validar_existencia_paciente("12345678"))

    def test_agregar_medico(self):
        self.clinica.agregar_medico(self.medico)
        self.assertTrue(self.clinica.validar_existencia_medico("MED001"))
    
    def test_agendar_turno(self):
        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)
        
        turno = self.clinica.agendar_turno("12345678", "MED001", "Pediatría", "Lunes", "10:00")
        self.assertIsNotNone(turno)
        self.assertEqual(len(self.clinica.obtener_turnos()), 1)



if __name__ == '__main__':
    unittest.main()