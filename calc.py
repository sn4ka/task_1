print("Символ мат. операции '0' завершит работу программы"
        "\n'=' выведет результат")
z = 0
x = float(input("x = "))
while z != "=":
    z = input("Выберите символ мат.операции (+,-,*,/,**): ")
    if z == '0':
        break
    if z in ('+', '-', '*', '/', '**'):
        y = float(input("y = "))
        if z == '+':
            x += y
        elif z == '-':
            x -= y
        elif z == '*':
            x *= y
        elif z == '**':
            x **= y
        elif z == '/':
            if y != 0:
                x /= y
            else:
                print("Деление на 0")
    else:
        if z != "=":
            print("Неверный знак операции!")
print (x)