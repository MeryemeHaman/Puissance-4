from render_connect4 import *
from random import randrange
import time

def init (nr=6,nc=7):
    """
    fonction qui cree une grille de case vide par defaut on a une grille de 6 lignes et 7 colonnes
    :param nr: (int) nombre de lignes
    :param nc: (int) nombre de colonnes
    :return: (list) une grille composée de nr lignes et nc colonnes remplie de 0
    :CU: nr>2 et nc>2
    """
    return list( nc*[0] for i in range(nr))

def nr(g):
    """
    fonction qui renvoie le nombre de lignes d'un grille
    :param g: (grille) une grille
    :return: (int) le nombre de ligne de la grille
    :CU: None
    """
    return len(g)

def nc(g):
    """
    fonction qui donne le nombre de colonne de g 
    :param g: (grille) une grille
    :return: (int) le nombre de colonne de la grille
    :CU: None
    """
    if nr(g) == 0:
        return 0
    else:
        return len(g[0])
    
def affiche_jeu (g):
    """
    fonction qui donne un affichage en text du la partie en cours
    :param g: (grille) une grille dont la valeur d'une case vide est 0 une case en rouge 1 et une jaune 2
    :return: (Nonetype) affiche le jeu si le nombre de colonnes et inferieur à 10 et affiche un ’O’ pour un disque rouge, un ’X’ pour un disque jaune et un ’-’ pour une case vide
    :CU: None
    """
    tmp=""
    c=nc(g)
    end=""
    for i in range (nr(g)):
        for j in range (c):
            if g[i][j]==0:
                tmp+="-"
            elif g[i][j]==1:
                tmp+="O"
            else:
                tmp+="X"
            if i == 0: # On a ajouté cette condition comme cela le end aura une chaine de caracteres des chifrres de chaque colonne sans fair une autre boucle for
                end+=str(j)
        tmp+="\n"
    tmp+=c*"="+"\n"+end
    print(tmp)

def colonne_valide (g):
    """
    fonction qui prend la colonne où le joueur veut mettre son jeton et verifie si la colonne et bien valide
    :return: (int) le numéro de la colonne donné par le joueur
    :CU: grille valide
    """
    non_valide=True
    col=nc(g)-1
    c=input("Rentrez la colonne où vous souhaitez mettre votre jeton\n\n")
    if c=='AP1':
        return "b"
    while non_valide: 
        p=int(c) #*
        if not(0<=p<=col and g[0][p]==0 ):
            c=input("Coup non permis \nRentrez une autre colonne s.v.p \n\n")
        else: 
            non_valide=False
    return p

def jouer_coup (g,joueur):
    """
    fonction qui prend la colonne ou le joueur veut mettre son jeton et verifie si la colonne et bien valide puis met le jeton dans la bonne ligne
    :param g: (grille) une grille dont la valeur d'une case vide est 0 une case en rouge 1 et une jaune 2
    :param joueur: (int) 1 ou 2 pour savoir quel joueur joue
    :return: (tuple) renvoie les coordonnes de la case ou le jeton est tombé
    :CU: le joueur et la grille sont valide
    """
    p=colonne_valide (g)
    if p=="b":
        return (-1,-1)
    mg=nr(g)-1
    while g[mg][p]!=0:
        mg=mg-1
    g[mg][p]=joueur
    return (mg,p)

def grille_pas_plein(g):
    """
    fonction qui verifie si la grille est pleine 
    :param g: (grille) une grille valide
    :return: (bool) renvoie True si la grille n'est pas pleine et renvoie False sinon
    :CU: Aucune
    """
    return 0 in g[0]



def grille():
    """
    fonction qui demande au joueur de lui donner la dimmension de la grille avec le numero de la colonne et ligne separe par une virgule verifie l'entree puis cree la grille
    :return: renvoie une grille vide de longeur et largeur preciser par le joueur
    :CU: None
    """
    non_correct=True
    g=input("Rentrez le nombre de ligne et de colonne de votre grille de jeu séparé par une virgule \nSi vous voulez jouer avec les valeurs par defaut appuyersur Entrer\n")
    if g=="":
        grille=init()
    else:
        while non_correct :
            tmp=g.split(",")
            if len(tmp)!=2:
                g=input("La grille que vous avez demandé n'est pas autorisé\nRentrez le nombre de colonne et de ligne de votre grille de jeu séparé par une virgule \nSi vous voulez jouer avec les valeurs par defaut appuyersur Entrer\n")
            else:
                for i in range (2):
                    tmp[i]=int(tmp[i])
                if not(tmp[0]>2 and tmp[1]>2):
                    g=input("La grille que vous avez demandé n'est pas autorisé\nRentrez le nombre de colonne et de ligne de votre grille de jeu séparé par une virgule \nSi vous voulez jouer avec les valeurs par defaut appuyersur Entrer\n")
                else:
                    grille=init(tmp[0],tmp[1])
                    non_correct=False
            if g=="":
                non_correct=False
                grille=init()
    return grille

