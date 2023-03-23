## Classe 3: Pandas

### 1-Pandas
És una **llibreria a Python** que s'especialitza en el maneig, anàlisi i processament de dades. 

Com importar la llibreria:
```Python
'import pandas as pd'
```

### 2-Tupla
Col·leccions de dades idèntiques o diferents classificades amb un índex i que no poden ser modificades.
```Python
Tupla = (1,2,3,4,5)
llista = [1,2,3,4,5]
```

### 3-Diccionari
És una estructura de dades que permet emmagatzemar qualsevol mena d'informació, des de cadenes de text o caràcters fins a números enters, amb decimals, llistes i fins i tot altres diccionaris.
```Python
'diccionari = {"clau": "valor"}'
```

##Exercicis
### Exercici 1:
Exercici amb 'diccionari', 'tuplas' i 'llista':
```Python
diccionari = {"clau": "valor"}
tupla = ("elquesigui","elquesigui")
llista_1 = [6,9] llista_2 = ["josep", "maria"]
llista_final =[]

for nota, nom in zip(llista_1, llista_2): 
  print(nota, nom) conjunt = (nota, nom) print(conjunt) llista_final.append(conjunt)

for t in llista_final:
  nota = t[0] connjunt = t[] 
```

### Exercici 2:
**Tasca 1:** unificar els noms en una unica cadena de text llista_final =[]
```Python
notes = [1,6,8,9,10,6,5] 
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"] cognoms = ["Tort","Soldevila","Luna","Muñoz","Fernandez","Hernandez", "Llopart"]

for alumne, cognom in zip(alumnes, cognoms):
   conjunt = f"{alumne} {cognom}" print(conjunt) llista_final.append(conjunt)
print(llista_final)
```

**Tasca 2:** Ajuntar els noms + la nota final
```Python
dades_finals = [] 

for alumne, nota in zip(llista_final, notes):
  conjunt = (alumne, nota)
    dades_finals.append(conjunt)
print(dades_finals)
```
Una segona manera de fer-ho:
```Python
llista_final =[]

for alumne, cognom, nota in zip(alumnes, cognoms, notes): 
  conjunt = f"{alumne} {cognom}" tupla = (conjunt, nota) llista_final.append(tupla) 
print(llista_final)
```

**Tasca 3:** sumar un punt a totes les notes sense superar el 
```Python 
for persona in llista_final: 
  nova_nota = persona [1]+1
  if nova_nota > 10:
    nova_nota = 10 nova_persona = (persona[0], nova_nota) 
print(nova_persona) 
```

**Tasca 4:** Afegir un tercer element dins la tupla:

Si la nota final es inferior a 5, añadir el texto "suspendido".
Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".
Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".
Si la nota es igual o superior a 7, añadir el texto "notable".
Si la nota supera el 9, añadir el texto "Excelente".
Si la nota equivale a un 10, añadir el texto "matrícula de honor".

```Python
llista_definitiva =[] 

for persona in llista_final:
  nova_nota = persona [1]+1 
    if nova_nota > 10: 
      nova_nota = 10 
    if nova_nota < 5:
      qualificacio = "suspendido" 
    elif nova_nota>= 5 and nova_nota<= 6:
      qualificacio = "aprovado" 
    elif nova_nota>6 and nova_nota<7:
      qualificacio ="bien" 
    elif nova_nota>= 7:
      qualificacio = "notable" 
    elif nova_nota>=9: 
      qualificacio="excelent" 
   elif nova_nota == 10: 
    qualificacio = "matricula d'honor"

nova_persona = (persona[0], nova_nota, qualificacio) llista_definitiva.append(nova_persona)

print(llista_definitiva)

df = pd.DataFrame(llista_definitiva)

df.to_csv(dataset.csv)
```
El que fem amb df, és convertir el resultat que imprimeix per pantalla en un csv.

**Tasca 5:** Transforma la llista de tuplas en un dataset
```Python
import json
import pandas as pd

Opening JSON file
f = open('medidas.json') #carregar l'arxiu data = json.load(f) #transformar a diccionri

for d in data:#iterem sobre les dades 
  print(d["temperatura"]) #imprimim el continggut de la key temperatura print(f'{d["fecha"]} {d["temperatura"]}')
print(len(data)) #imprimir la quantitat de dades que hi ha al arxiu

llista_dades = []

for d in data: 
  temp = d["temperatura"] 
  pres = d["presion"] 
  date = d["fecha"] 
  tupla = (temp, pres, date) 
  llista_dades.append(tupla) df = pd.DataFrame(llista_dades) 
  
  print(df)

df.to_csv("temperatures.csv", index=False, decimal=",")
```

Calcular la temperatura màxima
```Python
df = pd.DataFrame(llista_dades, columns=["temp", "pres", "data"]) print(df) max = df["temp"].idxmax() print(df.iloc[[max]])
```
