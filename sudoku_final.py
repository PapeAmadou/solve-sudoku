from math import*
from random import*
from numpy import zeros, array
import sys
import pygame
N:int=0
nb_cases:int=0
grille=None
grille_sol=None

def choisir_taille():  #cette fonction demande à l'utilisateur de saisir la taille de la grille souhaitée
    global N
    global nb_cases
    N=int(input("veuillez saisir la taille souhaitée"))
    print("--------------------------------------")
    '''nb_cases=int(input("Combien de cases voudriez-vous que l'on remplis svp ?"))
    if(nb_cases>=60):
        print("Vous avez choisi le niveau facil")
    if(nb_cases<60 and nb_cases>=30):
        print("Vous avez choisis le niveau moyen")
    if(nb_cases<30):
        print("Vous avez choisis le niveau difficile")'''


choisir_taille()
   

#choisir_taille()

#def creer_grille(): #cette fonction nous permet de créer et de retourner la grille
    #N=choisir_taille()
    #grille=zeros((N,N), int)
    #return grille
grille=zeros((N,N), int)
grille_sol=zeros((N,N), int)


#----------Detection de conflits entre-----------------

def chiffres_ligne(tableau,i):  #cette fonction nous retourne le tableau des nombres de 1 a 9 qui apparaissent sur la ligne d'indice i
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
    global N
    block=[ ]
    result=True
    a=int(sqrt(N))
    for m in range(a*(i//a),a*((i)//a)+a):
        for n in range(a*(j//a),a*(j//a)+a):
            block.append(tableau[m][n])
    #print(block)
    for l in range(len(block)):
        if(correct_ligne(block)==False):
            return False
    return result

'''print(correct_bloc(grille,0,0))
print(correct_bloc(grille,4,0))'''

    
    
            

def correct(tableau):   # cette fonction 
    global N
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
    a:int=0
    n:int=N
    
    while(a<n):
        b=0
        while(b<n):
    
            if(correct_bloc(tableau,a,b))==False:
                return False
            b+=int(sqrt(N))
            
        a+=int(sqrt(N))
       
    return True

def absents_ligne(tableau):
    global N
    ligne=[ ]
    for i in range(1,N+1):
        ligne.append(i)
    for j in range(len(tableau)):
        if(tableau[j] in ligne):
            ligne.remove(tableau[j])
    
    return ligne

def absent_block(tableau,i,j):
    global N
    block=[ ]
    a=int(sqrt(N))
    for m in range(a*(i//a),a*((i)//a)+a):
        for n in range(a*(j//a),a*(j//a)+a):
            block.append(tableau[m][n])

    ligne=absents_ligne(block)
    return ligne



def intersect(u,v):
    ligne=[ ]
    for i in range(len(u)):
        if(u[i] in v):
            ligne.append(u[i])
    return ligne

def val_possible(tableau,i,j):
    global N
    liste=[ ]
    ligne=absents_ligne(tableau[i])
    #print(ligne)

    for m in range(N):
        liste.append(tableau[m][j])

    colonne=absents_ligne(liste)
    #print(colonne)
    block=absent_block(tableau,i,j)
    #print(block)
    intersection=intersect(ligne,colonne)
    #print(intersection)
    return intersect(intersection,block)





def remplissage(n, N):
    global grille
    while(n>0):
        i=randint(0,N-1)
        j=randint(0,N-1)
        if(grille[i][j]==0):
            
            grille[i][j]=randint(1,N)
            if(correct(grille)==False):
                grille[i][j]=0
            else:
                n-=1

    return grille

 

def genere_grille():
    global grille
    global N
    global nb_cases
    n=N*N-nb_cases
    while(n>0):
        i=randint(0,N-1)
        j=randint(0,N-1)
        if(grille[i][j]!=0):
            grille[i][j]=0
            n-=1
    return grille



'''print(absents_ligne(grille[0]))
print(absents_ligne(grille[1]))
print(absents_ligne(grille[2]))
print(absents_ligne(grille[3]))'''
#print(absent_block(grille,0,0))
#print(val_possible(grille,0,0))
'''print(val_possible(grille,0,0))
print(val_possible(grille,3,0))
print(val_possible(grille,6,0))'''

        
        
                   
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
    a=int(sqrt(N))
    
    for m in range(a*(i//a),a*((i)//a)+a):
        for n in range(a*((j//a)),a*((j//a))+a):
            if(tableau[m][n]!=0):
                count+=1
           
    #print(count)
    block=zeros(count,int)
    k=0
    for m in range(a*(i//a),a*((i)//a)+a):
        for n in range(a*((j//a)),a*((j//a))+a):
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
        '''print(ligne)
        print(colonne)
        print(block)'''
    return conflit
def ajout_valeur(tableau,val,i,j):
        tableau[i][j]=val
'''print(chiffres_conflits(grille,2,3))
print(chiffres_conflits(grille,1,5))
print(chiffres_conflits(grille,7,2))'''

#-------------Passage à la case suivante------------------------
'''def case_suivante(i,j):  #cette fonction retourne les coordonnées (i,j) de la case suivante qu'on peut remplir
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
                    return liste'''


'''print(case_suivante(0,0))
print(case_suivante(8,8))
print(case_suivante(5,3))'''
def trouve_zero(tableau):
    global N
    resultat=[-1,-1]
    longueur=N+1
    for i in range(N):
        for j in range(N):
            #print(val_possible(tableau,i,j))
            if(tableau[i][j]==0 and len(val_possible(tableau,i,j))<longueur):
                liste=val_possible(tableau,i,j)
                longueur=len(val_possible(tableau,i,j))
                resultat=[i,j]
                #print(resultat)
                #print(liste)

    return resultat

#print(trouve_zero(grille))

def resoudre_grille():
    global N
    global grille
    
    if(correct(grille)):
        ligne=trouve_zero(grille)
        if (ligne[0]==-1):
            return True
        else:
            i, j=ligne[0], ligne[1]
            for n in range(1,N+1):
                grille[i][j]=n
                if(resoudre_grille()):
                    return True
                grille[i][j]=0
    return False       
def grille_resolue(tableau):
    global N
    for i in range(0,N):
        for j in range(0,N):
            if tableau[i][j]==0:
                return False
    return True

    
#----------------------Programme principal----------------------------




fichier = open("grille_sudoku_resolue.txt", "w")
for ligne in grille:
    ligne_str = " ".join(map(str, ligne))  # Convertit les nombres en chaînes de caractères
    fichier.write(ligne_str + "\n")

fichier.close()

fichier = open("grille_sudoku_resolue.txt", "r")
print (fichier.read())
fichier.close()



def programme_principal():
    remplissage(1,N)
    resoudre_grille()
    for i in range(0, N):
        for j in range(0, N):
            grille_sol[i][j] = grille[i][j]
    genere_grille()

#-----------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------

pygame.init()
#definition des tailles, couleurs et police d ecriture
color_facile = (0, 0, 0)
color_moyen = (0, 0, 0)
color_difficile = (0, 0, 0)
color_diabolique = (0, 0, 0)
taille_ecran_menu = [800*0.66, 800*0.66]
taille_ecran_menu_difficulte = [800*0.66, 800*0.66]
taille_ecran_sudoku = [800*0.66, 800*0.66]
taille_sudoku = [600*0.66,600*0.66]
background_color =  (105, 105, 105)
background_color_selection = (0, 58, 58)
taille_police = int(65*0.66)
taille_police_titre = int(80*0.66)
taille_police_button = int(25*0.66)
taille_police_chiffre = int(60*0.66)
taille_police_copyright = int(35*0.66)
police_ecriture_menu = pygame.font.SysFont('Didot', taille_police)
police_ecriture_copyright = pygame.font.SysFont('Times New Roman', taille_police_copyright)
police_ecriture_sudoku = pygame.font.SysFont('Comic sans ms', taille_police_titre)
police_ecriture_button = pygame.font.SysFont('Comic sans ms', taille_police_button)
police_ecriture_chiffre = pygame.font.SysFont('Didot', taille_police_chiffre)
violet = (110, 5, 255)
noir = (0, 0, 0)
blanc = (255, 255, 255)
coor_jouer = (80, 80, 150, 80)
COLOR_HIGHLIGHT=(255, 0, 0)
Turquoise =(64, 224, 208)
rouge = (255, 0, 0)
blue = (0, 0, 255)
vert = (0, 255, 0)
rouge_clair = (255, 100, 100)
gris_clair = (200, 200, 200)
jaune_orange = (255, 127, 0)
jaune = (255, 255, 120)
grid=zeros((N,N),int)
"""for i in range(0,N):
    for j in range (0,N):
        grid[i][j]=grille[i][j]"""
x = 0
y = 0
dif = taille_sudoku[0]// 9
val = 0
"""def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif"""
def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
#Fill value entered in cell
"""def draw_val(val):
    global dif
    text1 =police_ecriture_chiffre.render(str(val), True, noir)
    ecran.blit(text1, (x * dif + 15, y * dif + 15))"""


#definition des differentes classes

class Interface:
    def __init__(self, taille_ecran_menu, police_ecriture_menu, background_color):  # Constructeur de la classe
        self.ecran = pygame.display.set_mode(taille_ecran_menu)
        self.police_ecriture_menu = police_ecriture_menu
        self.background_color = background_color
        self.ecran.fill(background_color)


class Menu(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_jouer,
                 color_quitter):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_jouer = color_jouer
        self.color_quitter = color_quitter
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, vert)
        self.ecran.blit(value, (220*0.66, 50*0.66))
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, (50,50,50))
        self.ecran.blit(value, (230*0.66, 50*0.66))

        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu[1] // 2 - 100, 200*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu[1] // 2 - 100, 350*0.66, 300*0.66, 100*0.66], 0)
        #value = police_ecriture_menu.render(str("Jouer"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 80*0.66 - 100, 225*0.66))
        value = police_ecriture_menu.render(str("Jouer"), True, self.color_jouer)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 85*0.66 - 100, 225*0.66 + 3))

        #value = police_ecriture_menu.render(str("Quitter"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65*0.66 - 100, 375*0.66))
        value = police_ecriture_menu.render(str("Quitter"), True, self.color_quitter)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70*0.66 - 100, 375*0.66 + 3))
        #value = police_ecriture_copyright.render(str("Léo Emmanuel Diouf & Pape Amadou Ndao"), True, (0,0,0))
        #self.ecran.blit(value, (taille_ecran_menu[1]//2 - 303*0.66, taille_ecran_menu[0] - 50))
        value = police_ecriture_copyright.render(str("Léo Emmanuel Diouf & Pape Amadou Ndao"), True, Turquoise)
        self.ecran.blit(value, (taille_ecran_menu[1]//2 - 250*0.66, taille_ecran_menu[0] - 100))
        
        # Rectangle du bouton "Jouer"
        self.rect_jouer = pygame.Rect(taille_ecran_menu[1] // 2 - 100, 200*0.66, 300*0.66, 100*0.66)
        self.rect_quitter=pygame.Rect(taille_ecran_menu[1] // 2 - 100, 350*0.66, 300*0.66, 100*0.66)
        

    def handle_events(self):
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche de la souris
                        if self.rect_jouer.collidepoint(event.pos):
                            # Transition vers le Menu_mode
                            menu_mode = Menu_mode(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku,
                                                background_color, rouge, blanc)
                            menu_mode.handle_events()

                        elif self.rect_quitter.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                                    
                pygame.display.flip()            



class Menu_mode(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_importer,
                 color_generer):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_importer = color_importer
        self.color_generer = color_generer
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, vert)
        self.ecran.blit(value, (220*0.66, 50*0.66))
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, (50,50,50))
        self.ecran.blit(value, (230*0.66, 50*0.66))
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu[1] // 2 - 100, 300*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu[1] // 2 - 100, 450*0.66, 300*0.66, 100*0.66], 0)
        #value = police_ecriture_menu.render(str("Générer"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65*0.66 - 100, 225*0.66))
        value = police_ecriture_menu.render(str("Générer"), True, blue)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70*0.66 - 100, 325*0.66 + 3))
        value = police_ecriture_menu.render(str("Charger"), True, blue)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2+ 70*0.66 - 100, 475*0.66+3))

        """value = police_ecriture_menu.render(str("Générer"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 65*0.66 - 100, 375*0.66))
        value = police_ecriture_menu.render(str("Générer"), True, self.color_generer)
        self.ecran.blit(value, (taille_ecran_menu[1] // 2 + 70*0.66 - 100, 375*0.66 + 3))
"""
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_menu[0] - 100*0.66, taille_ecran_menu[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_menu[0] - 95*0.66, taille_ecran_menu[1] - 35*0.66))
        
        self.rect_retour=pygame.Rect(taille_ecran_menu[0] - 100*0.66, taille_ecran_menu[1] - 30*0.66, 100*0.66, 30*0.66)
        self.rect_importer=pygame.Rect([taille_ecran_menu[1] // 2 - 100, 300*0.66, 300*0.66, 100*0.66])
        self.rect_charger=pygame.Rect([taille_ecran_menu[1] // 2 - 100, 450*0.66, 300*0.66, 100*0.66])

    def handle_events(self):
        global grid
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche de la souris
                        if self.rect_retour.collidepoint(event.pos):
                            menu=Menu(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, rouge, blue)
                            menu.handle_events()
                        if self.rect_importer.collidepoint(event.pos):
                            difficult=Menu_difficulte(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_facile,
                                    color_moyen, color_difficile, color_diabolique)
                            difficult.handle_events()
                        if self.rect_charger.collidepoint(event.pos):

                            """# Ouvrir le fichier texte et lire son contenu
                            with open('grille_sudoku_resolue.txt', 'r') as fichier:
                                contenu = fichier.read()
                            import os

                            # Obtenir le répertoire courant du script
                            repertoire_courant = os.getcwd()

                            # Chemin du fichier texte
                            chemin_fichier = os.path.join(repertoire_courant, "grille_sudoku_resolue.txt")
                            with open(chemin_fichier, "r") as fichier:"""
                            fichier = open("C:/Users/Emma_df08/Documents/Pycharm Projects/grille_sudoku_resolue.txt","r")
                            contenu = fichier.read()
                            # Séparer les éléments du fichier
                            elements = contenu.split()

                            # Vérifier que le nombre d'éléments est cohérent avec une grille Sudoku 9x9
                            if len(elements) != 81:
                                print("Erreur: Le fichier ne contient pas une grille Sudoku valide.")
                                return

                            # Remplir la grille 2D avec les éléments extraits
                            for i in range(9):
                                for j in range(9):
                                    index = i * 9 + j
                                    grid[i][j] = int(elements[index])

                            # Utiliser la grille Sudoku avec Pygame
                            # Par exemple, afficher la grille
                            importer = SudokuImporter(taille_ecran_sudoku, grid, nombrevie=None)
                            importer.jouer()
                            #print(grid)


                pygame.display.flip()
                            


class Menu_difficulte(Interface):
    def __init__(self, taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, color_facile,
                 color_moyen, color_difficile, color_diabolique):
        super().__init__(taille_ecran_menu, police_ecriture_menu, background_color)
        self.color_facile = color_facile
        self.color_moyen = color_moyen
        self.color_difficile = color_difficile
        self.color_diabolique = color_diabolique
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, vert)
        self.ecran.blit(value, (220*0.66, 50*0.66))
        value = police_ecriture_sudoku.render(str("SUDOKU"), True, (50,50,50))
        self.ecran.blit(value, (230*0.66, 50*0.66))
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu_difficulte[1] / 3.2, 200*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu_difficulte[1] / 3.2, 350*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu_difficulte[1] / 3.2, 500*0.66, 300*0.66, 100*0.66], 0)
        pygame.draw.ellipse(self.ecran, Turquoise, [taille_ecran_menu_difficulte[1] / 3.2, 650*0.66, 300*0.66, 100*0.66], 0)

        #value = police_ecriture_menu.render(str("Facile"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80*0.66, 225*0.66))
        value = police_ecriture_menu.render(str("Facile"), True, self.color_facile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85*0.66, 225*0.66 + 3))

        #value = police_ecriture_menu.render(str("Moyen"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 80*0.66, 375*0.66))
        value = police_ecriture_menu.render(str("Moyen"), True, self.color_moyen)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 85*0.66, 375*0.66 + 3))

        #value = police_ecriture_menu.render(str("Difficile"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 65*0.66, 525*0.66))
        value = police_ecriture_menu.render(str("Difficile"), True, self.color_difficile)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 70*0.66, 525*0.66 + 3))

        #value = police_ecriture_menu.render(str("Diabolique"), True, noir)
        #self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + 30*0.66, 675*0.66))
        value = police_ecriture_menu.render(str("Diabolique"), True, self.color_diabolique)
        self.ecran.blit(value, (taille_ecran_menu_difficulte[1] / 3.2 + +35*0.66, 675*0.66 + 3))

        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 95*0.66, taille_ecran_sudoku[1] - 35*0.66))
        self.rect_retour=pygame.Rect(taille_ecran_menu[0] - 100*0.66, taille_ecran_menu[1] - 30*0.66, 100*0.66, 30*0.66)
        self.rect_facil=pygame.Rect([taille_ecran_menu_difficulte[1] / 3.2, 200*0.66, 300*0.66, 100*0.66])
        self.rect_moyen=pygame.Rect([taille_ecran_menu_difficulte[1] / 3.2, 350*0.66, 300*0.66, 100*0.66])
        self.rect_difficil=pygame.Rect([taille_ecran_menu_difficulte[1] / 3.2, 500*0.66, 300*0.66, 100*0.66])
        self.rect_diabolique=pygame.Rect([taille_ecran_menu_difficulte[1] / 3.2, 650*0.66, 300*0.66, 100*0.66])
        
    def handle_events(self):
        global nb_cases
        global grid
        running = True
        while running:
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche de la souris
                        if self.rect_facil.collidepoint(event.pos):
                            nb_cases=40
                            programme_principal()
                            for i in range(0, N):
                                for j in range(0, N):
                                    grid[i][j] = grille[i][j]
                            importer=SudokuImporter(taille_ecran_sudoku, grid, nombrevie=None)
                            #print(grille_sol)
                            importer.jouer()
                        if self.rect_moyen.collidepoint(event.pos):
                            nb_cases=33
                            programme_principal()
                            for i in range(0, N):
                                for j in range(0, N):
                                    grid[i][j] = grille[i][j]
                            importer=SudokuImporter(taille_ecran_sudoku, grid, nombrevie=None)
                            importer.jouer()
                        if self.rect_difficil.collidepoint(event.pos):
                            nb_cases=30
                            programme_principal()
                            for i in range(0, N):
                                for j in range(0, N):
                                    grid[i][j] = grille[i][j]
                            importer = SudokuImporter(taille_ecran_sudoku, grid, nombrevie=None)
                            importer.jouer()
                        if self.rect_diabolique.collidepoint(event.pos):
                            nb_cases=20
                            programme_principal()
                            for i in range(0, N):
                                for j in range(0, N):
                                    grid[i][j] = grille[i][j]
                            importer = SudokuImporter(taille_ecran_sudoku, grid, nombrevie=None)
                            importer.jouer()
                        elif self.rect_retour.collidepoint(event.pos):
                            menu_mode=Menu_mode(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, rouge,
                 blanc)
                            menu_mode.handle_events()
                pygame.display.flip()


class Sudoku(Interface):
    def __init__(self, taille_ecran_sudoku, grid, nombrevie=None):
        super().__init__(taille_ecran_sudoku, police_ecriture_menu, background_color)
        self.grid = grid
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 5)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 5)
            else:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 1)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 1)
        """# bouton retour
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 95*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # bouton solve
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 210*0.66, taille_ecran_sudoku[1] - 30*0.66, 110*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Résoudre"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 210*0.66, taille_ecran_sudoku[1] - 35*0.66))"""


        # affiche la grille de sudoku
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != 0:
                    value = police_ecriture_chiffre.render(str(self.grid[i][j]), True, noir)
                    self.ecran.blit(value, (100*0.66 + (j + 0.35) * taille_sudoku[0] // 9, 100*0.66 + ( i + 0.25 ) * taille_sudoku[1] // 9))
class SudokuImporter(Interface):
    
    def __init__(self, taille_ecran_sudoku, grid, nombrevie=None):
        super().__init__(taille_ecran_sudoku, police_ecriture_menu, background_color)
        self.grid = grid
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 5)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 5)
            else:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 2)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 2)
        # bouton retour
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Retour"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 90*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # bouton solve
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 225*0.66, taille_ecran_sudoku[1] - 30*0.66, 110*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Résoudre"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 225*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # bouton importer
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 390*0.66, taille_ecran_sudoku[1] - 30*0.66, 160*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Sauvegarder"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 385*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # affiche la grille de sudoku
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != 0:
                    value = police_ecriture_chiffre.render(str(self.grid[i][j]), True, noir)
                    self.ecran.blit(value, (100*0.66 + (j + 0.35) * taille_sudoku[0] // 9, 100*0.66 + ( i + 0.25 ) * taille_sudoku[1] // 9))
        value = police_ecriture_button.render(str(" Appuyer sur 0 pour effacer une valeur entrée au clavier "), True, Turquoise)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 715 * 0.66, taille_ecran_sudoku[1] - 95 * 0.66))
        self.rect_retour=pygame.Rect(taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66)
        self.rect_resoudre = pygame.Rect(taille_ecran_sudoku[0] - 225*0.66, taille_ecran_sudoku[1] - 30*0.66, 110*0.66, 30*0.66)
        self.rect_sauvegarder=pygame.Rect((taille_ecran_sudoku[0] - 390*0.66, taille_ecran_sudoku[1] - 30*0.66, 160*0.66, 30*0.66))
    def draw_grid(self):
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 5)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 5)
            else:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 2)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 2)

    def jouer(self):
        global val
        global x
        global y
        global dif
        global nb_cases
        global grille
        running = True
        while running:
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    x = (pos[0]-100*0.66)//dif
                    y = (pos[1]-100*0.66)//dif
                    if x>=0 and x<9 and y>=0 and y<9:
                        self.draw_grid()
                        pygame.draw.rect(self.ecran, Turquoise,(100 * 0.66 + x * dif, 100 * 0.66 + y * dif, dif+1, dif+1), 1)
                    if self.rect_retour.collidepoint(event.pos):
                        difficult = Menu_difficulte(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku,
                                                    background_color, color_facile,
                                                    color_moyen, color_difficile, color_diabolique)
                        difficult.handle_events()
                    if self.rect_resoudre.collidepoint(event.pos):
                        sudoku_sol=Sudoku(taille_ecran_sudoku, grille_sol, nombrevie=None)
                    if self.rect_sauvegarder.collidepoint(event.pos):
                        """fichier = open("grille_sudoku_resolue.txt", "w")
                        for ligne in grid:
                            ligne_str = " ".join(map(str, ligne))  # Convertit les nombres en chaînes de caractères
                            fichier.write(ligne_str + "\n")

                        fichier.close()"""
                        import os

                        # Obtenir le répertoire courant du script
                        repertoire_courant = os.getcwd()

                        # Chemin du fichier texte
                        chemin_fichier = os.path.join(repertoire_courant, "grille_sudoku_resolue.txt")

                        # Ouvrir le fichier en mode écriture
                        with open(chemin_fichier, "w") as fichier:
                            for ligne in grid:
                                ligne_str = " ".join(map(str, ligne))
                                fichier.write(ligne_str + "\n")
                        menu = Menu(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color,
                                    noir, noir)
                        menu.handle_events()

                if event.type == pygame.KEYDOWN:
                    """if event.key == pygame.K_LEFT:
                        x -= 1
                    if event.key == pygame.K_RIGHT:
                        x += 1
                    if event.key == pygame.K_UP:
                        y -= 1
                    if event.key == pygame.K_DOWN:
                        y += 1"""
                    if event.key == pygame.K_1:
                        val = 1
                    if event.key == pygame.K_2:
                        val = 2
                    if event.key == pygame.K_3:
                        val = 3
                    if event.key == pygame.K_4:
                        val = 4
                    if event.key == pygame.K_5:
                        val = 5
                    if event.key == pygame.K_6:
                        val = 6
                    if event.key == pygame.K_7:
                        val = 7
                    if event.key == pygame.K_8:
                        val = 8
                    if event.key == pygame.K_9:
                        val = 9
                    if event.key == pygame.K_0:
                        val=0
                    if x<9 and y<9 and x>=0 and y>=0:
                        """self.draw_grid()
                        pygame.draw.rect(self.ecran, Turquoise,(100 * 0.66 + x * dif, 100 * 0.66 + y * dif, dif + 1, dif + 1), 1)
                        self.pos[0] = x * dif + 100 * 0.66
                        self.pos[1] = y * dif + 100 * 0.66"""
                        if val != 0 and grid[int(y)][int(x)]==0:
                            ajout_valeur(grid,val,int(y),int(x))
                            if correct(grid)==True:
                                text1 =police_ecriture_chiffre.render(str(val), True, noir)
                                self.ecran.blit(text1, ((100*0.66+x * dif+15),(100*0.66+y * dif+15 )))
                            else:
                                ajout_valeur(grid,0, int(y), int(x))
                        if val==0 and grille[int(y)][int(x)]==0:
                            pygame.draw.rect(self.ecran, background_color, (int(100 * 0.66 + int(x) * int(dif)+5 ), int(100 * 0.66 + int(y) * int(dif)+5 ),int(dif)-10, int(dif)-10))
                            grid[int(y)][int(x)]=0
                if grille_resolue(grid):
                    termine=Menu_termine(taille_ecran_sudoku, grid)
                    termine.handle_events()
                pygame.display.flip()


