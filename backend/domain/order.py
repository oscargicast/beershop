from dataclasses import dataclass, field
from datetime import datetime

from domain.stock import Stock, Beer


class BeerNotFound(Exception):
    pass


@dataclass(frozen=True)
class RoundItem:
    beer: str
    quantity: int


@dataclass(frozen=True)
class Round:
    items: list[RoundItem] = field(default_factory=list)

    def __init__(self, *items: RoundItem):
        object.__setattr__(self, "items", list(items))

    def get_item(self, beer: str) -> RoundItem | None:
        for item in self.items:
            if item.beer == beer:
                return item
        raise ValueError(f"Beer {beer} not found in round.")


@dataclass(frozen=True)
class OrderRound(Round):
    created: datetime = datetime.now()


@dataclass
class Item:
    name: str
    price_per_unit: int
    total: int  # quantity.


class Order:
    IVA = 0.19

    created: datetime
    paid: bool
    taxes: float
    discounts: int
    subtotal: int
    items: list[Item]
    rounds: list[OrderRound]

    # List of all created order instances.
    _instances: list["Order"] = []

    def __init__(self, ref: str):
        self.reference = ref
        self.created = datetime.now()
        self.paid = False
        self.taxes = 0
        self.discounts = 0
        self.subtotal = 0
        self.items = list()
        self.rounds = list()
        # Add the instance to the list of instances.
        self.__class__._instances.append(self)

    def __repr__(self):
        return f"Order(reference={self.reference})"

    def __eq__(self, other):
        if not isinstance(other, Order):
            return False
        return other.reference == self.reference

    def __hash__(self):
        return hash(self.reference)

    def __gt__(self, other):
        if self.created is None:
            return False
        if other.created is None:
            return True
        return self.created > other.created

    @classmethod
    def get_instances(cls) -> list["Order"]:
        """Return all created instances."""
        return cls._instances

    @classmethod
    def clear_instances(cls) -> None:
        """Clear all created instances."""
        cls._instances.clear()

    def get_item(self, beer: str) -> Item | None:
        for item in self.items:
            if item.name == beer:
                return item
        return None

    def add_round(self, stock: Stock, round: Round):
        """
        Must check if the stock has enough beers to fulfill the round.
        Then, it must allocate the beers to the stock and update the round.
        Finally, it must update the order's subtotal, taxes, discounts, and items.
        """
        beers = []
        # Build the new stock to be allocated inside beers list.
        for round_item in round.items:
            beer = stock.beers[round_item.beer]  # Get beer from stock.
            quantity = beer.quantity - round_item.quantity
            beers.append(
                Beer(
                    name=beer.name,
                    price=beer.price,
                    quantity=quantity,
                )
            )
        stock.allocate(beers)
        self.__update_items(stock, round)
        self.__update_rounds(round)
        self.__update_subtotal()

    def __update_items(self, stock: Stock, round: Round):
        for round_item in round.items:
            beer = stock.beers[round_item.beer]  # Get beer from stock.
            # Buscar si el item ya existe en self.items
            item = next((i for i in self.items if i.name == beer.name), None)

            if item is None:
                # Si no existe, crear un nuevo item y añadirlo a la lista
                item = Item(
                    name=beer.name,
                    price_per_unit=beer.price,
                    total=round_item.quantity,
                )
                self.items.append(item)
            else:
                # Si ya existe, actualizar la cantidad total
                item.total += round_item.quantity

    def __update_rounds(self, round: Round):
        """Update the order's rounds."""
        self.rounds.append(
            OrderRound(
                created=datetime.now(),
                items=round.items,
            )
        )

    def __update_subtotal(self):
        """Update the order's subtotal, taxes, and discounts."""
        self.subtotal = sum(item.price_per_unit * item.total for item in self.items)
        self.taxes = self.subtotal * self.IVA
