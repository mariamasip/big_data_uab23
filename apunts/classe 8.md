# pip install transformers
# pip install torch
# Raw Data --> TOKENIZERS --> Models --> Outputs

from transformers import pipeline
#et diu si el missatge és negatiu o positiu
pipe = pipeline("text-classification")
result = pipe("Maria wants to kill Àlex")
print(result)

# pip install sentencepiece
#tradueix al català
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ca") #a vegades fa falta el tokenizer
result = pipe("Maria wants to kill Àlex")
print(result)

Arxiu 2
# DEPENDENCIAS
# pip install tqdm
# pip install pandas
# pip install transformers
# pip install torch
#####

# EJEMPLOS DE MODELOS
# https://huggingface.co/MMG/xlm-roberta-base-sa-spanish
# https://huggingface.co/jorgeortizfuentes/spanish_hate_speech
# https://huggingface.co/francisco-perez-sorrosal/distilbert-base-uncased-finetuned-with-spanish-tweets-clf
#####


import glob
from tqdm import tqdm
import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline


models = ["MMG/xlm-roberta-base-sa-spanish", "jorgeortizfuentes/spanish_hate_speech", "francisco-perez-sorrosal/distilbert-base-uncased-finetuned-with-spanish-tweets-clf"]

dataset = "dataset-inmigrantes-barcelona.csv"

def proc(dataset):
    for model in models:
        model_name = model.split("/")[1]
        print(model_name)
        dataset_new_name = f"procesado-{model_name}.csv"
        tup_list = []
        df = pd.read_csv(dataset, nrows=100, usecols=["tweet_id","text"])
        tweets = df["text"].to_list()
        tweet_id = df["tweet_id"].to_list()

        t = AutoTokenizer.from_pretrained(model)
        m = AutoModelForSequenceClassification.from_pretrained(model)

        for tweet, tid in tqdm(zip(tweets, tweet_id)):
            pipe = pipeline("text-classification", model=m, tokenizer=t)
            result = pipe(tweet)
            content = result[0]
            label = content["label"]
            score = content["score"]
            tupla = (str(tid), tweet, label, score)
            tup_list.append(tupla)

        data = pd.DataFrame.from_records(tup_list, columns=[f"tweet_id", "text", f"label-{model}", f"score-{model}"])

        data.to_csv(dataset_new_name, index=False)

proc(dataset)

# Aqui hacemos un merge de todos los datasets para tener un archivo final con todo

lists_of_sets = []
datasets = glob.glob("procesado-*.csv")

dataset_madre = pd.read_csv(datasets[0])

for d in datasets[1:]:
    df = pd.read_csv(d)
    dataset_madre = dataset_madre.merge(df, on=["tweet_id", "text"])
    print(dataset_madre)

dataset_madre.to_csv(f"final-{dataset}")
