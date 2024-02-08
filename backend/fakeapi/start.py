import random

import pandas as pd
from faker import Faker
from fastapi import FastAPI

app = FastAPI()
fake = Faker()

produtos = pd.read_csv('backend/fakeapi/produtos.csv', decimal=',')
produtos['index'] = range(1, len(produtos) + 1)
produtos.set_index('index', inplace=True)


@app.get('/gerarcompras')
async def gerarcompra():

    index = random.randint(1, len(produtos) - 1)
    tuple = produtos.iloc[index]

    return {
        'cliente': fake.name(),
        'provedor_cartao': fake.credit_card_provider(),
        'ean': int(tuple['EAN']),
        'nome_produto': tuple['Produto'],
        'preco': round(float(tuple['Preço']), 2),
        'id_loja': random.randint(1, 50),
        'data_time': fake.iso8601(),
        'posicao_cliente': fake.location_on_land(),
    }


@app.get('/gerarcompras/{numero_registros}')
async def gerarcompras(numero_registros: int):

    if numero_registros < 1:
        return {'error': 'O número deve ser maior que 1'}

    registros = []

    for _ in range(numero_registros):
        index = random.randint(1, len(produtos) - 1)
        tuple = produtos.iloc[index]

        transacao = {
            'cliente': fake.name(),
            'provedor_cartao': fake.credit_card_provider(),
            'ean': int(tuple['EAN']),
            'nome_produto': tuple['Produto'],
            'preco': round(float(tuple['Preço']), 2),
            'id_loja': random.randint(1, 50),
            'data_time': fake.iso8601(),
            'posicao_cliente': fake.location_on_land(),
        }
        registros.append(transacao)

    return registros
