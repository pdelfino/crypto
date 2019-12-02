dict = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15,
        "g":16,"h":17,"i":18,"j":19,"k":20,"l":21,
        "m":22,"n":23,"o":24,"p":25,"q":26,
        "r":27,"s":28,"t":29,"u":30,"v":31,"w":32,"x":33,"y":34,"z":35," ":36}

bloco_descriptografado_num = [22, 102, 91, 422, 102, 91, 812, 10]

def num_to_char(lista_num):

    string = ""
    
    for i in lista_num:
        string += str(i)
    
    lista = []
    
    for i in range(int(len(string)/2)):
        lista.append(int(string[2*i:2*i+2]))

    lista_char = []

    for num in lista:
        for i in dict:
            if num==dict[i]:

                lista_char.append(i)
                break

    final_string = ""
    
    for i in lista_char:
        final_string += str(i)

    return final_string

print (num_to_char(bloco_descriptografado_num))

