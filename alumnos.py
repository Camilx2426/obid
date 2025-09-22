class Alumno:
    def __init__(self, nombre, edad, peso, promedio):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.promedio = promedio

    def inscripcion(self):
        print("El alumno fue inscrito.")

    def asesorias(self):
        print("El alumno tiene acceso a asesorías.")

alumno1 = Alumno("Leo", 17, 65, 8.0)

alumno1.inscripcion()
alumno1.asesorias()
