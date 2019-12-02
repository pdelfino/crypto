# bruna:
def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    
    return b, x0, y0

# retorna x de modo que:    (x*a) === 1 (mod b)
def mulinv(a, b):
    g, x, _ = xgcd(a, b)
    
    if g == 1:
        return x % b
    else:
        return "MDC("+str(a)+","+str(b)+")!=1, logo, não tem inversa"


