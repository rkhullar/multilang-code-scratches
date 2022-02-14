from decimal import Decimal

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from model import Vendor as VendorInDB
from schema import Vendor

app = FastAPI()


vendor_database = [
   VendorInDB(country='MX', commodity='mango', variable_overhead=Decimal('1.24')),
   VendorInDB(country='BZ', commodity='mango', variable_overhead=Decimal('1.42')),
]


@app.get('/vendors')
async def list_vendors() -> list[Vendor]:
    def iter_vendors():
        for item in vendor_database:
            yield jsonable_encoder(Vendor(**item.dict()))
    return list(iter_vendors())


@app.get('/hello')
async def hello():
    unit_price, volume = 53, 405
    return dict(example=[
        {'country': 'MX', 'price': vendor_database[0].calculate_purchase_cost(unit_price, volume)},
        {'country': 'BZ', 'price': vendor_database[1].calculate_purchase_cost(unit_price, volume)}
    ])


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
