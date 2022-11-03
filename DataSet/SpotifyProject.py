import csv
import networkx as nx
import matplotlib.pyplot as plt
#First, We are go to reading a CSV, so far the data

def menu():
    print("Existen tres opciones para el filtrado: ")
    print("1.Bailabilidad")
    print("2.Popularidad")
    print("3.Bailabilidad y Popularidad")
    opcion=input("Que opción eliges?: ")
    try:
        value=int(opcion)
        if(value==1 or value==2 or value==3):
            return value
        else:
            return "Numero fuera de rango"
    except:
        return "Algo salió mal"


#option=menu()

#fh=open("songs_list_1.csv")
#for line in fh:
#    print(line)

#4-> Popularity
#5 ->Danceability


#Ranges Function

def getPointsDanceability(number):
    if 0 <= number <=9 : return 0
    if 10 <= number <= 19: return 2
    if 20 <= number <= 29: return 4
    if 30 <= number <= 39: return 6
    if 40 <= number <= 49: return 8
    if 50 <= number <= 59: return 10
    if 50 <= number <= 59: return 12
    if 60 <= number <= 69: return 14
    if 70 <= number <= 79: return 16
    if 80 <= number <= 89: return 18
    if 90 <= number <= 100: return 20

def getPointsPopularity(number):
    if 0 <= number <=9 : return 0
    if 10 <= number <= 19: return 2
    if 20 <= number <= 29: return 4
    if 30 <= number <= 39: return 6
    if 40 <= number <= 49: return 8
    if 50 <= number <= 59: return 10
    if 50 <= number <= 59: return 12
    if 60 <= number <= 69: return 14
    if 70 <= number <= 79: return 16
    if 80 <= number <= 89: return 18
    if 90 <= number <= 100: return 20

G=nx.DiGraph()

with open("songs_list_1.csv", "r") as file:
    csvreader=csv.reader(file)
    for row in csvreader:
        if(len(row)!=0):
            try:
                #print("XD")
                print(row[0],getPointsPopularity(int(row[3])))
                G.add_node(row[0])
            except:
                print("Anue value")



#G.add_edge(grafo,aristaInicial,aristaFinal,peso,DirigidoONoDirigido)

#G.add_node("Cancion2")
#G.add_edge("Cancion1","Cancion2")
print(G)

#nx.draw(G,with_labels=True)
pos=nx.layout.planar_layout(G)
nx.draw_networkx(G,pos)
labels=nx.get_edge_attributes(G,"weight")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.title("Grafo Canciones")
plt.show()
