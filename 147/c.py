N = int(input())
A = [0]*20
x = [[] for i in range(20)]
y = [[] for i in range(20)]

for i in range(1, N+1):
    A[i] = int(input())
    for j in range(A[i]):
        tmp = input().split()
        x[i].append(int(tmp[0]))
        y[i].append(int(tmp[1]))

for bits in range(1, 1 << N+1):
    print(bits & (1 << (i-1)))

print(A)
print(x)
print(y)
