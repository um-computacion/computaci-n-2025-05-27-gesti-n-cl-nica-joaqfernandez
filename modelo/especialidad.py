from modelo.exceptions import DiaNoDisponible

class Especialidad():
    def __init__(self, tipo: str, dia: list[str]):
        self.tipo = tipo
        self.dia = dia

    def verificar_dia_disponible(self, dia: str) -> bool:
        if dia not in self.dia:
            raise DiaNoDisponible(
                f"{self.tipo} no atiende los dias {dia}"
            )
        return True