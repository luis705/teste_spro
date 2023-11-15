import pymongo


class BancoDeDados:
    def __init__(self, ip: str = 'localhost', porta: str = 27017):
        self.cliente = pymongo.MongoClient(f'mongodb://{ip}:{porta}/')
        self.banco = None
        self.colecoes = dict()

    def cria_banco(self, banco):
        self.banco = self.cliente[banco]

    def cria_colecao(self, colecao):
        self.colecoes[colecao] = self.banco[colecao]

    def verifica_colecoes(self):
        print(self.banco.list_collection_names())

    def insere(self, colecao, dados):
        self.colecoes[colecao].insert_many(dados)

    def realiza_aggregation(self):
        return self.cliente['Teste']['Carros'].aggregate(
            [
                {
                    '$lookup': {
                        'from': 'Montadoras',
                        'localField': 'Montadora',
                        'foreignField': 'Montadora',
                        'as': 'Montadoras',
                    }
                },
                {'$addFields': {'Pais': {'$first': '$Montadoras.País'}}},
                {
                    '$group': {
                        '_id': '$Pais',
                        'Carros': {'$addToSet': '$Carro'},
                    }
                },
                {'$sort': {'_id': 1}},
            ]
        )
