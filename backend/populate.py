from domain.stock import Beer, Stock
from domain.order import Order, Round, RoundItem


def make_stock() -> Stock:
    stock = Stock()
    corona = Beer(
        name="Corona",
        price=115,
        quantity=5,
    )
    quilmes = Beer(
        name="Quilmes",
        price=120,
        quantity=10,
    )
    club_colombia = Beer(
        name="Club Colombia",
        price=110,
        quantity=3,
    )
    stock.allocate([corona, quilmes, club_colombia])
    return stock


def make_orders():
    stock = make_stock()
    # order-1
    order_1 = Order(ref="order-1")
    order_1.add_round(
        stock=stock,
        round=Round(
            RoundItem("Corona", 2),
            RoundItem("Club Colombia", 1),
        ),
    )
    order_1.add_round(
        stock=stock,
        round=Round(
            RoundItem("Club Colombia", 1),
            RoundItem("Quilmes", 2),
        ),
    )
    order_1.add_round(
        stock=stock,
        round=Round(
            RoundItem("Quilmes", 4),
        ),
    )
    # order-2
    order_2 = Order(ref="order-2")
    order_2.paid = True
    order_2.add_round(
        stock=stock,
        round=Round(
            RoundItem("Corona", 2),
        ),
    )
    order_2.add_round(
        stock=stock,
        round=Round(
            RoundItem("Club Colombia", 1),
        ),
    )
