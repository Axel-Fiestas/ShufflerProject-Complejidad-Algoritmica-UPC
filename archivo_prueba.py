diccionario={1:"Shibayan Records",2:"Shibayan Records",3:"Shibayan Records",4:"Foals"}

#Añadir elemento
diccionario[5]="The Police"

print(diccionario)

for clave in diccionario:
    valor=diccionario[clave]

    print(valor)

l = [['apple','banana','kiwi'],['chair','table','spoon']]
lista_id=[["Men At Work","Down Under"],["Men At Work","Catch A Star"],["Shibayan Records","SUPER MOON"]]
def findItem(theList, item):
   return [(ind, theList[ind].index(item)) for ind in range(len(theList)) if item in theList[ind]]

print(findItem(l, 'apple')) # [(0, 0)]
print(findItem(l, 'spoon')) # [(1, 2)]
print(findItem(lista_id,"Men At Work"))