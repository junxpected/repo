fib = [0, 1]
while len(fib) < 30:
    fib.append(fib[-1] + fib[-2])
print("Числа Фібоначчі:", fib)

# Шаблон 1: кожне третє число парне
ok = True
for i in range(30):
    if (i % 3 == 0) != (fib[i] % 2 == 0):
        ok = False
print("Кожне третє число парне:", ok)

# Шаблон 2: відношення сусідніх чисел наближається до 1.618
for i in (5, 10, 20, 29):
    print("fib[%d] / fib[%d] = %.6f" % (i, i - 1, fib[i] / fib[i - 1]))

# Шаблон 3: останні цифри чисел повторюються з періодом 60
last = [x % 10 for x in fib]
print("Останні цифри перших 30 чисел:", last)
print("Збігаються з числами через 60?", end=" ")
big = [0, 1]
while len(big) < 120:
    big.append(big[-1] + big[-2])
print(all(big[i] % 10 == big[i + 60] % 10 for i in range(60)))