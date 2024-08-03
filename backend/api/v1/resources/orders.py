from fastapi import APIRouter, HTTPException

from schemas.order import OrderSchema
from services.order import OrderService

from typing import Any


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.get("/{order_ref}", response_model=OrderSchema)
def read_item(order_ref: str) -> Any:
    order = OrderService.get_order_by_reference(order_ref)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderSchema.from_order(order)
