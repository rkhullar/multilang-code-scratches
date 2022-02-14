from pydantic import BaseModel
from decimal import Decimal


class Vendor(BaseModel):
    country: str
    commodity: str
    variable_overhead: Decimal
