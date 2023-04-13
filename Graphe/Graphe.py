# Class

class GrapheMat:

    def __init__(self, sommets=0):
        self.n = sommets
        self.adj = [[False] * sommets for k in range(sommets)]

    def ajouter_arc(self, s1, s2):
        if 0 <= s1 < self.n and 0 <= s2 < self.n:
            self.adj[s1][s2] = True

    def arc(self, s1, s2):
        if 0 <= s1 < self.n and 0 <= s2 < self.n:
            return self.adj[s1][s2]

    def voisins(self, s):
        voisins = []
        if 0 <= s < self.n:
            for k in range(self.n):
                if self.adj[s][k]:
                    voisins.append(k)
        return voisins

# Test #

print('------- graphe vide --------')
g = GrapheMat(0)
print(g.adj)
print(" existe-t-il un arc de 0 à 1 ?  ",g.arc(0,1))
print(" voisins du sommet 0 : ",g.voisins(0))
g.ajouter_arc(0,1)
print(" peut-on ajouter un arc de 0 à 1 ? ",g.adj)
print('------- graphe a un élément ---------')
gg = GrapheMat()
print(gg.adj)
print(" existe-t-il un arc de 0 à 1 ?  ",gg.arc(0,1))
print(" voisins du sommet 0 : ",gg.voisins(0))
gg.ajouter_arc(0,1)
print(" peut-on ajouter un arc de 0 à 1 ? ",gg.adj)
print('------- graphe a deux éléments ---------')
ggg = GrapheMat(2)
print(ggg.adj)
print(" existe-t-il un arc de 0 à 1 ?  ",ggg.arc(0,1))
ggg.ajouter_arc(0,1)
print(" peut-on ajouter un arc de 0 à 1 ? ",ggg.adj)
print(" existe-t-il un arc de 0 à 1 ?  ",ggg.arc(0,1))
print(" voisins du sommet 0 : ",ggg.voisins(0))
print('--------- graphe quelconque --------')
g4 = GrapheMat(3)
print(g4.adj)
g4.ajouter_arc(0,1)
g4.ajouter_arc(0,2)
g4.ajouter_arc(2,1)
print(" existe-t-il un arc de 0 à 1 ?  ",g4.arc(0,1))
print(" existe-t-il un arc de 2 à 1 ?  ",g4.arc(0,1))
print(" peut-on ajouter un arc de 0 à 1 ? ",g4.adj)
print(" existe-t-il un arc de 0 à 1 ?  ",g4.arc(0,1))
print(" voisins du sommet 0 : ",g4.voisins(0))
print(" voisins du sommet 1 : ",g4.voisins(1))
print(" voisins du sommet 2 : ",g4.voisins(2))


# Class avec dictionnaires

class GrapheDic:

    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj.keys():
            self.adj[s] = set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)

    def arc(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj.keys())

    def voisins(self, s):
        return self.adj[s]

# Test #

m=GrapheDic()
m.ajouter_sommet(0)
m.ajouter_sommet("A")
print(m.adj)
m.ajouter_arc("B","C")
print(m.adj)
print(m.arc('B',"C"))
print(m.sommets())
print(m.voisins("B"))

# Graphe non orienté

class Graphe_Non_Oriente:

    def __init__(self):
        self.adj = {}

    def ajouter_sommet(self, s):
        if s not in self.adj.keys():
            self.adj[s] = set()

    def ajouter_arc(self, s1, s2):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add(s2)
        self.adj[s2].add(s1)

    def arc(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj.keys())

    def voisins(self, s):
        return self.adj[s]

    def __str__(self):
        g = list(self.adj.items())
        j = ""
        for hkgkhg in range(len(g)):
            p = 0
            m = str(g[hkgkhg][0]) + " -> "
            if g[hkgkhg][1] != set():
                for k in g[hkgkhg][1]:
                    p += 1
                    m += k
                    if len(g[hkgkhg][1]) - p >= 1:
                        m += ", "
                j += m + "\n"
            else:
                j += m + "\n"
                m = str(g[hkgkhg][0]) + " -> "
        return j

    def nb_arcs(self):
        n = 0
        for s in self.adj.keys():
            n += len(self.adj[s])
        return n // 2

    def supprimer_arc(self, s1, s2):
        self.adj[s1].remove(s2)
        self.adj[s2].remove(s1)

    def nb_sommet(self):
        return len(self.adj.keys())

    # On appelle degré d'un sommet, dans un graphe le nombre de ses voisins.

    def degré(self, s):
        return len(self.adj[s])

# Test #

m=Graphe_Non_Oriente()
m.ajouter_sommet(0)
m.ajouter_sommet("A")
print(m.adj)
m.ajouter_arc("B","C")
m.ajouter_arc("B","D")
m.ajouter_arc("B","E")
print(m.adj)
print(m.arc('B',"C"))
print(m.sommets())
print(m.voisins("B"))
print(m.voisins("C"))
print(m.adj)
print("\n")
print(m)
print(m.nb_sommet())
print(m.degré('B'))