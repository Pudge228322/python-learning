b = input('Введите степень числа: ')
a = input('Введите число: ')
s = int(b) * str(a)
x = input('Введите 1 число из задания: ')
y = input('Введите 2 число из задания: ')
n2 = input("Введите 1 цифру 1 числа из задания: ")
n3 = input("Введите 1 цифру 2 числа из задания: ")
while x in s or y in s:
    if y in s:
        s = s.replace(y, n2, 1)
    else:
        s = s.replace(x, n3, 1)
print(s)
