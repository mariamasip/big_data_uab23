## classe 2

### llista.append
**Afegir noms a una llista** Amb 'llista.append' podem sumar elements d'una llista en una altra.
'''
llista = ["jaume", "carme"]
llista2= ["raquel", "maria"]

llista.append(llista2)
print(llista)
'''


Imprimir una llista amb els nom separats, a través del bucle 'for'.
'''
llista_noms= ["carme", "Joan"]

for nom in llista_noms:
    print(nom)
'''


Imprimir un dels noms de la llista, utilitzen '==' que significa que si el nom és igual a 'Joan', imprimeixi el nom en pantalla.
'''
for nom in llista_noms:
    if nom == "joan":
        print(nom)
'''


**Else** va després de 'if' en cas que no compleixi la condició de l'if' aquesta saltarà a 'else'. 
'''
llista_noms =["carme", "Joan"]

for nom in llista_noms:
    if nom == "joan":
        print(nom)
    else:
        print(nom + "no es en joan")
 '''
 Com que el nom no és igual '==' a Joan, imprimeix per pantalla: X no es Joan.
 
        
 **Elif** Són condicionals else encadenats.
 '''  
numeros =[1,2,3,6,7,8,10,15]

for n in numeros:
    if n < 6:
        print(f"{n} es menor que 6")
    elif n == 6:
        print(f"{n}es igual que 6")
    else:
        print(f"{n} es major que 6")
'''
Si el número de la llista és més petit '<' que 6, s'imprimirà: X es menor que 6. Si és igual '==' que 6, s'imprimirà: X és igual que 6. Si és major '>' que 6, s'imprimirà: X és major que 6.


**len** retorna la longitud d'un objecte, ja sigui una llista, cadena, tupla o diccionari.
'''
numeros =[1,2,3,6,7,8,10,15]
print(len(numeros)

numeros =[1,2,3,6,7,8,10,15]

print(len(numeros)
llargaria = len(numeros)
print(llargaria)
'''


######Exercicis bàsics

**Exercici A**
'''
frase = "esto es un ejercicio"
print(frase)

nota = 9
classe = "Analítica Digital"
frase2=(f"en la assignatura {classe} he obtingut un {nota}")
nota = 10
frase2=(f"en la assignatura {classe} he obtingut un {nota}")
print (frase2)
'''


**Exercici B**
'''
notas = ["5","7","6","4"]
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]
nota_numerica = int(nota)
print (nota_numerica + 1)

for nota in notas:
    print (nota_numerica+1)
'''
    
part 2 de l'exercici:
'''  
for nota in notas:
print (nota_numerica+1)

for nota, nom in zip(notas, alumnos):
    nota_numerica =int(nota)
    nota_final = nota_numerica+1
    print(nota_final, nom)
'''
En aquesta segona part, s'imprimeix el noms + la nota


esta el nom a la llista?    
'''
lista = ["adria", "carla", "joan", "pere"]

nom = "joan"

#saber si el nom esta a la llista
if nom in lista:
    print ("Sí")
else:
    print("no")
'''

    
**index** aquesta funció ens permet obtenir l'índex o la posició de la primera aparició d'un element dins d'una llista.
'''
lista = ["adria", "carla", "joan", "pere"]

nom = "joan"

if nom in lista:
    print ("Sí")
    #saber la posició del nom dins la llista
    position = lista.index(nom)
    print(position)
else:
    print("no")
'''
És el mateix que en l'exercici anterior però utilitzant la funció index de manera més eficient.

**set**és una col·lecció d'elements desordenats que no admet duplicats.
'''
lista = ["adria", "carla", "joan", "pere", "pere"]

valors_unics = set(lista)

print(valors_unics)
print(len(valors_unics))
'''
Per saber quans alumnes, sense contar els duplicats, dins una llista.

Exercici 1
a)
'''
llista = [ "david", "dani", "marta", "jaume", "adria", "carla", "joan", "pere", "carla", "pere", "adria", "quico", "pere", "joan", "agustí", "adria", "joan", "adria", "siscu", "carles", "dani", "carla"]
llista_unics = set(llista)
print(f"Han vingut {len(llista_unics)} alumnes")
'''

Exercici 2
b)
'''
llista = [ "david", "dani", "marta", "jaume", "adria", "carla", "joan", "pere", "carla", "pere", "adria", "quico", "pere", "joan", "agustí", "adria", "joan", "adria", "siscu", "carles", "dani", "carla"]

llista_unics = set(llista)
print(f"Han vingut {len(llista_unics)} alumnes")

for nom in llista_unics:
    valor = llista.count (nom)
    if valor > 1:
        print(nom, valor)

llista_repetits=[]
for nom in llista_unics:
    valor = llista.count (nom)
    if valor > 1:
        llista_repetits.append(nom)
    print(f"Han repetit {len(llista_repetits)} alumnes")

'''

Utilitzant el contador
'''
llista_repetits=[]
contador = 0
for nom in llista_unics:
    valor = llista.count(nom)
    if valor > 1:
        llista_repetits.append(nom)
        contador = contador + 1

print(f"Han repetit {len(llista_repetits)} alumnes")
print(contador)
'''

Exercici 2 
c)
'''
percentatge = (contador/len(llista_unics)) * 100
print (f"El percentatge d'assistència és del {percentatge} %")
'''
L'equació de % =  x/y * 100

Exercici 3
a)
'''
notes = ["5","3","7","8","9.5","4","6,2"]
alumnes = ["adria","agnès","josep","rafa","cristina","Gemma","Eduard"]
'''

Part a) imprimir les ntes per cada alumne
'''
for nota, alumne in zip(notes, alumnes):
    print(nota, alumne)
'''

Part b) Calcular la nota promig
'''
notes_arreglades = []
for nota, alumne in zip(notes, alumnes):
    print(nota_final, nom)

    nota_arreglada = int(nota)
    print(nota_arreglada)

    if "." in nota:
        nota_arreglada = float(nota)
        notes_arreglades.append(nota_arreglada)
    elif "," in nota:
        nota_arreglada = float(nota.replace(",", "."))
        notes_arreglades.append(nota_arreglada)
    else:
        nota_arreglada = int(nota)
        notes_arreglades.append(nota_arreglada)

    print(notes_arreglades)
    print(round(sum(notes_arreglades)/len(notes_arreglades))
'''
          
Calcula i imprimeix la nota més alta amb l'alumne
'''
nota_maxima = max(notes_arreglades)
posicio = notes_arreglades.index(nota_maxima)
print(nota_maxima, posicio)
print(f"La màxima és un {nota_maxima}, i l'ha obtingut {alumnes[posicio]}")
'''

Imprineix la nota mínima
'''
nota_minima = min(notes_arreglades)
posicio = notes_arreglades.index(nota_minima)
print(nota_minima, posicio)
print(f"La màxima és un {nota_minima}, i l'ha obtingut {alumnes[posicio]}")
'''

    


