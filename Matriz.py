t = [[i * i for i in range (3)] for j in range (3)]
print(t)
s = 0
for i in range(3):
    s += t[i][i]
    print(s)
print(s)