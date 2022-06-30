import math
print('Вас приветствует приложение для вычисления дискриминанта! Впишите коэффициенты:')
print("ax^2 + bx + c = 0:")
a=int(input('Введите коэффициент a:'))
b=int(input('Введите коэффициент b:'))
c=int(input('Введите коэффициент c:'))
rofl=0
formula=((b**2)-4*a*c)
print('Дискриминант:')
print(formula)

if formula>0:

    import math
    from math import sqrt
    D=math.sqrt(formula)
    print('Корень дискриминанта равен:')
    print(D)
    D_plus=(-b+math.sqrt(formula))/(2*a)
    D_minus=(-b-math.sqrt(formula))/(2*a)
    print('Положительный корень:')
    print(D_plus)
    print('Отрицательный корень:')
    print(D_minus)
elif formula==0:

    D = math.sqrt(formula)
    print('Корень дискриминанта равен:')
    print(D)
    D_odin =-b/(2*a)
    print('Корень:')
    print(D_odin)
else:
    print('Нет корней')
