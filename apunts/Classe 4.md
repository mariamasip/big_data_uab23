## Classe 3: API Twitch

### API
Direcció API twitch -  'https://pytwitchapi.readthedocs.io/en/v2.5.7/modules/twitchAPI.twitch.html'
```Python
pip install twitchAPI==2.5.7.1
```
Per **impirmir dades** d'un perfil (el meu en aquest cas)
```Python
from twitchAPI.twitch import Twitch
from pprint import pprint

twitch = Twitch('-', '-')
pprint(twitch.get_users(logins=['mariamasip5']))
```
### Funció 'get_streams'
```Python
from twitchAPI.twitch import Twitch
from pprint import pprint

twitch = Twitch('5o4e1o1ofoml8nxmq023liwk4vy870', 'ikwo5xvth1y3pyu7t9e5r0z8lvs0xi')

streams = twitch.get_streams(first=20, language="es") #funcio per agafar streams
print(streams)
```

### Exportar Json
Per exportar en un document Json:
```Python
streams = twitch.get_streams(first=20, language="es") #funcio per agafar streams
print(streams)

with open("output_file.json", 'w', encoding='utf-8') as f:
    json.dump(streams, f, ensure_ascii=False, indent=4)
```  
    
### Selecionar les dades 
Selecionar les dades del Json que volem i les ordenem:
```Python
dades = streams["data"]

for dada in dades:
    Captured at=
    User_id = dada["user_id"]
    User_name = dada["user_name"]
    Game_id = dada["game_id"]
    Game_name = dada["game_name"]
    Title = dada["title"]
    viewers_count = dada["viewer_count"]
    Started At = dada["started_at"]
    is_mature = dada["is_mature"]
```
### Importar pandas
```Python
import pandas aspd #a dalt del docu
```

###Fixer sencer exemple
El fixer sencer per tal de seleccionar aquelles caselles que trobem interessants i després guardar-les en un csv.
```Python
from twitchAPI.twitch import Twitch
from pprint import pprint
import json
import pandas as pd
import datetime
twitch = Twitch('5o4e1o1ofoml8nxmq023liwk4vy870', 'ikwo5xvth1y3pyu7t9e5r0z8lvs0xi')

streams = twitch.get_streams(first=20, language="es") #funcio per agafar streams


now = datetime.datetime.now()
dades = streams["data"]

llista_dataframes = []
for dada in dades:
    captured_at = now
    user_id = dada["user_id"]
    user_name = dada["user_name"]
    game_id = dada["game_id"]
    game_name = dada["game_name"]
    title = dada["title"]
    viewer_count = dada["viewer_count"]
    started_at = dada["started_at"]
    is_mature = dada["is_mature"]

    df = pd.DataFrame({
        "captured_at": captured_at,
        "user_id": user_id,
        "user_name": user_name,
        "game_id": game_id,
        "title": title,
        "viewer_count": viewer_count,
        "is_mature":is_mature,

    }, index=[0])
    llista_dataframes.append(df)

final_dataframe = pd.concat(llista_dataframes)
final_dataframe.to_csv("prova2.csv", index=False)
```
Final del fixer

## Funcions
```Python
def loquesea():
    print("hola")

loquesea()
```

Amb una variable fora de la funció
```Python
variable="hola"
def loquesea():
    print(variable)

loquesea()
```
```Python
variable="hola"
variable_2 = "adeu"
def loquesea(pip, car): #agafa les variables per ordre de recepció, no importa en nom en la invocació
    print(pip, car)

loquesea(variable)
```

El document final amb el Try i l'except. Amb el cursor que fa el canvi de pàgina
```Python
from pprint import pprint
import json
from twitchAPI.twitch import Twitch
import pandas as pd
import datetime
import time
twitch = Twitch('5o4e1o1ofoml8nxmq023liwk4vy870', 'ikwo5xvth1y3pyu7t9e5r0z8lvs0xi')
now = datetime.datetime.now()
llista_dataframes = []
cursor_dummy = None #per indicar que és la primera pag

#el cursor es com un marcapàgines
def crida(cursor): #reb la variable

    streams = twitch.get_streams(first=20, language="ca", after=cursor) #funcio per agafar streams seleccionem quantes en volem i l'idioma
    dades = streams["data"]

    for dada in dades:
        captured_at = now
        user_id = dada["user_id"]
        user_name = dada["user_name"]
        game_id = dada["game_id"]
        game_name = dada["game_name"]
        title = dada["title"]
        viewer_count = dada["viewer_count"]
        started_at = dada["started_at"]
        is_mature = dada["is_mature"]

        df = pd.DataFrame({
            "captured_at": captured_at,
            "user_id": user_id,
            "user_name": user_name,
            "game_id": game_id,
            "title": title,
            "viewer_count": viewer_count,
            "is_mature":is_mature,

        }, index=[0])
        llista_dataframes.append(df)

    try:
        cursor = streams["pagination"]["cursor"]#el cursor canvia de pàgina
        print(f"Fent una nova consulta. Total de streams {len(llista_dataframes)}")
        time.sleep(1)
        crida(cursor)

    except KeyError:
        print("ultima pàgina")
        print(f"Total de streams capturats {len(llista_dataframes)}")
        pass


crida(cursor_dummy)#variables dummy(buscar)

final_dataframe = pd.concat(llista_dataframes)
final_dataframe.to_csv("cat.csv", index=False)
print(final_dataframe)
```



