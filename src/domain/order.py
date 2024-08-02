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

    def __init__(self, ref: str):
        self.reference = ref
        self.created = datetime.now()
        self.paid = 0
        self.taxes = 0
        self.discounts = 0
        self.items: dict[str, Item] = dict()
        self.rounds: list[OrderRound] = list()
        self.subtotal = 0

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
        """Update order's subtotal, taxes, discounts, and items."""
        for round_item in round.items:
            beer = stock.beers[round_item.beer]  # Get beer from stock.
            # Update item.
            item = self.items.get(beer.name)
            if not item:
                item = Item(
                    name=beer.name,
                    price_per_unit=beer.price,
                    total=round_item.quantity,
                )
            else:
                item.total += round_item.quantity
            self.items[beer.name] = item

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
        self.subtotal = sum(
            item.price_per_unit * item.total for item in self.items.values()
        )
        self.taxes = self.subtotal * self.IVA
