"""
Funciones a usar
    isMutant(List) de tipo booleano
    
    isAdn(List) de tipo booleano
"""
def isMutant(dna):    
    """
    devuelve True si la cadena ADN es mutante
    búsqueda por filas, columnas, diagonal superior e inferior derecha e izq.

    Se puede mejorar esta función creando una nueva función interna para recorrer por filas
    las reorganizaciones de datos diagonales =)
    """
    letrasIguales = 0 
    secuencia = 0
    cadenaMutante = [] #Usada para debug
    #Búsqueda por filas
    for f in range(len(dna)):   #recorre filas
        letrasIguales = 0
        
        for c in range(len(dna)-1): #recorre columnas
        
            if dna[f][c] == dna[f][c+1]:                
                letrasIguales += 1
                
                if letrasIguales == 3: #cadena detectada
                    
                    cadenaMutante.append(dna[f][c-2])
                    cadenaMutante.append(dna[f][c-1])
                    cadenaMutante.append(dna[f][c])
                    cadenaMutante.append(dna[f][c+1])
                    
                    secuencia += 1
            else:
                letrasIguales = 0
     
    #Búsqueda por columnas                
    for c in range(len(dna)):   #recorre columnas
        letrasIguales = 0
        
        for f in range(len(dna)-1): #recorre filas
            
            if dna[f][c] == dna[f+1][c]:                
                letrasIguales += 1
                
                if letrasIguales == 3: #cadena detectada
                    
                    cadenaMutante.append(dna[f-2][c])
                    cadenaMutante.append(dna[f-1][c])
                    cadenaMutante.append(dna[f][c])
                    cadenaMutante.append(dna[f+1][c])
                    
                    secuencia += 1                    
            else:
                letrasIguales = 0
                
    #Búsqueda oblicua o diagonal principal               
    for f in range(len(dna)-1):           
        c = f

        if dna[f][c] == dna[f+1][c+1]:                
            letrasIguales += 1
            
            if letrasIguales == 3:

                cadenaMutante.append(dna[f-2][c-2])
                cadenaMutante.append(dna[f-1][c-1])
                cadenaMutante.append(dna[f][c])
                cadenaMutante.append(dna[f+1][c+1])
                secuencia += 1                    
        else:
            letrasIguales = 0
                
    #Búsqueda oblicua en spin o diagonal superior izq derecha
    for k in range(len(dna)):  
        cadenaTemp = []
        
        if k > 3:
            for j in range(k+1):   #primer spin
                cadenaTemp.append(dna[k-j][j])            
        
            letrasIguales = 0
            for c in range(len(cadenaTemp)-1):   #recorre col                

                if cadenaTemp[c] == cadenaTemp[c+1]:                
                    letrasIguales += 1
                                        
                    if letrasIguales == 3: #cadena detectada
                        
                        cadenaMutante.append(cadenaTemp[c-2])
                        cadenaMutante.append(cadenaTemp[c-1])
                        cadenaMutante.append(cadenaTemp[c])
                        cadenaMutante.append(cadenaTemp[c+1])
                        
                        secuencia += 1
                else:
                    letrasIguales = 0
                    
    #Búsqueda oblicua en spin 2 o diagonal inferior izq a der
    for k in range(len(dna)-1,0,-1): 
        cadenaTemp = []
        
        for j in range(k):   #2ndo spin       
            cadenaTemp.append(dna[len(dna)-1-j][len(dna)-k+j])            
          
        letrasIguales = 0
        for c in range(len(cadenaTemp)-1):   #recorre col                

            if cadenaTemp[c] == cadenaTemp[c+1]:                
                letrasIguales += 1
                                    
                if letrasIguales == 3: #cadena detectada
                    
                    cadenaMutante.append(cadenaTemp[c-2])
                    cadenaMutante.append(cadenaTemp[c-1])
                    cadenaMutante.append(cadenaTemp[c])
                    cadenaMutante.append(cadenaTemp[c+1])
                    
                    secuencia += 1
            else:
                letrasIguales = 0

    #Búsqueda oblicua en spin 3 o superior der a izq
    for k in range(len(dna)):
        cadenaTemp = []
        
        for j in range(k):   #3er spin 
            cadenaTemp.append(dna[len(dna)-k+j][j])            
         
        letrasIguales = 0

        for c in range(len(cadenaTemp)-1):   #recorre col                

            if cadenaTemp[c] == cadenaTemp[c+1]:                
                letrasIguales += 1
                                    
                if letrasIguales == 3: #cadena detectada

                    cadenaMutante.append(cadenaTemp[c-2])
                    cadenaMutante.append(cadenaTemp[c-1])
                    cadenaMutante.append(cadenaTemp[c])
                    cadenaMutante.append(cadenaTemp[c+1])
                    
                    secuencia += 1
            else:
                letrasIguales = 0

    #Búsqueda oblicua en spin 4 o diagonal inferior der a izq
    for k in range(len(dna)):
        cadenaTemp = []
 
        for j in range(k):   #4to spin 
            cadenaTemp.append(dna[j][len(dna)-k+j])            
           
        letrasIguales = 0
        for c in range(len(cadenaTemp)-1):   #recorre col                

            if cadenaTemp[c] == cadenaTemp[c+1]:                
                letrasIguales += 1
                                    
                if letrasIguales == 3: #cadena detectada
                    
                    cadenaMutante.append(cadenaTemp[c-2])
                    cadenaMutante.append(cadenaTemp[c-1])
                    cadenaMutante.append(cadenaTemp[c])
                    cadenaMutante.append(cadenaTemp[c+1])
                    
                    secuencia += 1
            else:
                letrasIguales = 0
                
    print(cadenaMutante)
    if secuencia > 1: #Mutante detectado
        print("usuario con",secuencia,"cadenas de ADN interesantes")
        return True
    else:
        print("usuario con",secuencia,"cadena(s) de ADN interesante(s)")
        return False

