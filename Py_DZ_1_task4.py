#  4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quarter  = int(input('Input the namber of the quarter from 1 to 4 - '))
if quarter == 1:  
    print('The value of the arguments is: x > 0 ; y > 0')
elif quarter ==  2:      
    print('The value of the arguments is: x < 0 ; y > 0')
elif quarter == 3:
    print('The value of the arguments is: x < 0 ; y < 0')
elif quarter == 4 : 
    print('The value of the arguments is: x > 0 ; y < 0')
else:      print('Input the correct namber of the quarter')
