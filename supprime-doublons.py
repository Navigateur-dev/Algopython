"Nombre d'élément tab"

nb = int(input("saisir le nombre d'éléments de votre liste : "))
liste = []

"Comptage et saisie dans la liste"
i = 0

while i < nb :
    i=i+1
    
    print("saisir l'élément (entier)",i,"de la liste : ")
    liste.append (int(input()))


'Trie'
listeTrie = []
for i in range (nb):
    if liste[i] not in listeTrie:
        listeTrie.append(liste[i])
listeTrie.sort()
'Affiche'
print("Liste initiale : ", liste)
print("Liste traité :", listeTrie)
        
