# Find the maximum of five number
num = int(input('Enter number 1 \n'))
num1 = int(input('Enter number 2 \n'))
num2 = int(input('Enter number 3 \n'))
num3 = int(input('Enter number 4 \n'))
num4 = int(input('Enter number 5 \n'))
if num > num1 > num2 > num3 > num4:
    print(num)
if num1 > num > num2 > num3 > num4:
    print(num1)
if num2 > num > num1 > num3 > num4:
    print(num2)
if num3 > num > num1 > num2 > num4:
    print(num3)
if num4 > num > num1 > num2 > num3:
    print(num4)
else:
    print('You entered the wrong thing, repeat the input')


