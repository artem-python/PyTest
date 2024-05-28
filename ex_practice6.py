import numpy as np

# 2-3
a, s, p = 1, 150, 200

while not a > 10:
    a += 2
    p += a
    s += p
print(f"A: {a}\nP: {p}\nS: {s}")
# Long
while True:
    if a > 10:
        break
    else:
        a += 2
        p += a
        s += p
print(f"A: {a}\nP: {p}\nS: {s}")

# 4
s = 1

for n in range(1, 6):
    s *= n
print(f"S: {s}")
# Long
s = 1

for n in [1, 2, 3, 4, 5]:
    s *= n
print(f"S: {s}")

# 5
m, n = 12, 5
while m != n:
    if m > n:
        m -= 2 * n
    else:
        n -= 3
print(f"M: {m}\nN: {n}")
# Long
m, n = 12, 5
while True:
    if m == n:
        break
    else:
        if m > n:
            m -= 2 * n
        else:
            n -= 3
print(f"M: {m}\nN: {n}")

# 6
l, k = [], []
for i in range(10):
    k.append(10 - i)
for i in range(10):
    l.append(k[5] - k[i])
res = np.array(l)
print(len(res[res < 0]))
# Long
l, k = [], []
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    k.append(10 - i)
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    l.append(k[5] - k[i])
res = np.array(l)
print(len(res[res < 0]))
