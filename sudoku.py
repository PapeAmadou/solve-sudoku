from random import*
from numpy import zeros, array
N:int=0
grille=None
def choisir_taille():  #cette fonction demande à l'utilisateur de saisir la taille de la grille souhaitée
    global N
    N=int(input("veuillez saisir la taille souhaitée"))
    print(N)

choisir_taille()

   

#choisir_taille()

#def creer_grille(): #cette fonction nous permet de créer et de retourner la grille
    #N=choisir_taille()
    #grille=zeros((N,N), int)
    #return grille
grille=zeros((N,N), int)

def remplissage(n, N):
    global grille
    while(n>0):
        i=randint(0,N-1)
        j=randint(0,N-1)
        if(grille[i][j]==0):
            grille[i][j]=randint(1,N)
            n-=1

    return grille

print(remplissage(81,N))       

#----------Détection de conflits entre-----------------

def chiffres_ligne(tableau,i):  #cette fonction nous retourne le tableau des nombres de 1 à 9 qui apparaissent sur la ligne d'indice i
    global N
    global grille
    n=0
    for j in range(N):
        if(tableau[i][j]!=0):
            n+=1
    #print(n)
    ligne=zeros(n,int)
    k=0
    for j in range(N):
        if(tableau[i][j]!=0):
            ligne[k]=tableau[i][j]
            k+=1
    return ligne

#print(chiffres_ligne(grille,3))
def correct_ligne(ligne):   #cette fonction nous permet de savoir si une ligne ne  contient pas deux fois le même chiffre
    global N
    bool=True
    for i in range(0,N-1):
        for j in range(i+1,N):
            if(ligne[i]==ligne[j] and ligne[i]!=0):
                return False
    return bool
def correct_bloc(tableau,i,j):
    block=[ ]
    bool=True
    for m in range(3*(i//3),3*((i)//3)+3):
        for n in range(3*((j//3)),3*((j//3))+3):
            block.append(tableau[m][n])
    #print(block)
    for l in range(len(block)):
        if(correct_ligne(block)==False):
            return False
    return bool

'''print(correct_bloc(grille,0,0))
print(correct_bloc(grille,4,0))'''

    
    
            

def correct(tableau):   # cette fonction 
    global N
    global grille
    bool=True
    liste=[ ]
    for i in range(0,N):
        if(correct_ligne(tableau[i])==False):
            return False
    for k in range(0,N):
            for m in range(len(tableau[:,k])):
                liste.append(tableau[:,k][m])
            
            if(correct_ligne(liste)==False):
                return False
            liste.clear()
    a=0
    
    while(a<N):
        b=0
        while(b<N):
    
            correct_bloc(grille,a,b)
        a+=sqrt(N)
    return bool
        
        
                   
'''print(correct_ligne(grille[0]))
print(correct_ligne(grille[1]))
print(correct_ligne(grille[2]))
print(correct_ligne(grille[3]))
print(correct_ligne(grille[4]))
print(correct_ligne(grille[5]))
print(correct_ligne(grille[6]))
print(correct_ligne(grille[7]))
print(correct_ligne(grille[8]))
#print(grille[:,1])'''
#print(correct(grille))





def chiffres_colonne(tableau,j): #cette fonction nous retourne le tableau des nombres de 1 à 9 qui apparaissent sur la colonne d'indice i
    global N
    n=0
    for i in range(N):
        if(tableau[i][j]!=0):
            n+=1
    #print(n)
    colonne=zeros(n,int)
    k=0
    for i in range(N):
        if(tableau[i][j]!=0):
            colonne[k]=tableau[i][j]
            k+=1
            
    return colonne

#print(chiffres_colonne(grille,2))


def chiffres_bloc(tableau, i, j):  #cette fonction nous retourne le tableau des chiffres apparaissant dans un bloc de "N/2 x N/2"
    global N
    count=0
    
    for m in range(3*(i//3),3*((i)//3)+3):
        for n in range(3*((j//3)),3*((j//3))+3):
            if(tableau[m][n]!=0):
                count+=1
           
    #print(count)
    block=zeros(count,int)
    k=0
    for m in range(3*((i)//3),3*((i)//3)+3):
        for n in range(3*((j//3)),3*((j//3))+3):
            if(tableau[m][n]!=0):
                block[k]=tableau[m][n]
                k+=1
            
    return block
#print(chiffres_bloc(grille, 7,4))

def chiffres_conflits(tableau,i,j):   #cette fonction nous retourne la liste des valeurs qu'on ne peut pas mettre à la case (i,j)

    conflit=[ ]
   
    ligne=chiffres_ligne(tableau,i)
    colonne=chiffres_colonne(tableau,j)
    block=chiffres_bloc(tableau,i,j)
    if(tableau[i][j]==0):
        for m in range(len(ligne)):
            for n in range(len(colonne)):
                if(colonne[n]==ligne[m]):
                    conflit.append(colonne[n])
        for a in range(len(ligne)):
            for b in range(len(block)):
                if(ligne[a]==block[b]):
                    conflit.append(ligne[a])
        for c in range(len(colonne)):
            for d in range(len(block)):
                if(colonne[c]==block[d]):
                    conflit.append(colonne[c])
        print(ligne)
        print(colonne)
        print(block)
    return conflit

'''print(chiffres_conflits(grille,2,3))
print(chiffres_conflits(grille,1,5))
print(chiffres_conflits(grille,7,2))'''

#-------------Passage à la case suivante------------------------
def case_suivante(i,j):  #cette fonction retourne les coordonnées (i,j) de la case suivante qu'on peut remplir
    global N
    global grille
    liste=[ ]
    if(i==8 and j==8):
        liste.append(9)
        liste.append(0)
        return liste
    else:
        for m in range(i,N):
            for n in range(j,N):
                if(grille[m][n]==0):
                    liste.append(m)
                    liste.append(n)
                    return liste


'''print(case_suivante(0,0))
print(case_suivante(8,8))
print(case_suivante(5,3))'''






