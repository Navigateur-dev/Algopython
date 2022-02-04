def depot(n):
    somme = 1
    for i in range (1,n):
        somme = somme + 1.01
    return somme
print (depot(4))
print(depot(1))
print(depot(8))

def jour(n):
    jours=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
    jour = 0
#    semaine = 0
    affiche = ""
    for i in range (1,n):
        jour = jour + 1
        if jour >= 7:
#            semaine = semaine + 1
            jour = 0
            affiche = jours[jour]
        else :
            affiche = jours[jour]
    return affiche
print(jour(2))
print(jour(12))
print(jour(25))

def contenu(n):
    total= 0
    tire = 1
    for i in range (1,n+1):
        total += depot(i)
        

    return total
print(contenu(8))
print(contenu(3))

        
        