# Algebra, Teoria dos Números e Criptografia 
---

 + Professor:  Luciano Castro.

 + Data: 2019.2.

 + Tech Stack: Python 3. 

 + Projeto: 
   
     - A1: 
      
        - resolução das questões de programação do livro  "Números inteitores e Criptografia RSA" do Capítulo 1 ao 6.
       
     - A2: 
      
        - [a definir, provável: blockchain]
       
     
### Por que usar github?

Conforme conversado um dia após a aula, apresentar o trabalho como arquivo markdown no github tem algumas vantagens:
- não exige nenhuma instalação, simplesmente abrindo o link no navegador;
- o formato markdown permite uma estética bacana que diferencia código de texto;
- o trabalho fica no github e, como legado, faz parte do portfólio do aluno. Cada vez mais, o github tem sido analisado como parte da entrevista de programadores.



## Capítulo 1



### Questão 1

Na verdade, não era para fazer essa questão. A instrução é que apenas questões com indicação de "faça um programa..." sejam feitas.

No entanto, quando eu comecei o trabalho eu achei que era para fazer todas as questões que **pudessem ser resolvidas** por um algoritmo rs. Então, acabei fazendo a questão 1. Foi bacana porque servia como teste unitário para outras questões.



```python
'''fiz o algoritmo de euclides, mas não era suficiente
    foi preciso extender, material de consulta livro, wikipedia'''
def euclidean_algo(m,n):
    
    if m%n==0:
        return n

    else:
        remainder = m%n
        m = n
        n = remainder
        return str(euclidean_algo(m,n))

def mdc(m,n):

    mdc = euclidean_algo(m,n)
    result = "MDC: "+str(mdc)
    return result

# teste com número grande - funciona
#print (mdc(1221,1234567891011121314151617181920212223242526272829))

def extended_euclidean_algo(m, n):
    
    if m == 0:
        return (n, 0, 1)
    
    else:
        mdc, x, y = extended_euclidean_algo(n % m, m)
        alpha = y - ((n//m)*x)
        beta = x
        return (mdc, alpha, beta)

def pretty_eea(m,n):
    mdc, alpha,beta = extended_euclidean_algo(m,n)
    print ("Par de inteiros:  ",m,n)
    return ("mdc: " +str(mdc) + ", alpha: "+str(alpha)+", beta: "+ str(beta)+"\n")

print ("exemplo do livro: ",pretty_eea(1234,54))
print (pretty_eea(14,35))
print (pretty_eea(252,180))
print (pretty_eea(6643,2873))
print (pretty_eea(272828282,3242))


```



Output:

```python
Par de inteiros:   1234 54
exemplo do livro:  mdc: 2, alpha: -7, beta: 160

Par de inteiros:   14 35
mdc: 7, alpha: -2, beta: 1

Par de inteiros:   252 180
mdc: 36, alpha: -2, beta: 3

Par de inteiros:   6643 2873
mdc: 13, alpha: -16, beta: 37

Par de inteiros:   272828282 3242
mdc: 2, alpha: 697, beta: -58655556

```





### Questão 8

Essa questão já é exatamente o que foi pedido. Basicamente, trata-se de uma implementação do algoritmo estendido de Euclides, como indicado pelo enunciado. A solução é:

```python
'''
    fiz o algoritmo de euclides, mas não era suficiente
    foi preciso extender, material de consulta livro, wikipedia'''

def euclidean_algo(m,n):
    
    if m%n==0:
        return n

    else:
        remainder = m%n
        m = n
        n = remainder
        return euclidean_algo(m,n)

#print (euclidean_algo(5,12))

def mdc(m,n):

    mdc = euclidean_algo(m,n)
    result = "MDC: "+str(mdc)
    return result

#print (mdc(1221,1234567891011121314151617181920212223242526272829))

def extended_euclidean_algo(a, b,c):

    gcd = euclidean_algo(a,b)
     
    if gcd%c!=0:
        return "Sem solução"

    else:

        if a == 0:
            return (b, 0, 1)
        
        else:
            mdc, x, y = extended_euclidean_algo(b % a, a,c)
            alpha = y - ((b//a)*x)
            beta = x
            return (mdc, alpha, beta)

def pretty_eea(m,n,c):
    
    output = extended_euclidean_algo(m,n,c)
    if output=="Sem solução":
        return "Sem solução"
    else:

        mdc, alpha,beta = extended_euclidean_algo(m,n,c)
        print ("Par de inteiros:  ",m,n)
        return (str(alpha)+"*"+str(m)+" + "+str(beta)+"*" +str(n)+"="+str(c))

print ("Exemplo do livro: ",pretty_eea(1234,54,2))
print ("Exemplo similar ao do livro com a=1234, b=54 e c= 3: ",pretty_eea(1234,54,3))

```

Além do livro, consultei também o wikipedia sobre o assunto. O output usou como teste um exemplo de dentro do livro, mas que não foi citado no enunciado:



```python
Par de inteiros:   1234 54
Exemplo do livro:  -7*1234 + 160*54=2
Exemplo similar ao do livro com a=1234, b=54 e c= 3:  Sem solução
```



### Questão 9

Achei essa questão bem legal. Na verdade, esse é o tipo de conteúdo que me empolga em matemática. Quando vi que o resultado do experimento computacional estava dando próximo ao resultado teórico tive uma sensação engraçada. Dá vontade de compartilhar de contar para alguém rs.



```python
import random

def euclidean_algo(m,n):
    
    if m%n==0:
        return n

    else:
        remainder = m%n
        m = n
        n = remainder
        return euclidean_algo(m,n)

#função para gerar pares de números
def random_pairs(n):
    lista = []
    for i in range(1,n):
        pairs = []

        pairs.append(random.randint(1,10000000))
        pairs.append(random.randint(1,10000000))
        lista.append(pairs)
    return lista

def mdc_on_list(l):

    num_pares = len(l)
    counter_coprime = 0

    for i in l: 
        #print (i)
        mdc = euclidean_algo(i[0],i[1])
        #print (mdc) 
        if mdc==1:
            counter_coprime+=1
            #print (counter_coprime)

    quotient = counter_coprime/num_pares
    #print (quotient)

    return quotient


for i in [10,100,1000,10000,100000,1000000,10000000]:

    print ("Total de duplas de inteiros a serem avaliados: "+str(i)+"| Proporção co-primos: "+str(mdc_on_list(random_pairs(i))))
```



 A tabela gerada foi:

```python
Total de duplas de inteiros a serem avaliados: 10| Proporção co-primos: 0.3333333333333333

Total de duplas de inteiros a serem avaliados: 100| Proporção co-primos: 0.5656565656565656

Total de duplas de inteiros a serem avaliados: 1000| Proporção co-primos: 0.5885885885885885

Total de duplas de inteiros a serem avaliados: 10000| Proporção co-primos: 0.603060306030603

Total de duplas de inteiros a serem avaliados: 100000| Proporção co-primos: 0.6066560665606656

Total de duplas de inteiros a serem avaliados: 1000000| Proporção co-primos: 0.6083026083026083

Total de duplas de inteiros a serem avaliados: 10000000| Proporção co-primos: 0.6079405607940561
```

Resultado teórico: 6/(pi^2)

Aproximadamente, o resultado teórico é: 0.60792710185

O experimento computacional mais robusto, com 1000000 pares de número como entrada, retorna: 0.6079713607971361

Isto indica a convergência entre o resultado empírico e o resultado teórico



## Capítulo 2



