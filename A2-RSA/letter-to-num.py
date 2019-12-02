dict = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,
        "g":16,"h":17,"i":18,"j":19,"k":20,"l":21,
        "m":22,"n":23,"o":24,"p":25,"q":26,
        "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35," ":36}

#duas funções
#for i in dict:
 #   print (i,dict[i])

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
    string = ""
    for i in lista_num:
        string += str(i)

    return string

#print (char_to_num("a"))
teste= char_to_num("BRENO bumbum guloso")
teste_bruna = char_to_num("matematica")
#print (teste_bruna)

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

#print (num_to_char(teste))
#print (num_to_char(teste_bruna))

print (char_to_num('matematica'))
