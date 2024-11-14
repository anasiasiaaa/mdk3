from random import randint, uniform
def start(claim):
    print('Приём в ВУЗ открыт')
    
    #генерация значений проходного балла в зависимости от выбранного режима
    if claim['mode'] == 'fixed':
        claim['score1'] = randint(78, 85)#ограничения на рандом
        claim['score2'] = randint(70, 77)
        #проверка, чтобы значения отличались минимум на 8
        while claim['score1'] - claim['score2'] < 8:
            claim['score2'] = randint(70, 77)
    else:
        #генерация случайных значений 
        scores1 = [randint(78, 85) for _ in range(100)] 
        scores2 = [randint(70, 85) for _ in range(100)]
        claim['score1'] = sum(scores1) // len(scores1) #подсчеты среднего
        claim['score2'] = sum(scores2) // len(scores2)  
    
    #вывод
    print(f'Документы поданы')
    print(f'Проходной балл для 1 волны: {claim["score1"]}, для 2 волны: {claim["score2"]}')
    
    claim['state'] = 'analyze_wave1'
def analyze_wave1(claim):
    #анализ результатов вступительных испытаний для 1 волны
    claim['valueN'] = randint(60, 100)  #генерация случайного результата
    print(f'Результат вступительных испытаний: {claim["valueN"]}')
    print(f'Конкурс 1 волна')
    
    #проверка, попадает ли абитуриент в 1 волну
    if claim['valueN'] > claim['score1']:
        print('Попадание в 1 волну')
        claim['state'] = 'processing' 
    else:
        claim['state'] = 'analyze_wave2' 
def analyze_wave2(claim):
    #анализ результатов вступительных испытаний для 2 волны
    print(f'Конкурс 2 волна')
    
    #проверка, попадает ли абитуриент во 2 волну
    if claim['valueN'] > claim['score2']:
        print('Попадание во 2 волну')
        claim['state'] = 'processing'  
    else:
        print('Конкурс не пройден')
        claim['state'] = 'finish' 
def processing(claim):
    #обработка результатов и вывод приказа о зачислении
    print('Приказ о зачислении')
    claim['state'] = 'finish' 
def finish(claim):
    #вывод сообщения о завершении
    print('Приём в ВУЗ закрыт')
    claim['state'] = None  #завершение работы кода
#определение какие функции в каком состоянии вызывать
state = {
    'start': start,
    'analyze_wave1': analyze_wave1,
    'analyze_wave2': analyze_wave2,
    'processing': processing,
    'finish': finish
}
#запуск процесса поступления в ВУЗ
def run_admission(mode):
    claim = {'state': 'start', 'mode': mode}  #создание новой заявки с выбранным режимом
    while claim['state'] is not None:  #выполняем цикл, пока процесс не завершится
        fun = state[claim['state']]  #определяем функцию для текущего состояния
        fun(claim)  #вызываем соответствующую функцию
#ыыбор режима работы
def main():
    print("Выберите режим работы: \n1. Фиксированные значения \n2. Среднее арифметическое")
    choice = input("Введите 1 или 2: ")
    if choice == '1':
        run_admission('fixed')
    elif choice == '2':
        run_admission('average')
    else:
        print("Неверный ввод. Пожалуйста, введите 1 или 2.")
main()
