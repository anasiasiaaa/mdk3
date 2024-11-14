import math

class Circle:


    def __init__(self, radius):
       #инициализирует круг с заданным радиусом
        self.radius = radius

    def get_perimeter(self):
       #ычисляет периметр круга
        return round(2 * math.pi * self.radius, 2)

    def get_area(self):
       
        #вычисляет площадь круга
        return round(math.pi * self.radius * self.radius, 2)
try:
        # Создаем два объекта класса "Круг"
    a = int(input("Введите радиус первого круга: "))
    b = int(input("Введите радиус второго круга: "))
    circle1 = Circle(a) # Создаем круг с радиусом 5
    circle2 = Circle(b) # Создаем круг с радиусом 3

    # Выводим площадь первого круга
    print("Площадь первого круга:", circle1.get_area())

    # Выводим периметр и площадь второго круга
    print("Периметр второго круга:", circle2.get_perimeter())
    print("Площадь второго круга:", circle2.get_area())
except ValueError:
    print("Введите корректные значения")
