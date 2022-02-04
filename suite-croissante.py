L = []
i = 10
for i in range (0,10) :
    L.append(i**2+1) 

croissante = True
p = len(L)
for i in range (1,p):
    if L[i] < L[i-p] :
        croissante = False
print(croissante)
print(i)
print(L)
