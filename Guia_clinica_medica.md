# 📋 Sistema de Gestión para una Clínica

Este proyecto implementa un sistema de gestión para una clínica médica en Python, dividio en modulos, donde se encuenta las clases, la interfaz de consola (CLI) y las pruebas unitarias.


## ▶️ Ejecucion

Para ejecutar el proyecto, desde la raiz del proyecto:

```bash
  python3 main.py
```

## 🧪 Tests

Para ejecutar los tests, desde la raiz del proyecto:

```bash
python3 -m unittest discover -s src/test
```


## 📂 Estructura



    ClinicaFinal/
    ├── main.py              # Punto de entrada para ejecutar la CLI
    ├── README.md            # Documentación del proyecto
    ├── .gitignore           # Archivos/Directorios ignorados por Git
    └── src/
        ├── cli/
        │   └── cli.py       # Interfaz de consola (menú y manejo de entradas)
        ├── modelo/
        │   ├── __init__.py  # Convertir el directorio en paquete Python
        │   ├── clinica.py   # Clase principal que centraliza la lógica
        │   ├── paciente.py  # Modelo Paciente
        │   ├── medico.py    # Modelo Médico
        │   ├── especialidad.py  # Modelo Especialidad
        │   ├── turno.py     # Modelo Turno
        │   ├── receta.py    # Modelo Receta
        │   ├── historia_clinica.py  # Modelo HistoriaClinica
        │   └── exceptions.py  # Excepciones personalizadas
        └── test/
            ├── __init__.py
            ├── test_paciente.py
            ├── test_medico.py
            ├── test_especialidad.py
            ├── test_turno.py
            ├── test_receta.py
            ├── test_historiaclinica.py
            └── test_clinica.py
    



## 📂 Contacto
- Joaquin Fernandez Leuzzi

 - [Joaquin Fernandez (GitHub)](hhttps://github.com/joaqfernandez)
 - [Joaquin Fernandez (Mail institucional)](joal.fernandez@alumno.um.edu.ar)