def cree_lc_h(r,c):
    """
    fonction qui donne les coordonnees des cases horizontales plus ou mois 3 par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases horizontale de plus ou moins 3
    :CU: None
    """
    return list((r,i) for i in range(c-3,c+4))

def cree_lc_v(r,c):
    """
    fonction qui donne les coordonnees des cases horizontales plus ou moins 3 par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases horizontales de plus ou moins 3
    :CU: None
    """
    return list((i,c) for i in range(r-3,r+4))

def cree_lc_d1(r,c):
    """
    fonction qui donne les coordonnees des cases verticales plus ou moins 3 par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases  diagonales de haut en bas de gauche à droite de plus ou moins 3
    :CU: None
    """     
    return list((r+i,c-i) for i in range (3,-4,-1))
                        
def cree_lc_d2(r,c):
    """
    fonction qui donne les coordonnees des cases horizontales plus ou mois 3 par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases les cases diagonales de haut en bas de gauche à droite de plus ou moins 3
    :CU: None
    """     
    return list((r-i,c-i) for i in range (3,-4,-1))

def dans(f,gri):
    """
    fonction qui determine si une coordonnées est bien dans une grille
    :param f: (tuple) la coordonnee de la case sous la forme (numéro de ligne, numéro de colonne)
    :return: (bool) renvoie True si les coordonnees sont correct False sinon
    :CU: None
    """
    return ( 0<=f[0]<nr(gri) and 0<= f[1]<nc(gri))

def tronque_dans(d,gri):
    """
    fonction qui a pour effet d'enlever toutes les coordonnes qui ne sont pas dans grilles
    :param d: (liste de tuple) liste de coordonnes de cases
    :return: (liste de tuple) renvoie une liste avec que les cases qui sont dans la grille
    :CU:None
    """
    res=[]
    for c in d:
        if dans(c,gri):
            res.append(c)
    return res


def is_align4 (lc, g, p):
    """
    fonction qui determine s'il ya un quelconque alignement de 4 pour une case
    :param lc: (liste de tuple) liste de coordonnes de cases
    :param g: (grille) une grille
    :param p: (int) 1 pour le joueur1 et 2 pour le joueur2
    :return: (bool) renvoie True si il y'a un alignement et False sinon
    :CU: None
    """
    lc1=tronque_dans(lc,g)
    comp=0
    res=[]
    for c in lc1:
        if g[c[0]][c[1]] == p:
            comp+=1
        else:
            comp=0
        res.append(comp)
    return 4 in res

def is_win(g,r,c,p) :
    """
    fonction qui determiner si il y aun gagnant dans une partie ou non
    :param r: (int) le numéro de la ligne
    :param c: (int) le numéro de la colonne
    :param g: (grille) une grille
    :param p: (int) 1 pour le joueur1 et 2 pour le joueur2
    :return: (int) renvoie 1 si le joueur 1 gagne 2 si le joueur 2 gagne ou 0 si personne n'a gagné
    :CU: None
    """
    case=(r,c)
    lc_h,lc_v,lc_d1,lc_d2=cree_lc_h(case[0],case[1]),cree_lc_v(case[0],case[1]),cree_lc_d1(case[0],case[1]),cree_lc_d2(case[0],case[1])
    if is_align4 (lc_h, g, p) or is_align4 (lc_v, g, p) or is_align4 (lc_d1, g, p) or is_align4 (lc_d2, g, p):
        return p
    return 0 

def colonne_valide_ia (g,c):
    """
    fonction qui verifie si la colonne choisit par l'ia est valide
    :return: (int) c si la colonne est valide ou -1 sinon
    :CU: Aucune
    """
    col=nc(g)-1
    if 0<=c<=col and g[0][c]==0:
        return c
    else: 
        return -1
    
