import pandas as pd

#1 ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

list=[] #Es crea una llista anomenada "list". S'utilitza per guardar cadascun dels dataframes que es generin en processar els chunks de l'arxiu CSV.
df= pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep="\t", usecols=["captured_at", "viewer_count"]) #Es llegeix l'arxiu, s'estableixen els chunks cada 10000, separador de columnes per un tabulador (\t) i les columnes que volem utilitzar

for chunk in df:
    df2 = chunk.groupby("captured_at")["viewer_count"].sum().reset_index() #Per a cada chunk, s'agrupa per la columna "captured_at" i es calcula la suma de la columna "viewer_count"
    list.append(df2)#Aquest dataframe s'afegeix a la llista "list" per conquetenar-lo
    print(chunk)#imprimeix els chuks al terminal

final_frame_1 = pd.concat(list) #Es concatenen tots els dataframes de la llista "list" en un únic dataframe
final_frame_2 = final_frame_1.groupby("captured_at")["viewer_count"].sum()#s'agrupa per la columna "captured_at" i es calcula la suma de la columna "viewer_count" per a cada valor únic de "captured_at"
final_frame_2.to_csv("1.csv") #es crea el csv final

#2 ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?

list_viewers=[] #Es defineixen dues llistes buides, una per agrupar el viewer_count
list_ocurrencies=[] #Llista per agrupar el nombre d'ocurrencies simultànies d'un mateix joc

df= pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["game_name", "viewer_count"]) #Es llegeix l'arxiu, s'estableixen els chunks cada 10000, separador de columnes per un tabulador (\t) i les columnes que volem utilitzar

for chunk in df:

    dfviews = chunk.groupby("game_name")["viewer_count"].sum().reset_index() #S'agrupen les instàncies de cada joc juntament amb la suma total dels viewers
    dfocurrencies = chunk.groupby("game_name").size().reset_index(name='ocurrencies') #s'agrupem les instàncies de cada joc amb el nombre total d'ocurrencies simultànies.
    print(chunk)#imprimim el chunk al terminal

    list_viewers.append(dfviews) #Es concatenen les llistes resultants per obtenir un dataframe únic per al viewer_count i un altre per al nombre d'ocurrencies simultànies
    list_ocurrencies.append(dfocurrencies) #afegim a la llista el resultat de processar el chunk

final_frame_viewers = pd.concat(list_viewers) #concatenem totes les llistes
final_frame_ocurrencies = pd.concat(list_ocurrencies) #concatenem totes les llistes

df_viewers_2 = final_frame_viewers.groupby("game_name")["viewer_count"].sum().reset_index() #Es netegen les dades del dataframe únic per al viewer_count i el dataframe únic per al nombre d'ocurrencies simultànies. Això implica eliminar les duplicats de categoria i sumar els resultats totals
df_ocurrencies_2 = final_frame_ocurrencies.groupby("game_name")["ocurrencies"].sum().reset_index()

final_frame_2 = df_viewers_2.merge(df_ocurrencies_2) #Es realitza un merge dels dos dataframes per obtenir-ne un de nou que contingui el nom del joc, el nombre de viewers, i el nombre d'ocurrències simultànies
final_frame_2.to_csv("2final.csv") #creem el csv


#3¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?

listcategories=[] #Creem una llista buida per emmagatzemar els resultats de cada iteració
df= pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep="\t", usecols=["captured_at", "game_name", "viewer_count"])##Es llegeix l'arxiu, s'estableixen els chunks cada 10000, separador de columnes per un tabulador (\t) i les columnes que volem utilitzar

for chunk in df:
    df_sum3 = chunk.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index() #Agrupem les files del chunk per "captured_at" i "game_name" i sumem els valors de la columna "viewer_count", generant així un dataframe amb les columnes "captured_at", "game_name" i "viewer_count"
    listcategories.append(df_sum3)#Afegim el dataframe a la llista "listcategories"
    print(chunk)

final_frame_1 = pd.concat(listcategories)#Concatenem tots els dataframes de la llista
final_frame_2 = final_frame_1.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index()
final_frame_2.to_csv("3.csv")#Generem un nou dataframe

#4.¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?

list_audiencia = [] #Creem dues llistes buides
list_hores = []

df = pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["streamer_name","game_name", "viewer_count"])


for chunk in df:
    df_audiencia = chunk.groupby('streamer_name')['viewer_count'].sum().reset_index()#es crea un dataframe que agrega els viewers per cada "streamer_name" i els suma
    df_hores = chunk.groupby('streamer_name').size().transform(lambda x: x*0.25).reset_index(name='hores')#es crea un dataframe que agrega les hores d'streaming i es multiplica per 0.25 per convertir les línies de dades en hores
    print(chunk)

    list_audiencia.append(df_audiencia)
    list_hores.append(df_hores)

df_audiencia_final = pd.concat(list_audiencia).groupby('streamer_name')['viewer_count'].sum().reset_index() #es crea un dataframe final
df_hores_final = pd.concat(list_hores).groupby('streamer_name')['hores'].sum().reset_index()
df_final = df_audiencia_final.merge(df_hores_final)#fusiona les dades dels dataframes "df_audiencia_final" i "df_hores_final"

df_final.to_csv('4.csv', decimal=",") #crea el csv i canvia la separació dels decimals per comes

#5.¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores? ¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?
df = pd.read_csv('feb_23_es_simple.csv',sep="\t")

df_sum = df.groupby(['captured_at'])['viewer_count'].std().reset_index() #s'agrupa la columna 'captured_at' del dataframe 'df' i s'aplica la funció 'std()'

df_sum.to_csv('5prova1.csv', decimal=',', index=False)#es crea el csv 
