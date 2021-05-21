import math
a=int(input('Enter Firts Number : '))
b=int(input('Enter Second Number : '))
print('*'*57,'Calculatore','*'*57)
print(' Select operation')
print(' 1.Addition')
print(' 2.Subtraction')
print(' 3.Multiplication')
print(' 4.Divide')
print(' 5.Square')
print(' 6.squar root')
print('*'*127)
c=int(input('Enter number of Operation'))
if c==1:
    print('Addition =',a+b)
elif c==2:
    print('Suntraction =',a-b)
elif c==3:
    print('Multiplication =',a*b)
elif c==4:
    print('Divide =',a/b)
elif c==5:
    print('Square',a**b)
elif c==6:
    print(math.sqrt(a))
    print(math.sqrt(b))