class Transport:
    def __init__(self, transport_type, load_capacity):
        #запись типа транспорта и грузоподъемности
        self.transport_type = transport_type
        self.load_capacity = load_capacity

    def display_load_capacity(self):
        #вывод информации о грузоподъемности
        print(f"Грузоподъемность {self.transport_type}: {self.load_capacity} кг")


class Car(Transport):
    def __init__(self, load_capacity):
        #наследование класса через super
        super().__init__("Автомобиль", load_capacity)
        self.cargo_weight = 0  #начальный вес груза

    def add_cargo(self):
        #вывод грузоподъемности
        self.display_load_capacity()  

        while True:
            #запрос на ввод веса груза
            weight_input = input("Введите вес груза (кг) или оставьте поле пустым для завершения: ")
            
            #завершение программы при пустом вводе
            if weight_input.strip() == '':
                break  
            
            try:
                #преобразование введенного значения в целое число
                weight = int(weight_input)

                #проверка на отрицательное значение
                if weight < 0:
                    print("Вес не может быть отрицательным. Пожалуйста, введите корректное значение.")
                    continue

                #установка веса груза
                self.cargo_weight = weight

                while True:
                    increase = 10  #увеличение веса груза на 10 кг
                    consent = input(f"Хотите увеличить массу груза на {increase} кг? (да/нет): ").strip().lower()
                    
                    #если пользователь согласен, увеличиваем вес
                    if consent == 'да':
                        new_weight = self.cargo_weight + increase
                        #проверка на превышение грузоподъемности
                        if new_weight > self.load_capacity:
                            print("Превышение грузоподъемности! Текущий вес груза:", self.cargo_weight, "кг")
                            break
                        else:
                            self.cargo_weight = new_weight
                            print(f"Масса груза увеличена. Текущий вес груза: {self.cargo_weight} кг")
                    
                    #если пользователь не согласен, оставляем вес прежним
                    elif consent == 'нет':
                        print(f"Масса груза осталась прежней: {self.cargo_weight} кг")
                        break
                    
                    #обработка неверного ввода
                    else:
                        print("Неверный ввод. Пожалуйста, ответьте 'да' или 'нет'.")

            except ValueError:
                #обработка ошибки с весом
                print("Пожалуйста, введите корректный вес груза или оставьте поле пустым.")


def main():
    #запрос типа транспорта у пользователя
    transport_type = input("Введите тип транспорта (автомобиль, мотоцикл, катер): ").strip().lower()

    #проверка типа транспорта и занесение в класс транспорт
    if transport_type == "автомобиль":
        car = Car(load_capacity=500)#задание грузоподъености кжадому типу
        car.add_cargo()

    elif transport_type == "мотоцикл":
        motorcycle = Transport("Мотоцикл", load_capacity=200)
        motorcycle.display_load_capacity()

    elif transport_type == "катер":
        boat = Transport("Катер", load_capacity=350)
        boat.display_load_capacity()

    else:
        print("Неверный тип транспорта.")

if __name__ == "__main__":
    main()
