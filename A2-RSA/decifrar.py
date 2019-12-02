bloco_matematica = [70, 11, 71, 176, 11, 71, 15, 439]

def decifrar(alist, a, n):
    m = []
    for c in alist:
        m.append((c**a)%n)
    return m

print (decifrar(bloco_matematica, 341,817))
