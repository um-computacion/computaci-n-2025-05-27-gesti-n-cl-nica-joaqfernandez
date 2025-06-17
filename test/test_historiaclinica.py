import unittest
from datetime import datetime
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.turno import Turno
from src.modelo.receta import Receta
from src.modelo.especialidad import Especialidad
from src.modelo.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Juan Pérez", "12345678", "12/12/2000")
        self.medico = Medico("Dr. García", "987654", [
            Especialidad("Pediatría", ["lunes", "miércoles"])
        ])
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        fecha = datetime(2025, 6, 18, 10, 0)
        turno = Turno(self.paciente, self.medico, fecha, "Pediatría")
        self.historia.agregar_turno(turno)
        self.assertIn(turno, self.historia.obtener_turnos())

    def test_agregar_receta(self):
        receta = Receta(self.paciente, self.medico, ["Ibuprofeno"])
        self.historia.agregar_receta(receta)
        self.assertIn(receta, self.historia.obtener_recetas())

    def test_str_historia_clinica(self):
        str_repr = str(self.historia)
        self.assertIn("HistoriaClinica(", str_repr)

if __name__ == "__main__":
    unittest.main()
