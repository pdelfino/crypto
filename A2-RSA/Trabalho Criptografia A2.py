
# coding: utf-8

# ## Criptografia RSA
# Alunos: Bruna Fernanda Fistarol e Pedro Delfino

# O conjunto de códigos a seguir pretende simular o funcionamento da criptografia RSA. 
# 
# O algoritmo foi descrito em 1978 com o objetivo de possibilitar a transmissão segura de dados. 
# O sistema tem como base de funcionamento uma chave pública, divulgada para criptografar os dados, e uma chave privada, a qual é secreta. A essência do algoritmo encontra-se na dificuldade de decompor um número muito grande em fatores primos, decomposição esta necessária para descobrir a chave secreta do sistema.

# **1)** Escolha, aleatoriamente, dois números primos $p$ e $q$.

# **2)** Calcule $n = pq$ e $Φ(n) = (p - 1)(q - 1)$.

# **3)** Escolha $1 < a < Φ(n)$ de forma que $a$ e $Φ(n)$ sejam primos entre si; assim, $a$ possui inverso multiplicativo módulo $Φ(n)$.

# In[17]:


def mdc(a, Φ):
    #retorna m = mdc(a, Φ)"
    while a != 0:
        Φ, a = a, Φ % a
    return Φ


# O código acima pode ser usado para testar se o $a$ escolhido é primo com $Φ(n)$; caso seja, o mdc retornado será $1$.

# **4)** Calcule $d$ de modo que $d$ seja o inverso multiplicativo de $a$ módulo $Φ(n)$, ou seja, $a*d  ≡ 1 ~~(mod ~~Φ(n))$

# Para o cálculo de $d$, utilizamos o Algoritmo de Euclides Estendido. 

# In[ ]:


def alg_euclides_est(a, b):
    #retorna (x, y) tal que a*x + b*y = 1
    d, x, y, z = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y, z = z, y - q * z
        d, x = x, d - q * x
    if 1%b != 0:
        return "O sistema não tem solução"
    else:
        return d


# ### Criptografando a mensagem

# Para criptografar uma mensagem $m$ tal que $1 < m < n-1$ em uma mensagem $c$, basta fazer $m^a ≡ c ~~(mod ~~n)$

# ### Descriptografando a mensagem

# Para recuperar a mensagem criptografada, basta fazer $c^d ≡ m~~ (mod~~n)$
