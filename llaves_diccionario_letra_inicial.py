lista = input("introduzca lista de palabras: ")
lista = lista.split(', ')
dic = {}

for p in lista:
    if dic.get(p[0]) != None:
        if isinstance(dic.get(p[0]), list):
            dic.get(p[0]).append(p)
        else:
            dic[p[0]] = [dic.get(p[0]), p]
    else:
        dic[p[0]] = p

print(f'\n Resultado diccionario: {dic}')