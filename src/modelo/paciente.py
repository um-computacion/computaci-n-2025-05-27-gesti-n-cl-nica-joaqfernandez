class Paciente:
    def __init__(self, nombre: str, dni: str, fecha_nacimiento: str):
        # Validaciones
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not dni or not dni.strip():
            raise ValueError("El DNI no puede estar vacío")
        if not fecha_nacimiento or not fecha_nacimiento.strip():
            raise ValueError("La fecha de nacimiento no puede estar vacía")
        
        # Validar formato de fecha dd/mm/aaaa
        try:
            partes = fecha_nacimiento.split('/')
            if len(partes) != 3:
                raise ValueError("Formato de fecha inválido. Use dd/mm/aaaa")
            dia, mes, año = map(int, partes)
            if dia < 1 or dia > 31 or mes < 1 or mes > 12 or año < 1900:
                raise ValueError("Fecha inválida")
        except ValueError as e:
            if "invalid literal" in str(e):
                raise ValueError("Formato de fecha inválido. Use dd/mm/aaaa")
            raise e
        
        self.__nombre = nombre
        self.__dni = dni
        self.__fecha_nacimiento = fecha_nacimiento

    def obtener_dni(self) -> str:
        return self.__dni

    def __str__(self) -> str:
        return f"{self.__nombre}, {self.__dni}, {self.__fecha_nacimiento}"