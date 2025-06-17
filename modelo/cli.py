from modelo.clinica import Clinica
from modelo.paciente import Paciente
from modelo.medico import Medico
from modelo.especialidad import Especialidad

class CLI:
    def __init__(self):
        self.clinica = Clinica()
    
    def mostrar_menu(self):
        print("\n" + "="*40)
        print("         CLÍNICA MÉDICA")
        print("="*40)
        print("1. Agregar paciente")
        print("2. Agregar médico")
        print("3. Agendar turno")
        print("4. Emitir receta")
        print("5. Ver historia clínica")
        print("6. Ver todos los pacientes")
        print("7. Ver todos los médicos")
        print("8. Ver todos los turnos")
        print("0. Salir")
        print("="*40)
    
    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            
            try:
                if opcion == "1":
                    self.agregar_paciente()
                elif opcion == "2":
                    self.agregar_medico()
                elif opcion == "3":
                    self.agendar_turno()
                elif opcion == "4":
                    self.emitir_receta()
                elif opcion == "5":
                    self.ver_historia_clinica()
                elif opcion == "6":
                    self.ver_pacientes()
                elif opcion == "7":
                    self.ver_medicos()
                elif opcion == "8":
                    self.ver_turnos()
                elif opcion == "0":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida")
            
            except Exception as e:
                print(f"Error: {e}")
    
    def agregar_paciente(self):
        print("\n--- Agregar Paciente ---")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        dni = input("DNI: ")
        
        paciente = Paciente(nombre, apellido, edad, dni)
        self.clinica.agregar_paciente(paciente)
    
    def agregar_medico(self):
        print("\n--- Agregar Médico ---")
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        dni = input("DNI: ")
        matricula = input("Matrícula: ")
        
        # Especialidades básicas
        print("Especialidades disponibles:")
        print("1. Pediatría (Lunes, Miércoles, Viernes)")
        print("2. Cardiología (Martes, Jueves)")
        print("3. Clínica Médica (Lunes a Viernes)")
        
        opcion_esp = input("Seleccione especialidad (1-3): ")
        
        if opcion_esp == "1":
            esp = Especialidad("Pediatría", ["Lunes", "Miércoles", "Viernes"])
        elif opcion_esp == "2":
            esp = Especialidad("Cardiología", ["Martes", "Jueves"])
        else:
            esp = Especialidad("Clínica Médica", ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"])
        
        medico = Medico(nombre, apellido, dni, matricula, [esp])
        self.clinica.agregar_medico(medico)
    
    def agendar_turno(self):
        print("\n--- Agendar Turno ---")
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        especialidad = input("Especialidad: ")
        dia = input("Día (ej: Lunes): ")
        hora = input("Hora (ej: 10:00): ")
        
        self.clinica.agendar_turno(dni, matricula, especialidad, dia, hora)
    
    def emitir_receta(self):
        print("\n--- Emitir Receta ---")
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        medicamentos_str = input("Medicamentos (separados por coma): ")
        medicamentos = [med.strip() for med in medicamentos_str.split(",")]
        
        self.clinica.emitir_receta(dni, matricula, medicamentos)
    
    def ver_historia_clinica(self):
        print("\n--- Historia Clínica ---")
        dni = input("DNI del paciente: ")
        historia = self.clinica.obtener_historia_clinica_por_dni(dni)
        print(historia)
    
    def ver_pacientes(self):
        print("\n--- Todos los Pacientes ---")
        pacientes = self.clinica.obtener_pacientes()
        for paciente in pacientes:
            print(f"- {paciente}")
    
    def ver_medicos(self):
        print("\n--- Todos los Médicos ---")
        medicos = self.clinica.obtener_medicos()
        for medico in medicos:
            print(f"- {medico}")
    
    def ver_turnos(self):
        print("\n--- Todos los Turnos ---")
        turnos = self.clinica.obtener_turnos()
        for turno in turnos:
            print(f"- {turno}")
