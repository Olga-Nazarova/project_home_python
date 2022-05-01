# Using two given numbers, check whether one is the square of the second
print('Enter the first number')
num = int(input())
print('Enter the second number')
num1 = int(input())
if num == num1 ** 2:
    print('A number', num, 'is the square of another', num1)
else:
    print('The numbers entered are not squares of each other')

