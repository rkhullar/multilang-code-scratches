from fastapi import FastAPI
import uvicorn
from dataclasses import dataclass
from decimal import Decimal

app = FastAPI()


@dataclass
class Vendor:
    country: str
    commodity: str
    variable_overhead: Decimal

    def calculate_purchase_cost(self, unit_price: int, volume: int) -> Decimal:
        return (unit_price + self.variable_overhead) * volume


vendor_database = [
   Vendor(country='MX', commodity='mango', variable_overhead=Decimal('1.24')),
   Vendor(country='BZ', commodity='mango', variable_overhead=Decimal('1.42')),
]


@app.get('/hello')
def hello():
    unit_price, volume = 53, 405
    return dict(example=[
        {'country': 'MX', 'price': vendor_database[0].calculate_purchase_cost(unit_price, volume)},
        {'country': 'BZ', 'price': vendor_database[1].calculate_purchase_cost(unit_price, volume)}
    ])


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
