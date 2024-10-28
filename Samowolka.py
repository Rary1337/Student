def Calculator():
    num1 = float(input('Введите первое число:'))
    operator = input ('Введите нужное действие (*, -, +, /):')
    num2 = float(input('Введите второе число:'))
    if operator == '+':
        print(num1+num2)
    elif operator == '/':
        print(num1/num2)
    elif operator == '*':
        print(num1*num2)
    elif operator == '-':
        print(num1-num2)
    else:
        print('Неверное значение')


Calculator()