#********************* función isAdn ****************************
def isAdn(dna):
    print("La cadena de ADN recibida es:")
    #contar filas
    N = len(dna) #tamaño filas
    M = 0 #tamaño columnas
    
    #contar columnas
    for filas in range(N):
        M = 0
        print()
        for col in range(len(dna[filas])):
            M +=1
            print(dna[filas][col],end="")
        if N==M:
            pass
        else:
            print("\nrevisa la cadena de ADN, los tamaños NxM no son iguales")
            return False
        
    for f in range(len(dna)):   #recorre filas
        print()
        fail=[]
        error = 0
        for c in range(len(dna)): #recorre columnas

            if (dna[f][c] == 'A' or dna[f][c] == 'T' or dna[f][c] == 'C' or
            dna[f][c] == 'G'):
                pass
                #print(dna[f][c],end="")
            else:
                print(" ",end="")
                error = 1
                fail.append(dna[f][c])
        if error:
                print(" Error",fail,"No es una base nitrogenada",end="")
                return False
    print()
    return True

if __name__=="__main__":
    print("solo para debug")
    dna1=["ATGCGA",
         "CAGTGC",
         "TTATGT",
         "AGAAGG",
         "CCCCTA",
         "TCACTG"]
    dna2=["ATGCGA",
          "CAGTGC",
          "TTTTGA",
          "ATAAAG",
          "TCCATA",
          "TCACTG"]
    dna3=["ATGCGA",
          "CAGTGC",
          "TTTTGA",
          "ATAAGG",
          "TCCCGA",
          "TCACTG"]
    dna4=["ATTCGA",
          "CACACC",
          "TTGTTA",
          "ATAAGT",
          "TCGCGA",
          "TCATTG"]
    dna5=["ATTCGA",
          "CACTCC",
          "TTGTA", #adn con un faltante
          "ATAAGT",
          "TCACGA",
          "TCATTG"]
    dna6=["ATTCG",
          "CFCPC", #adn con error
          "TTATT",
          "ATAAG",
          "TCAKG"]

    dna7=["ATTCG",
          "CCCCC",
          "TTATT",
          "ATAAG",
          "TCAAG"]
    
    dna8=["ATTCGTA",
          "CCCCCTA", #adn con error
          "TTATTTA",
          "ATAAGTA"]
    
    dna = dna8
    if isAdn(dna):
        print(isMutant(dna))




    
