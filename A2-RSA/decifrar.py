bloco_matematica = [770, 752, 459, 643, 752, 459, 659, 584]

def decifrar(alist, a, n):
    m = []
    for c in alist:
        m.append((c**a)%n)
    return m

print (decifrar(bloco_matematica, 563,817))
