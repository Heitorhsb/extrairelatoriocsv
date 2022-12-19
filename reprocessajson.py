#!/usr/bin/env python

import json


arquivo = open("nomes.csv" , "w+")

with open("collection.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

for i in dados:


    print(i['userName'],";", i['end'],";", i['content'],";", file = arquivo) 

    ##CORRIGE UM ERRO DE UMA VIRGULA NO FINAL DO JSON QUE INVALIDA O ARQUIVO


