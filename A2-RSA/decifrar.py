bloco_matematica = [70, 11, 71, 214, 352, 11, 71, 574, 352, 439]

def decifrar(alist, a, n):
    m = []
    for c in alist:
        m.append((c**a)%n)
    return m

print (decifrar(bloco_matematica, 341,817))
