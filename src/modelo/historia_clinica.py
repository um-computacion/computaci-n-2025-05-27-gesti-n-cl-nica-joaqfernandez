from src.modelo.paciente import Paciente
from src.modelo.turno import Turno
from src.modelo.receta import Receta

class HistoriaClinica:
    def __init__(self, paciente: Paciente):
        if not isinstance(paciente, Paciente):
            raise ValueError("El paciente debe ser una instancia de la clase Paciente")
        
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []
    
    def agregar_turno(self, turno: Turno):
        if not isinstance(turno, Turno):
            raise ValueError("El turno debe ser una instancia de la clase Turno")
        self.__turnos.append(turno)

    def agregar_receta(self, receta: Receta):
        if not isinstance(receta, Receta):
            raise ValueError("La receta debe ser una instancia de la clase Receta")
        self.__recetas.append(receta)

    def obtener_turnos(self) -> list[Turno]:
        return self.__turnos.copy()

    def obtener_recetas(self) -> list[Receta]:
        return self.__recetas.copy()

    def __str__(self) -> str:
        turnos_str = "\n".join(f"  - {turno}" for turno in self.__turnos) if self.__turnos else "  - No hay turnos"
        recetas_str = "\n".join(f"  - {receta}" for receta in self.__recetas) if self.__recetas else "  - No hay recetas"
        return f"HistoriaClinica({self.__paciente},\nTurnos:\n{turnos_str}\nRecetas:\n{recetas_str})"