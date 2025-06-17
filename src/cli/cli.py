from src.modelo.clinica import Clinica
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad
from src.modelo.exceptions import *
from datetime import datetime

class CLI:
    def __init__(self):
        self.clinica = Clinica()
    
    def mostrar_menu(self):
        print("\n" + "="*40)
        print("         CLÍNICA MÉDICA")
        print("="*40)
        print("1) Agregar paciente")
        print("2) Agregar médico")
        print("3) Agendar turno")
        print("4) Agregar especialidad")
        print("5) Emitir receta")
        print("6) Ver historia clínica")
        print("7) Ver todos los turnos")
        print("8) Ver todos los pacientes")
        print("9) Ver todos los médicos")
        print("0) Salir")
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
                    self.agregar_especialidad()
                elif opcion == "5":
                    self.emitir_receta()
                elif opcion == "6":
                    self.ver_historia_clinica()
                elif opcion == "7":
                    self.ver_turnos()
                elif opcion == "8":
                    self.ver_pacientes()
                elif opcion == "9":
                    self.ver_medicos()
                elif opcion == "0":
                    print("¡Hasta luego!")
                    break
                else:
                    print("Opción inválida")
            
            except (PacienteNoEncontradoException, MedicoNoDisponibleException, 
                    TurnoOcupadoException, RecetaInvalidaException) as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Error inesperado: {e}")
    
    def agregar_paciente(self):
        print("\n--- Agregar Paciente ---")
        nombre = input("Nombre completo: ")
        dni = input("DNI: ")
        fecha_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
        
        paciente = Paciente(nombre, dni, fecha_nacimiento)
        self.clinica.agregar_paciente(paciente)
    
    def agregar_medico(self):
        print("\n--- Agregar Médico ---")
        nombre = input("Nombre completo: ")
        matricula = input("Matrícula: ")
        
        medico = Medico(nombre, matricula)
        
        # Agregar especialidades
        while True:
            print("\nEspecialidades disponibles:")
            print("1. Pediatría")
            print("2. Cardiología") 
            print("3. Clínica Médica")
            print("4. Otra")
            print("0. No agregar más especialidades")
            
            opcion = input("Seleccione especialidad: ")
            
            if opcion == "0":
                break
            elif opcion == "1":
                dias = ["lunes", "miércoles", "viernes"]
                esp = Especialidad("Pediatría", dias)
            elif opcion == "2":
                dias = ["martes", "jueves"]
                esp = Especialidad("Cardiología", dias)
            elif opcion == "3":
                dias = ["lunes", "martes", "miércoles", "jueves", "viernes"]
                esp = Especialidad("Clínica Médica", dias)
            elif opcion == "4":
                tipo = input("Nombre de la especialidad: ")
                dias_str = input("Días de atención (separados por coma): ")
                dias = [dia.strip().lower() for dia in dias_str.split(",")]
                esp = Especialidad(tipo, dias)
            else:
                print("Opción inválida")
                continue
            
            medico.agregar_especialidad(esp)
            print(f"Especialidad {esp.obtener_especialidad()} agregada")
        
        self.clinica.agregar_medico(medico)
    
    def agendar_turno(self):
        print("\n--- Agendar Turno ---")
        dni = input("DNI del paciente: ")
        matricula = input("Matrícula del médico: ")
        especialidad = input("Especialidad: ")
        
        # Solicitar fecha y hora
        fecha_str = input("Fecha (dd/mm/aaaa): ")
        hora_str = input("Hora (HH:MM): ")
        
        # Convertir a datetime
        try:
            fecha_hora_str = f"{fecha_str} {hora_str}"
            fecha_hora = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
        except ValueError:
            print("Formato de fecha u hora inválido")
            return
        
        self.clinica.agendar_turno(dni, matricula, especialidad, fecha_hora)
    
    def agregar_especialidad(self):
        print("\n--- Agregar Especialidad a Médico ---")
        matricula = input("Matrícula del médico: ")
        
        try:
            medico = self.clinica.obtener_medico_por_matricula(matricula)
            
            tipo = input("Nombre de la especialidad: ")
            dias_str = input("Días de atención (separados por coma): ")
            dias = [dia.strip().lower() for dia in dias_str.split(",")]
            
            especialidad = Especialidad(tipo, dias)
            medico.agregar_especialidad(especialidad)
            
            print(f"Especialidad {tipo} agregada al médico {medico}")
            
        except Exception as e:
            print(f"Error: {e}")
    
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
        if not pacientes:
            print("No hay pacientes registrados")
        else:
            for paciente in pacientes:
                print(f"- {paciente}")
    
    def ver_medicos(self):
        print("\n--- Todos los Médicos ---")
        medicos = self.clinica.obtener_medicos()
        if not medicos:
            print("No hay médicos registrados")
        else:
            for medico in medicos:
                print(f"- {medico}")
    
    def ver_turnos(self):
        print("\n--- Todos los Turnos ---")
        turnos = self.clinica.obtener_turnos()
        if not turnos:
            print("No hay turnos agendados")
        else:
            for turno in turnos:
                print(f"- {turno}")