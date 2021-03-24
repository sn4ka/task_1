import math

print ("Введите число")
n = int(input())

if n <= 1:
    print("Число должно быть больше 1")
    quit()
elif n == 2:
    print("Число простое")
    quit()

k = 2
l = int(math.sqrt(n))

while k <= l:
    if n % k == 0:
        print("Число составное")
        quit()
    k += 1

print("Число простое")