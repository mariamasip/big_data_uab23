#pip install beautifulsoup4
#pip insgtall requests
#pip install spotipy
#pip install lxml
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup

anys = range(2000, 2023, 1)

llista_dataframes = []

for any in anys:
    try:
        resposta = requests.get(f"https://es.wikipedia.org/wiki/Festival_de_la_Canci%C3%B3n_de_Eurovisi%C3%B3n_{any}") #un paquet
        soup = BeautifulSoup(resposta.text, 'html.parser')
        final = soup.find('span', id = "Final")
        tabla = final.find_next("table")
        df = pd.read_html(tabla.prettify())[0]
        df["any"] = any
        print(df)
        df.columns.values[0] = "N."
        df.columns.values[5] = "Puntos"
        df.columns.values[2] = "Cantante"

        llista_dataframes.append(df)
    except AttributeError:
       # print(f"error: {any}")


final = pd.concat(llista_dataframes)
#final.to_excel("llista_final.xlsx", index=False)
"""
df = pd.read_excel("llista_final.xlsx")

SPOTIPY_CLIENT_ID = "437c8ad79c904d3ba854ad5f29fc285f"
SPOTIPY_CLIENT_SECRET = "f31a5599a04345a4914ffbd3147234c6"

auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
ap = spotipy.Spotify(auth_manager = auth_manager)

for index, row in df.iterrows():
    artista = row["Intérprete(s)"]
    track = row["Canción"].split("«")[1].split("«")[0]
    try:
       p_track = track.split("«")[1].split("«")[0]
    except IndexError
        p_track=track
    print(artista, p_track)
    q = f"{artista}{p_track}"
    info = sp.search(q, limit =10, offset=0, type='track', market=None)
    print(info)
