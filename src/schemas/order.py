from datetime import datetime
from pydantic import BaseModel, PlainSerializer
from typing_extensions import Annotated

from domain.order import Order


CustomDateTime = Annotated[
    datetime,
    PlainSerializer(
        lambda _datetime: _datetime.strftime("%Y-%m-%d %H:%M:%S"),
        return_type=str,
    ),
]


class RoundItemSchema(BaseModel):
    beer: str
    quantity: int


class RoundSchema(BaseModel):
    items: list[RoundItemSchema]


class OrderRoundSchema(RoundSchema):
    created: CustomDateTime


class OrderSchema(BaseModel, Order):
    created: CustomDateTime
    rounds: list[OrderRoundSchema]
