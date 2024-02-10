from typing import Dict, Union

GenericSchema = Dict[str, Union[str, float, int]]


TransactionSchema: GenericSchema = {
    'ean': int,
    'preco': float,
    'id_loja': int,
    'data_time': str,
}
