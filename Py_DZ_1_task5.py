#  5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.-+-
#  Пример:
#  - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21

x1, y1 = int(input('Input the coordinate X1 =  ')), int(input('Input the coordinate Y1 =  '))
x2, y2 = int(input('Input the coordinate X2 =  ')), int(input('Input the coordinate Y1 =  '))
distance = round(((x2 - x1)**2 + (y2 - y1)**2) **(0.5), 2)
print(f'distance from point 1 to point 2 is: {distance} ')
