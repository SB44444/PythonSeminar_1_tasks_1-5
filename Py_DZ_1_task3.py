#  3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
#  Пример:
#  - x=34; y=-30 -> 4
#  - x=2; y=4-> 1
#  - x=-34; y=-30 -> 3

x = int(input('Input the  coordinate X =  '))
y = int(input('Input the  coordinate Y =  '))
if x == 0 and y == 0:
    print('The point is the origin of the coordinate plane')
elif x == 0 and y > 0:
    print('The point belongs to 1 and 2 quarters')
elif x == 0 and y < 0:
    print('The point belongs to 3 and 4 quarters')
elif y == 0 and x > 0:
    print('The point belongs to 1 and 4 quarters')
elif y == 0 and x < 0:
    print('The point belongs to 2 and 3 quarters')
elif x > 0 and y > 0:
    print('The point belongs to 1 quarter')
elif x < 0 and y > 0:
    print('The point belongs to 2 quarter')
elif x < 0 and y < 0:
    print('The point belongs to 3 quarter')
elif x > 0 and y < 0:
    print('The point belongs to 4 quarter')    
