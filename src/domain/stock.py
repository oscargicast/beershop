from dataclasses import dataclass
from datetime import datetime


class OutOfStock(Exception):
    pass


@dataclass
class Beer:
    name: str
    price: int
    quantity: int


class Stock:
    beers: dict[str, Beer]

    def __init__(self):
        self.beers = dict()
        self.last_update = datetime.now()

    def allocate(self, beers: list[Beer] | Beer):
        if isinstance(beers, Beer):
            beers = [beers]
        # Validate Beer objects before allocating them.
        if any(self.can_allocate(beer) for beer in beers):
            raise OutOfStock(f"Quantity can not be negative.")
        for beer in beers:
            self.beers[beer.name] = beer
        # Update last_update.
        self.last_update = datetime.now()

    def can_allocate(self, beer: Beer) -> bool:
        return beer.quantity < 0
