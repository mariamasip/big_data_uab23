import pandas as pd

# 1 ¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

list=[]
df= pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep="\t", usecols=["captured_at", "viewer_count"])

for chunk in df:
  df2 = chunk.groupby("captured_at")["viewer_count"].sum().reset_index()
  list.append(df2)
  print(chunk)

  final_frame_1 = pd.concat(list)
final_frame_2 = final_frame_1.groupby("captured_at")["viewer_count"].sum()
final_frame_2.to_csv("1.csv")

# 2 ¿Cuales son las categorías más vistas y en las que más horas de directo se han realizado?

list_viewers=[] 
list_ocurrencies=[] 

df= pd.read_csv("feb_23_es_simple.csv", chunksize=1000000, sep="\t", usecols=["game_name", "viewer_count"]) 
for chunk in df: 

    dfviews = chunk.groupby("game_name")["viewer_count"].sum().reset_index() 
    dfocurrencies = chunk.groupby("game_name").size().reset_index(name='ocurrencies') 

    list_viewers.append(dfviews) #afegim a la llista el resultat de processar el chunk
    list_ocurrencies.append(dfocurrencies) 

final_frame_viewers = pd.concat(list_viewers) 
final_frame_ocurrencies = pd.concat(list_ocurrencies) 

df_viewers_2 = final_frame_viewers.groupby("game_name")["viewer_count"].sum().reset_index() 
df_ocurrencies_2 = final_frame_ocurrencies.groupby("game_name")["ocurrencies"].sum().reset_index() 

final_frame_2 = df_viewers_2.merge(df_ocurrencies_2) 
final_frame_2.to_csv("2.csv") 

# 3¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?

listcategories=[]
df= pd.read_csv("feb_23_es_simple.csv", chunksize=10000, sep="\t", usecols=["captured_at", "game_name", "viewer_count"])

for chunk in df:
    df_sum3 = chunk.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index()
    listcategories.append(df_sum3)
    print(chunk)

final_frame_1 = pd.concat(listcategories)
final_frame_2 = final_frame_1.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index()
final_frame_2.to_csv("3.csv")

