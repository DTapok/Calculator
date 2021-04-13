numb = float(input('Введите первое число - '))
cycle = True
while(cycle):
    operation = input(f'{numb} ')
    operation = operation.split()
    try:
        if (operation[0] == '+'):
            numb = numb + float(operation[1])
        elif (operation[0] == '-'):
            numb = numb - float(operation[1])
        elif (operation[0] == '*'):
            numb = numb * float(operation[1])
        elif (operation[0] == '/'):
            if (operation[1] != '0'):
                numb = numb / float(operation[1])
            else:
                print('Попытка деления на ноль!!!')
        elif (operation[0] == '**'):
            numb = numb ** float(operation[1])
        elif (operation[0] in 'cC'):
            numb = 0
        elif (operation[0] == '='):
            cycle = False
        else:
            print('Не корректно введена операция')
            print('Попробуй разделять операцию и число пробелом')
    except:
        print('Что-то пошло не так...')
print(f'Ответ {numb}')