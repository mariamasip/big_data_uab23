#cadenes
"això és una cadena"
"això és 'una cadena'"
'això és una cadena'
'Això "és" una cadena'
#nums
1
1.3

#variable
var = 1
print(var)

var2 = 1+4
print(var2)

usuari = "Ibai Llanos"
likes = 100
#print("L'usuari", usuari, "té", likes, "likes")

#conversio likes en una cadena de text
#frase_final = "L'usuari", +usuari+, "té",+ str(likes)+, "likes"
#print(frase_final)

#les variables es sobreescriuen
var3= 1
var4=2
resultat = var3 + var4

var5= 4
resultat = var3 + var4 + var5
print(resultat)

#llistes d'items
llista_noms = ["Pere", "Carme", "Joan"]
congnoms = ["Fernandez", "Padilla", "Huguet"]
print(llista_noms)

#també podem fer llistes de variables
nom_complert =[llista_noms, cognoms]
print(nom_complert)

#Imprimir noms per separat, el loop for / per cada cosa a la llista in noms
for nom in llista_noms:
    print("en", nom, "no ha vingut")

#altre sistema nomes amb python *3
for nom in llista_noms:
print(f"En {nom} no ha vingut")

#exercici llista
numeros = [1,2,3,4,10]
afegit = 2

for num in numeros:
    print(num + afegit)
