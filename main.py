from backend.contracts.schemas import TransactionSchema
from backend.datasource.api import APICollector

schema = TransactionSchema

Collector = APICollector(schema).start(500)

print(Collector)