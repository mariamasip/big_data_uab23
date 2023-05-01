import pandas com pd
import glob
import json

files = glob.glob('api_responses/*.json') #Obrim la llista d'arxius JSON al directori "api_responses/"


users_mentions = {} #Creem un diccionari buit per emmagatzemar les mencions d'usuaris

# Iterem sobre cada arxiu JSON a la llista d'arxius
for file in files:

    #Obrim l'arxiu JSON i carreguem les dades en una variable
    with open(file, encoding="utf-8") as jsonfiles:
        dades = json.load(jsonfiles)
        
        tweets = dades["data"]
        users_data = dades["includes"]["users"]
        print(len(tweets))

        # Iterem sobre cada tuit a la llista de tuits
        for tweet in tweets:
        
            author_id = tweet["author_id"]
            for user in users_data:  # Iterem sobre cada usuari a la llista d'usuaris
                if user["id"] == author_id: # Si la ID de l'autor del tuit coincideix amb la ID de l'usuari
                    user_name = user["username"]
                    if user_name not in users_mentions: #Si el nom d'usuari no està en el diccionari users_mentions, afegir-lo
                        users_mentions[user_name] = []

                    if "entities" in tweet and "mentions" in tweet["entities"]: # Si el tuit inclou mencions a altres usuaris
                        for mention in tweet["entities"]["mentions"]:
                            mention_name = mention["username"] # Obtindrem el nom d'usuari mencionat en el tuit
                            if mention_name not in users_mentions[user_name]: # Si el nom d'usuari mencionat no està a la llista de mencions de l'usuari actual, afegir-lo
                                users_mentions[user_name].append(mention_name)


    data = {"target": [], "source": []}     #Crear un DataFrame amb les dades de les mencions
    for user, mentions in users_mentions.items():
        for mention in mentions:
            data["target"].append(user)
            data["source"].append(mention)
    df = pd.DataFrame(data)

    df.to_csv("final_gephi.csv", index=False) 
    # Guardar el DataFrame en un arxiu CSV