def ia_aleat(g):
    """
    fonction qui donne le coup de l'ordinateur choisit aleatoirement
    :param g: (grille) grille
    :return: renvoie aléatoirement une colonne c
    :CU: g non vide
    """
    #a=list(ia_aleat(g) for i in range (1000))
    #b=list( i for i in range (1000))
    #import matplotlib.pyplot as plt
    #plt.plot(a,b)
    #plt.show()
    n=nc(g)
    alea=randrange(0,n)
    while colonne_valide_ia(g,alea) == -1:
        alea=randrange(0,n)
    return alea

def jouer_coup_ia (g,p,joueur):
    """
    fonction qui donne les coordonnes de la case où le jeton va tomber
    :param g: (grille) une grille dont la valeur d'une case vide est 0 une case en rouge 1 et une jaune 2
    :param p: 
    :param joueur: (int) 1 ou 2 pour savoir quel joueur joue
    :return: (tuple) renvoie les coordonnes de la case ou le jeton est tombé
    :CU: le joueur et la grille sont valide
    """
    mg=nr(g)-1
    while g[mg][p]!=0:
        mg=mg-1
    g[mg][p]=joueur
    return (mg,p)


def unmove(g,c,l):
    """
    fonction qui supprime le dernier coup jouer
    :param g: (grille) une grille valide
    :param c: (int) indice de la colonne du jeton jouée
    :param l: (int) indice de la ligne du jeton jouée
    :return: (none) modifie la grille en rendant la case de ligne l et de colonne c vide
    :CU: La colonne et le ligne sont valide
    """
    g[l][c]=0

def ia_win(g,p):
    """
    fonction qui determine si le prochain coup de l'ordinateur lui permettra de gagner ou pas
    :param g: (grille) une grille valide
    :param p: (int) 1 pour le joueur 1 ou 2 pour le joueur 2
    :return: (list) renvoie la liste des coup qui permettrons à l'ordinateur de gagné
    :CU: Aucune
    """
    res=[]
    n=nc(g)
    for i in range (n):
        r,c=jouer_coup_ia (g,i,p)
        if is_win(g,r,c,p):
            res.append((r,c))
        unmove(g,c,r)
    res.append(res!=[])
    return res
    
    
def play ():
    """
    Ouvre une fenetre avec un affichage graphique de la partie et donne un affichage simple de la partie dans la console 
    :return: une partie de connect
    :CU: None
    """
    cu=input("Tapez 1 pour jouer avec quelqu'un\nTapez 2 pour jouer contre un ordinateur\nLaissez vide puis appuyer sur Entrer pour laisser l'ordinateur jouer\n")
    gri=grille()
    comp=0
    affiche_jeu(gri)
    draw_connect4(gri)
    r=0
    c=0
    joueur=1
    while grille_pas_plein(gri) and is_win(gri,r,c,joueur)==0 : #*
        if comp%2==0:
            joueur=1
        else:
            joueur=2
        if cu == '1':
            r,c=jouer_coup(gri,joueur)
        elif cu == '2':
            if joueur == 1:
                r,c=jouer_coup(gri,joueur)
            else:
                iawin=ia_win(gri,joueur)
                print(iawin)
                if iawin[-1]:
                    r,c=iawin[0]
                else:
                    r,c=jouer_coup_ia (gri,ia_aleat(gri),joueur)
        elif cu == "":
            r,c=jouer_coup_ia (gri,ia_aleat(gri),joueur)
        if (r,c)==(-1,-1):
            return gri
        affiche_jeu(gri)
        draw_connect4(gri)
        comp+=1
    if not(grille_pas_plein(gri)) :
        print("Draw")
    else:
        print("Le joueur",joueur,"a gagné")
    wait_quit()
    
def score_quad (quad,p):
    """
    fonction qui retourne un score d'un quadruplet pour un joueur
    :param quad: (list) liste de nombre 0 pour case vide 1 pour le joueur 1 et 2 pour le joueur 2
    :param p: (int) 1 pour le joueur 1 et 2 pour le joueur 2
    :return: (int) renvoie un score pour le quadruplet passer en parametre
    :CU: Aucune
    """
    res=0
    case1,case2,case0=(1 in quad),(2 in quad),(0 in quad)
    if (case1 and case2) or (not(case1) and not(case2) and case0):
        return res
    comp1,comp2=1,1
    q,d=1,-1
    for i in range (4):
        if quad[i] == p:
            if comp1 == 2:
                q=q*10
            elif comp1>=3:
                q=q*100
            res=res+q
            comp1+=1
        elif quad[i] != p and quad[i] != 0:
            if comp2 == 2:
                d=d*10
            elif comp2 >=3:
                d=-500
            res=res+d
            comp2+=1
    return res

