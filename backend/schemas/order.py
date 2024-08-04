from datetime import datetime
from pydantic import BaseModel, PlainSerializer
from typing import List
from typing_extensions import Annotated

from domain.order import Order, Item, OrderRound, RoundItem


CustomDateTime = Annotated[
    datetime,
    PlainSerializer(
        lambda _datetime: _datetime.strftime("%Y-%m-%d %H:%M:%S"),
        return_type=str,
    ),
]


class OrderItemSchema(BaseModel):
    name: str
    price_per_unit: int
    total: int

    @classmethod
    def from_order_item(cls, item: Item) -> "OrderItemSchema":
        return cls(
            name=item.name,
            price_per_unit=item.price_per_unit,
            total=item.total,
        )


class RoundItemSchema(BaseModel):
    beer: str
    quantity: int

    @classmethod
    def from_round_item(cls, item: RoundItem) -> "RoundItemSchema":
        return cls(beer=item.beer, quantity=item.quantity)


class OrderRoundSchema(BaseModel):
    created: CustomDateTime
    items: List[RoundItemSchema]

    @classmethod
    def from_order_round(cls, order_round: OrderRound) -> "OrderRoundSchema":
        return cls(
            created=order_round.created,
            items=[RoundItemSchema.from_round_item(item) for item in order_round.items],
        )


class OrderSchema(BaseModel):
    reference: str
    created: CustomDateTime
    paid: bool
    taxes: float
    discounts: int
    subtotal: int
    items: List[OrderItemSchema]
    rounds: List[OrderRoundSchema]

    @classmethod
    def from_order(cls, order: Order) -> "OrderSchema":
        return cls(
            reference=order.reference,
            created=order.created,
            paid=order.paid,
            taxes=order.taxes,
            discounts=order.discounts,
            subtotal=order.subtotal,
            items=[OrderItemSchema.from_order_item(item) for item in order.items],
            rounds=[
                OrderRoundSchema.from_order_round(order_round)
                for order_round in order.rounds
            ],
        )
