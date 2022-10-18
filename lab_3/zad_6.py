def listmerger(lista1:list,lista2:list)->list:
    #Połączyć
    lista3 = lista1+lista2\

    #Usuwanie duplikatów
    lista3 = list(dict.fromkeys(lista3))

    #Do potęgi trzeciej
    i = 0
    while i < len(lista3):
        lista3[i]**=3
        i+=1

    return lista3