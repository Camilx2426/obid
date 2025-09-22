class Triangulo:
    def _init_(self):
        self.base = 0
        self.altura = 0
        self.area = 0

    def leer_datos(self):
        self.base = float(input("Ingresa la base del triángulo: "))
        self.altura = float(input("Ingresa la altura del triángulo: "))

    def calcular_area(self):
        self.area = (self.base * self.altura) / 2

    def imprimir_datos(self):
        print("\nDatos del triángulo:")
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.area}")

triangulo = Triangulo()

triangulo.leer_datos()
triangulo.calcular_area()
triangulo.imprimir_datos()