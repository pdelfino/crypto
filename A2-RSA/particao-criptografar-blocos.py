def particao(N, n):
    a = 0
    b = 1
    saida = []
    while b != len(N):
        while int(N[a:b]) < n:
            b += 1
            if b == len(N) + 1:
                saida.append(int(N[a:b - 1]))    
                return saida
        b -= 1
        if N[b] == '0':
            b -= 1
        saida.append(int(N[a:b]))
        a = b
        b +=1

output = (particao('22102914221029181210', 817))
print (output)

def criptografia(alist, a, n): #recebe lista de números
    c = []
    for m in alist:
        c.append((m**a)%n)
    return c

print (criptografia(output,65537,817))
