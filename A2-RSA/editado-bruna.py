
O conjunto de códigos a seguir pretende simular o funcionamento da criptografia RSA. 
 
O algoritmo foi descrito em 1978 com o objetivo de possibilitar a transmissão segura de dados. 
O sistema tem como base de funcionamento uma chave pública, divulgada para criptografar os dados, e uma chave privada, a qual é secreta. A essência do algoritmo encontra-se na dificuldade de decompor um número muito grande em fatores primos, decomposição esta necessária para descobrir a chave secreta do sistema.

**1)** Escolha, aleatoriamente, dois números primos $p$ e $q$.

**2)** Calcule $n = pq$ e $Φ(n) = (p - 1)(q - 1)$.

**3)** Escolha $1 < a < Φ(n)$ de forma que $a$ e $Φ(n)$ sejam primos entre si; assim, $a$ possui inverso multiplicativo módulo $Φ(n)$.

def mdc(a, Φ):
    #retorna m = mdc(a, Φ)"
    while a != 0:
        Φ, a = a, Φ % a
    return Φ

O código acima pode ser usado para testar se o $a$ escolhido é primo com $Φ(n)$; caso seja, o mdc retornado será $1$.

**4)** Calcule $d$ de modo que $d$ seja o inverso multiplicativo de $a$ módulo $Φ(n)$, ou seja, $a*d  ≡ 1 ~~(mod ~~Φ(n))$

Para o cálculo de $d$, utilizamos o Algoritmo de Euclides Estendido. Note que calcular $d$ é equivalente a resolver a equação diofantina $ad - my = 1$, onde $m = Φ(n)$.

def alg_euclides_est(a, b):
    #retorna (x, y) tal que a*x + b*y = 1
    aux = b
    d, x, y, z = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y, z = z, y - q * z
        d, x = x, d - q * x
    if 1%b != 0:
        return "O sistema não tem solução"
    else:
        while d < 0:
            d += aux
    return d


Criptografando a mensagem

Para criptografar uma mensagem $m$ tal que $1 < m < n-1$ em uma mensagem $c$, basta fazer $m^a ≡ c ~~(mod ~~n)$. Aqui, utiliza-se a chave pública $(n, a)$.




dict = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,
        "g":16,"h":17,"i":18,"j":19,"k":20,"l":21,
        "m":22,"n":23,"o":24,"p":25,"q":26,
        "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35," ":36}


def char_to_num(string):

    string = string.lower()  
    
    lista_num = []

    for char in string:
        #print (char) 
        for i in dict:
            #print (i)  
            if char==i:
                
                lista_num.append(dict[i])
                break
    return lista_num

#print (char_to_num("a"))
teste = char_to_num("matematica")
print (teste)


-------

def criptografia(alist, a, n): #recebe lista de números correspondente a letras
    c = []
    for m in alist:
        c.append((m**a)%n)
    return c


Descriptografando a mensagem

 Para recuperar a mensagem criptografada, basta fazer $c^d ≡ m~~ (mod~~n)$. Para isso, é necessário ter acesso à chave privada $d$, que só é calculada rapidamente se houver acesso aos primos $p$ e $q$.


def decifrar(alist, d, n):
    m = []
    for c in alist:
        m.append((c**a)%n)
    return m


def num_to_char(lista_num):

    lista_char = []

    for num in lista_num:
        for i in dict:
            if num==dict[i]:

                lista_char.append(i)
                break

    final_string = ""
    
    for i in lista_char:
        final_string += str(i)

    return final_string

print (num_to_char(teste))


Para verificar se o código está funcionando, escolhemos $p = 19$ e $q = 43$. Daí:

$n = 19*43 = 817$
 
$Φ(n) = 18*42 = 756$

Agora, escolhemos $a$ tal que $a$ seja primo com $756$:

mdc(47, 756) # a = 47 é uma possível escolha

# Calculamos d:
