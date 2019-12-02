
def alg_euclides_est(a, b):
    #retorna (x, y) tal que a*x + b*y = 1
    d, x, y, z = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y, z = z, y - q * z
        d, x = x, d - q * x
    return b, d, y

print (alg_euclides_est(7,14))

# retorna x de modo que:    (x*a) === 1 (mod b)
def mulinv(a, b):
    output = alg_euclides_est(a, b)
    g = output[0]
    x = output[1]

    if g == 1:
        return x % b
    else:
        return "MDC("+str(a)+","+str(b)+")!=1, logo, não tem inversa"

for i in range (100,10000):
    print (mulinv(i,237))
