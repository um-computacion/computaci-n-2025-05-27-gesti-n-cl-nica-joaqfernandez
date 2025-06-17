class Especialidad:
    def __init__(self, tipo: str, dias: list[str]):
        # Validaciones
        if not tipo or not tipo.strip():
            raise ValueError("El tipo de especialidad no puede estar vacío")
        if not dias or len(dias) == 0:
            raise ValueError("Debe especificar al menos un día de atención")
        
        # Validar que los días sean válidos
        dias_validos = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
        for dia in dias:
            if dia.lower() not in dias_validos:
                raise ValueError(f"Día inválido: {dia}. Días válidos: {', '.join(dias_validos)}")
        
        self.__tipo = tipo
        self.__dias = [dia.lower() for dia in dias]  # Convertir a minúsculas

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return dia.lower() in self.__dias

    def __str__(self) -> str:
        return f"{self.__tipo} (Días: {', '.join(self.__dias)})"