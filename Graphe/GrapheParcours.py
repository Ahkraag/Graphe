class Graphe:

    def __init__(self, oriente=False, pondere=False):
        self.adj = {}
        self.oriente = oriente
        self.pondere = pondere

    def ajouter_sommet(self, s):
        if s not in self.adj.keys():
            self.adj[s] = set()

    def ajouter_arc(self, s1, s2, d=1):
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.adj[s1].add((s2, d))
        if not self.oriente:
            self.adj[s2].add((s1, d))

    def arc(self, s1, s2):
        return s2 in self.adj[s1]

    def sommets(self):
        return list(self.adj.keys())

    def voisins(self, s):
        return list(self.adj[s])

    def __str__(self):
        rep = ""
        for sommet in self.adj.keys():
            rep += str(sommet) + " -->"
            for v in self.adj[sommet]:
                rep += " (" + str(v[0]) + "," + str(v[1]) + ") ,"
            rep += "\n"
        return rep

    def nb_sommets(self):
        return len(self.adj.keys())

    def degre(self, s):
        return len(self.adj[s])

    def nb_arcs(self):
        n = 0
        for s in self.adj.keys():
            n += len(self.adj[s])
        if not self.oriente:
            return n // 2
        return n

    def supprimer_arc(self, s1, s2, d):
        self.adj[s1].remove((s2, d))
        if not self.oriente:
            self.adj[s2].remove((s1, d))

def parcours_profondeur(g,s,vus):
    """parcours en profondeur du graphe g, depuis le sommet s.
    L'ensemble vus contient les sommets déjà visités"""
    if s not in vus:
        vus.add(s)
        for e,d in g.voisins(s):
            if e not in vus:
                parcours_profondeur(g,e,vus)

# Test #

g = Graphe(True,False)
g.ajouter_arc("A","B")
g.ajouter_arc("A","D")
g.ajouter_arc("B","C")
g.ajouter_arc("D","E")
g.ajouter_arc("E","B")
g.ajouter_arc("C","E")
g.ajouter_arc("C","F")
g.ajouter_arc("G","C")

vus = set()
parcours_profondeur(g,"A",vus)
print(vus)

##########

def existe_chemin(g,u,v):
    """renvoie True si un chemin existe dans le graphe g du sommet u vers le sommet v, False sinon"""
    parcours_profondeur(g,u,vus=set())
    return v in vus


# Test #

print(existe_chemin(g,"C","F"))
print(existe_chemin(g,"D","G"))

#########

def parcours_cycle(g, couleurs, s):
    """parcours en profondeur du graphe g à partir de s avec marquage trois couleurs"""
    if couleurs[s]==gris:
        return True
    elif couleurs[s]==noir:
        return False
    else:
        couleurs[s]=gris
        for e,d in g.voisins(s):
            if parcours_cycle(g,couleurs,e):
                return True
        couleurs[s]=noir
        return False

def cycle(g):
    """Renvoie False si g ne contient aucun cycle, True sinon"""
    m=g.sommets()
    couleurs={}
    for k in m:
        couleurs[k]=blanc
    for j in couleurs:
        if parcours_cycle(g,couleurs,j):
            return True
    return False

print(cycle(g))


def parcours_largeur(g, s):
    """parcours en largeur du graphe g depuis le sommet s.
    Renvoie le dictionnaire des distances à partir de s"""
    courant={s};suivant=set();dist={s:0}
    while len(courant)!=0:
        a=courant.pop();v=g.voisins(a)
        for e,j in v:
            if e not in dist: suivant.add(e);dist[e]=dist[a]+1
        if len(courant)==0:courant, suivant=suivant,set()
    return dist

# Test #

s = {4,7,8,9}
t = s.pop()
print(t)
print(s)
help(parcours_largeur)

############

def distance(g,u,v):
    """distance de u à v en nombre d'arcs (et None si pas de chemin)"""
    m=parcours_largeur(g,u)
    if v in m:return m[v]


# Test #

print(distance(g,"A","F"))
print(distance(g,"A","G"))
print(distance(g,"E","B"))