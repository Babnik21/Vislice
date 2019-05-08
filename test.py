def prastevilo(n):
    if n == 1:
        return False
    for i in range(1, int(n**0.5//1)):
        if n%(i+1) == 0:
            return False
    return True

sez = []
for i in range(1, 200):
    if prastevilo(i):
        sez.append(i)

print(sez)