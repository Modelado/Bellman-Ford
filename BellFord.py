def  crearAristas(G, nodo1, nodo2, peso):
    if nodo1 not in G:
        G[nodo1] = {}
    if nodo2 not in G:
        G[nodo2] = {}
    if nodo2 not in G[nodo1]:
        (G[nodo1])[nodo2] = peso
    return G

def bellmanFord(G,s,t):
    Grafica ={}
    for v in G:
        for peso in G[v]:
            crearAristas(Grafica,peso,v,(G[v])[peso])

    opt = {}
    for v in G:
        opt[v] = 10000    
    opt[s] = 0
    anterior = {}
    
    for i in range(len(G)):
        for v in G:
            if v in Grafica:
                for peso in Grafica[v]:
                    if opt[peso] + (Grafica[v])[peso] < opt[v]:
                        opt[v] = opt[peso] + (Grafica[v])[peso]
                        anterior[v] = peso    
    print "Caminos cortos de  " + s + " hacia  cada vertice" 

    for peso in G:
        v = peso
        camino = " " + peso
        while (v != s):
            camino += " " + anterior[v]
            v = anterior[v]
        print camino
    
def test():
    (a,b,c,d,e,f) = ('A', 'B', 'C', 'D', 'E', 'F')
    aristas = ((a,b,1),(a,c,2),(a,d,4),(c,d,1),(d,f,3),(d,e,2),(f,e,1))
    G = {}
    for (v,peso,cost) in aristas:
        crearAristas(G, v, peso, cost)
    
    bellmanFord(G, a, f)
    
test()
