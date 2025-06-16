from modelo.exceptions import DiaNoDisponible

class Especialidad():
    def __init__(self, nombre: str, dia: list[str]):
        self.nombre = nombre
        self.dia = dia

    def verificar_disponible(self, dia: str) -> bool:
        if dia not in self.dia:
            raise DiaNoDisponible(
                f"{self.nombre} no atiende los dias {dia}"
            )
        return True