bloco_matematica = [469, 752, 717, 214, 333, 752, 717, 745, 333, 154]

def decifrar(alist, a, n):
    m = []
    for c in alist:
        m.append((c**a)%n)
    return m

print (decifrar(bloco_matematica, 65537,817))