class Menu_termine(Interface):
    def __init__(self, taille_ecran_sudoku, grid):
        super().__init__(taille_ecran_sudoku, police_ecriture_menu, background_color)
        self.grid = grid
        for i in range(0, 10):
            if i % 3 == 0:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 5)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 5)
            else:
                pygame.draw.line(self.ecran, noir, (100*0.66, 100*0.66 + i * taille_sudoku[1] // 9),
                                 (100*0.66 + 9 * taille_sudoku[0] // 9, 100*0.66 + i * taille_sudoku[1] // 9), 1)
                pygame.draw.line(self.ecran, noir, (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66),
                                 (100*0.66 + i * taille_sudoku[0] // 9, 100*0.66 + 9 * taille_sudoku[1] // 9), 1)
        # bouton quitter
        pygame.draw.rect(self.ecran, gris_clair, (taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66), 0)
        value = police_ecriture_button.render(str("Quitter"), True, noir)
        self.ecran.blit(value, (taille_ecran_sudoku[0] - 90*0.66, taille_ecran_sudoku[1] - 35*0.66))
        # affiche la grille de sudoku
        for i in range(0, 9):
            for j in range(0, 9):
                if self.grid[i][j] != 0:
                    value = police_ecriture_chiffre.render(str(self.grid[i][j]), True, noir)
                    self.ecran.blit(value, (100*0.66 + (j + 0.35) * taille_sudoku[0] // 9, 100*0.66 + ( i + 0.25 ) * taille_sudoku[1] // 9))
        self.rect_quitter=pygame.Rect(taille_ecran_sudoku[0] - 100*0.66, taille_ecran_sudoku[1] - 30*0.66, 100*0.66, 30*0.66)
    def handle_events(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Clic gauche de la souris
                        if self.rect_quitter.collidepoint(event.pos):
                            pygame.quit()
                            sys.exit()
                pygame.display.flip()
        
        


if N==9:
    menu=Menu(taille_ecran_menu, police_ecriture_menu, police_ecriture_sudoku, background_color, noir, noir)
    menu.handle_events()
else:
    print("L'interface graphique n'a été configurée que pour les grilles 9x9 mais nous vous affichons une grille remplie")
    programme_principal()
    print(grille_sol)
