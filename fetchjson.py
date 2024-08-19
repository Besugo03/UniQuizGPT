import json
import requests

def main(test: str) -> int:
    """
    Funzione main del file che si occupa di prendere da github i file json delle domande e trasporle in oggetto
    Domanda
    """
    url = "https://raw.githubusercontent.com/dag7dev/UniQuizzes/7b91bb66e43857059fea30cbe32c0e87aeeceb6b/json/so2mz.json"

    #effettuo la richiesta sul sito web passando l'url
    r = requests.get(url, allow_redirects=False)

    #apro il file in modalità "write byte" e scrivo il contenuto basandomi su ciò che ho preso dall'url
    open("questions.json","wb").write(r.content)

    #apro il file e con le funzioni di libreria json mi salvo i dati 
    with open('questions.json', encoding="utf8") as f:
        json_data = json.load(f)

    #navigo le domande presenti nel file json
    for question in json_data:
        question["correct"] = ord(question["correct"])-97
        

    return 0

main("a")

class Domanda:
    def __init__(self, n_risposte):
        self.n_risposte=n_risposte;