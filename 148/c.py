n = input()

a, b = n.split()

a = int(a)
b = int(b)

for i in range(10 ** 5):
    i = i + 1
    if (i * a) % b == 0:
        print(a*i)
        break
