import pandas as pd
import json
import glob

# per obrir tots els arxius JSON dins del directori "api_responses/"
files = glob.glob('api_responses/*.json')

# Creem una llista buida per a emmagatzemar els marcs de dades
llista_dfs = []

# Recorrem cada arxiu JSON
for file in files:
    # Obrim l'arxiu JSON
    with open(file, encoding="utf-8") as jsonfiles:
        # Carrega les dades JSON
        dades = json.load(jsonfiles)

        # Obtenim els tuits de l'arxiu JSON
        tweets = dades["data"]
        print(len(tweets))

        # Recorrem cada tuit
        for tweet in tweets:
            # Obtenim les dades del tuit que ens interessen
            author_id = tweet["author_id"]
            text = tweet["text"]
            created_at = tweet["created_at"]
            possibly_sensitive = tweet["possibly_sensitive"]
            retweet_count = tweet["public_metrics"]["retweet_count"]
            reply_count = tweet["public_metrics"]["reply_count"]
            like_count = tweet["public_metrics"]["like_count"]
            quote_count = tweet["public_metrics"]["quote_count"]
            impression_count = tweet["public_metrics"]["impression_count"]
            lang = tweet["lang"]

            # Obté la llista d'usuaris de l'arxiu JSON
            users = dades["includes"]["users"]
            # Per a cada usuari de la llista d'usuaris
            for user in users:
                # Si la ID de l'usuari coincideix amb la ID de l'autor del tuit actual
                if user["id"] == author_id:
                    # Guarda el nom d'usuari de l'autor i el nombre de seguidors
                    user_name = user["username"]
                    print(user["id"], user["username"])
                    followers = user["public_metrics"]["followers_count"]
                # Si la ID de l'usuari no coincideix amb la ID de l'autor del tuit actual, passa a l'usuari següent
                else:
                    pass

            # Creem un nou dataframe de dades per al tuit
            df = pd.DataFrame({
                "user_id": author_id,
                "user_name": user_name,
                "followers": followers,
                "text": text,
                "lang": lang,
                "created_at": created_at,
                "impression_count": impression_count,
                "like_count": like_count,
                "retweet_count": retweet_count,
                "reply_count": reply_count,
                "quote_count": quote_count,
                "possibly_sensitive": possibly_sensitive,
            }, index=[0])

            print(df)
            # Afegim el marc de dades a la llista
            llista_dfs.append(df)

# Concatenem el dataframe amb les dades
df_final = pd.concat(llista_dfs)

# Guardem el dataframe final en un fitxer CSV que s'anomena final_tableau.csv
df_final.to_csv("final_tableau.csv")
