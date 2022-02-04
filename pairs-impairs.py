tailleListe = int(input("Saisir le nombre d'éléments de votre liste :"))
liste = []
listePair = []
listeImpair = []

i=0
while i < tailleListe :
    i=i+1
    print("saisir l'élément (entier)",i,"de la liste : ")
    liste.append (int(input()))
while i < tailleListe :
    if liste[i] % 2 == 0 :
        listePair.append(len(liste))
    else :
        listeImpair.append(len(liste))

    
print("Pairs : ", listePair)
print("Impairs:", listeImpair)
