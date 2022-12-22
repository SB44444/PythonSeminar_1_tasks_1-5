#  1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным./
#  Пример:
#  - 6 -> да
#  - 7 -> да
#  - 1 -> нет
my_day = int(input('Input the namber week day from 1 to 7 - '))
if 0 < my_day < 6:
        print('No, the day is not weekend')
elif 5 < my_day < 8:
    print('Yes, the day is weekend')
else:
    print('Input the correct namber')