def cree_h (r,c):
    """
    fonction qui donne les coordonnees des cases horizontales moins 3 par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases horizontales de moins 3
    :CU: None
    """
    return list((i,c) for i in range(r,r+4))

def cree_v (r,c):
    """
    fonction qui donne les coordonnees des cases horizontales plus 3 par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases horizontales de plus 3
    :CU: None
    """
    return list((r,i) for i in range(c,c+4))

def cree_d1 (r,c):
    """
    fonction qui donne les coordonnees des cases diagonales
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases  diagonales de haut en bas de gauche à droite
    :CU: None
    """     
    return list((r+i,c-i) for i in range (0,-4,-1))


def cree_d2 (r,c):
    """
    fonction qui donne les coordonnees des cases diagonales par rapport à la case du jeton
    :param r,c: (int) numéro de la ligne , numéro de la colonne
    :retour: (list) renvoie une liste de tuple des coordonnes des cases les cases diagonales de haut en bas de gauche à droite"""     
    return list((r-i,c-i) for i in range (0,-4,-1))

def analyse_case(r,c,g,p):
    """
    fonction qui retourne le score maximale de la case passé en paramètre
    :param r: (int) le numéro de la ligne
    :param c: (int) le numéro de la colonne
    :param g: (grille) une grille valide
    :param p: (int) 1 pour le joueur 1 2 pour le joueur 2
    :return: (tuple) renvoie le tuple du score maximale de la case dans l'indice 0 l'indice de la ligne dans l'indice 1 du tuple et l'indice colonne dans l'indice 2 du tuple
    :CU: None
    """
    h,v,d1,d2=tronque_dans(cree_h(r,c),g),tronque_dans(cree_v(r,c),g),tronque_dans(cree_d1(r,c),g),tronque_dans(cree_d2(r,c),g)
    tmp1=list(h,v,d1,d2)
    tmp2=list( f for f in tmp1 if len(f)==4)
    tmp3=[]
    tmp5=[]
    for f in tmp2:
        tmp4=list( g[d[0]][d[1]] for d in f)
        tmp3.append(tmp4)
    for f in tmp3:
        tmp5.append(score_quad (f,p))
    return (max(tmp5),r,c)

def analyse_grille (g,p):
    """
    """
    res=[analyse_case(i,j,g,p) for i in range (nr(g)) for j in range (nc(g))]
    res.sort(reverse=True)
    return (res[0][1],res[0][2])


def analyse_grille (g,p):
    i= -1
    nr=nr(g)
    res=[]
    while i>=-nr and ((1 in g[i]) or (2 in g[i])) :
        tmp=list((analyse_case(i,j,g,p)) for j in range (nc(g)))
        res.append(tmp)
        i=i-1
    res.sort(reverse=True)
    return (res[0][1],res[0][2])
            
def play ():
    """
    Ouvre une fenetre avec un affichage graphique de la partie et donne un affichage simple de la partie dans la console 
    :return: une partie de connect
    :CU: None
    """
    cu=input("Tapez 1 pour jouer avec quelqu'un\nTapez 2 pour jouer contre un ordinateur\nLaissez vide puis appuyer sur Entrer pour laisser l'ordinateur jouer\n")
    gri=grille()
    comp=0
    affiche_jeu(gri)
    draw_connect4(gri)
    r=0
    c=0
    joueur=1
    while grille_pas_plein(gri) and is_win(gri,r,c,joueur)==0 : #*
        if comp%2==0:
            joueur=1
        else:
            joueur=2
        if cu == '1':
            r,c=jouer_coup(gri,joueur)
        elif cu == '2':
            if joueur == 1:
                r,c=jouer_coup(gri,joueur)
            else:
                iawin=ia_win(gri,joueur)
                print(iawin)
                if iawin[-1]:
                    r,c=iawin[0]
                else:
                    r,c=jouer_coup_ia (gri,ia_aleat(gri),joueur)
        elif cu == "":
            r,c=jouer_coup_ia (gri,ia_aleat(gri),joueur)
        if (r,c)==(-1,-1):
            return gri
        affiche_jeu(gri)
        draw_connect4(gri)
        comp+=1
    if not(grille_pas_plein(gri)) :
        print("Draw")
    else:
        print("Le joueur",joueur,"a gagné")
    wait_quit()

        
