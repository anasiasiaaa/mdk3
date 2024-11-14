class Sale:
    def __init__(self, product_type):
        #добавление вида товара и списка сумм продаж
        self.product_type = product_type
        self.monthly_sales = []

    def set_monthly_sales(self, sales):
        #установка значений сумм продаж за 6 месяцев
        if len(sales) != 6:
            raise ValueError("Необходимо ввести 6 значений продаж")
        self.monthly_sales = sales

    def best_month(self):
        #определение самого удачного месяца
        max_sales = max(self.monthly_sales)
        #получение индекса месяца из самой большой прибыли
        month_index = self.monthly_sales.index(max_sales)

        #cписок названий месяцев
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"]
        return f"Самый удачный месяц: {months[month_index]}, Сумма продаж: {max_sales} руб."

    def display_info(self):
        #вывод информации о продаже
        print(f"Вид товара: {self.product_type}")
        print("Суммы продаж за 6 месяцев:", self.monthly_sales)


def main():
    try:
        tech_sale = Sale("Техника")
        b = input("Введите 6 значений продаж в категории Техника через пробел: ")
        a = [float(x) for x in b.split()] 
        if len(a)!= 6:
            print("Введите значения за 6 месяцев через пробел")
            return

        #проверяем, есть ли значения меньше 0
        if any(value < 0 for value in a):
            print("Введите положительные значения")
            return

        tech_sale.set_monthly_sales(a)
    
    
        tech_sale.display_info()
        print(tech_sale.best_month())

        print()#для разделения вывода


        furniture_sale = Sale("Мебель")
        d = input("Введите 6 значений продаж в категории Мебель через пробел: ")
        c = [float(x) for x in d.split()] 
        if len(c) != 6:
            print("Введите значения за 6 месяцев через пробел")
            return

        if any(value < 0 for value in c):
            print("Введите положительные значения")
            return

        furniture_sale.set_monthly_sales(c)
        furniture_sale.display_info()
        print(furniture_sale.best_month())
    except ValueError:#ошибка типа данных
        print("Введите корректные значения")


if __name__ == "__main__":
    main()

