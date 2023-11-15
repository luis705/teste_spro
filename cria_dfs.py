import json

import pandas as pd

from db import BancoDeDados


def cria_dataframes():
    data_1 = {
        'Carro': ['Onix', 'Polo', 'Sandero', 'Fiesta', 'City'],
        'Cor': ['Prata', 'Branco', 'Prata', 'Vermelho', 'Preto'],
        'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
    }

    data_2 = {
        'Montadora': ['Chevrolet', 'Volkswagen', 'Renault', 'Ford', 'Honda'],
        'País': ['EUA', 'Alemanha', 'França', 'EUA', 'Japão'],
    }

    df_1 = pd.DataFrame(data_1)
    df_2 = pd.DataFrame(data_2)

    return df_1, df_2


if __name__ == '__main__':
    df_1, df_2 = cria_dataframes()

    mongo = BancoDeDados()
    mongo.cria_banco('Teste')
    mongo.cria_colecao('Carros')
    mongo.cria_colecao('Montadoras')

    mongo.insere('Carros', json.loads(df_1.to_json(orient='records')))
    mongo.insere('Montadoras', json.loads(df_2.to_json(orient='records')))
    mongo.verifica_colecoes()

    print(list(mongo.realiza_aggregation()))
