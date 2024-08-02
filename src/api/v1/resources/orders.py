from fastapi import APIRouter, HTTPException

from schemas.order import OrderSchema
from services.order import OrderService


router = APIRouter(
    prefix="/orders",
    tags=["orders"],
)


@router.get("/{order_ref}")
def read_item(order_ref: str) -> OrderSchema:
    order = OrderService.get_order_by_reference(order_ref)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
