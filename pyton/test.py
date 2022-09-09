a = int(input())

b = a//1000

one = b // 100
two = b // 10 % 10
three = b % 10

c = a % 1000

four = c // 100
five = c // 10 % 10
six = c % 10

if (one+two+three)==(four+five+six):
    print ('Счастливый')
else:
    print ('Обычный')