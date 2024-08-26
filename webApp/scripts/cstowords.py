def swaphexa1byte(word):  #ingresa 1 bytes hexa y devuelve el swap
    longitud = len(word)
    mitad = longitud // 2
    parte1 = word[:mitad]
    parte2 = word[mitad:]
    word = parte2 + parte1
    return word

def swaphexa(word):  #ingresa 2 bytes hexa y devuelve el swap
    longitud = len(word)
    mitad = longitud // 2
    parte1 = word[:mitad]
    parte2 = word[mitad:]
    parte1 = parte1[::-1]
    parte2 = parte2[::-1]
    word = parte1 + parte2
    return word

def hexbinswapbinhex(word): #ingresa 2 bytes hexa convierte en binario, swapea y devuelve hexa
    string=""
    for caracter_hex in word:
        #print("carácter ingresado hexadecimal: ",caracter_hex)
        # Convertir el carácter hexadecimal a binario de 4 dígitos
        caracter_bin = bin(int(caracter_hex, 16))[2:].zfill(4)
        #print("El carácter en binario de 4 dígitos es:", caracter_bin)
        cadena_invertida = str(caracter_bin[::-1])
        #print("Cadena invertida:",cadena_invertida)
        numero_binario =cadena_invertida
        # Convertir el número binario a hexadecimal
        numero_hex = hex(int(numero_binario, 2))[2:]
       # print(numero_hex)
        string+=numero_hex

    return string

def show_words(numero_cs):
    words="\n\n"

    if len(numero_cs)==24:
        words+=f"Es sistema 12 bytes!!\nNumero CS= {numero_cs}\n" 

        words+=f"word 4 = {hexbinswapbinhex(swaphexa(numero_cs[20:24]))}\n"

        words+=f"word 5 = {hexbinswapbinhex(swaphexa(numero_cs[16:20]))}\n"

        words+=f"word 6 = {hexbinswapbinhex(swaphexa(numero_cs[12:16]))}\n"

        words+=f"word 7 = {hexbinswapbinhex(swaphexa(numero_cs[8:12]))}\n"

        words+=f"word 8 = {hexbinswapbinhex(swaphexa(numero_cs[4:8]))}\n"

        words+=f"word 9 = {hexbinswapbinhex(swaphexa(numero_cs[0:4]))}\n"      

        return words
    
    elif len(numero_cs)==12:
        words+=f"Es sistema 6 bytes!!\nNumero CS= {numero_cs}\n"
        return words
    elif len(numero_cs)==14:
        words+=f"Es sistema 7 bytes!!\nNumero CS= {numero_cs}\n" 
        words+=f"word 9 = {hexbinswapbinhex(swaphexa(numero_cs[0:4]))}\n"
        words+=f"word 8 = {hexbinswapbinhex(swaphexa(numero_cs[4:8]))}\n"
        words+=f"word 7 = {hexbinswapbinhex(swaphexa(numero_cs[8:12]))}\n"
        words+=f"word 6 = {hexbinswapbinhex(swaphexa1byte(numero_cs[12:14]))}+84\n"
        return words
    #print("Cadena invertida y dividida a la mitad:", swaphexa(numero_cs[12:16]))


    else:
        return "Error el numero tiene que tener 24 digitos"
