from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass
class Vendor:
    country: str
    commodity: str
    variable_overhead: Decimal

    def dict(self):
        return asdict(self)

    def calculate_purchase_cost(self, unit_price: int, volume: int) -> Decimal:
        return (unit_price + self.variable_overhead) * volume
