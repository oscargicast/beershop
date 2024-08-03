from fastapi import HTTPException

from domain.order import Order


class OrderService:
    @staticmethod
    def get_order_by_reference(order_ref: str) -> Order | None:
        orders = Order.get_instances()
        for order in orders:
            if order.reference == order_ref:
                return order
        return None
