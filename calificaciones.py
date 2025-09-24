class RegistroAlumnos:
    def __init__(self):
        self.nombres = []
        self.calificaciones = []
        self.promedio_grupal = 0
        self.alumnos_destacados = []

    def leer_datos(self):
        print("Ingrese los nombres y calificaciones de 10 alumnos:")
        for i in range(10):
            nombre_alumno = input("Nombre del alumno: ")
            calificacion_alumno = float(input("Calificación del alumno: "))
            self.nombres.append(nombre_alumno)
            self.calificaciones.append(calificacion_alumno)

    def procesar_datos(self):
        self.promedio_grupal = sum(self.calificaciones) / len(self.calificaciones)
        self.alumnos_destacados = []
        for indice in range(len(self.calificaciones)):
            if self.calificaciones[indice] > 9.5:
                self.alumnos_destacados.append(self.nombres[indice])

    def imprimir_resultados(self):
        print("--- Resultados ---")
        print("Promedio grupal:", self.promedio_grupal)
        if self.alumnos_destacados:
            print("Alumnos con calificación mayor a 9.5:")
            for alumno in self.alumnos_destacados:
                print(alumno)
        else:
            print("No hay alumnos con calificación mayor a 9.5.")

registro = RegistroAlumnos()
registro.leer_datos()
registro.procesar_datos()
registro.imprimir_resultados()
