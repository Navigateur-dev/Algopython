def saisie_liste_entiers(n) :
    """ Permet la saisie de n entiers séparés par un espace et retourne
        ces n entiers sous la forme d'une liste
        
        Paramètre:
            n (int) : nombre d'éléments à saisir
            
        Valeur de retour: liste des entiers saisis au clavier ou False en cas
            d'erreur (nombre ou type des valeurs saisies incorrect)
    """
    chaine = input("")
    # Récupère les valeurs saisies séparées par un espace dans une liste de chaines
    les_nombres = chaine.split()
    ## Vérifie que le nombre de valeurs saisies correspond au nombre attendu
    if len(les_nombres) != n :
        return False
    # Crée une liste vide pour y stocker les entiers
    liste = []
    for i in range(n):
        try:
            liste.append(int(les_nombres[i]))
        except ValueError:
            # en cas d'erreur lors de la conversion de la valeur saisie en int
            return False
    return liste
             
             
def affiche_matrice(matrice) :
    """ Affiche la matrice passée en paramètre
    
    Paramètre:
        L (list[list[int]]) : matrice à afficher      
    """
    
    for i in range(len(L)):
        # partie à compléter
        for j in range(len(L[i])):
            print(L[i][j], end='')
    print()
    
L = [[1, 5, 3, 1],[0,4,3,3],[4,2,1,2]]
