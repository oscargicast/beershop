import pytest
import sys

from pathlib import Path

from domain.stock import Beer, Stock
from domain.order import Order, Round, RoundItem

# Add the src directory to the sys.path.
src_path = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture(scope="function")
def stock() -> Stock:
    stock = Stock()
    corona = Beer(
        name="Corona",
        price=115,
        quantity=2,
    )
    quilmes = Beer(
        name="Quilmes",
        price=120,
        quantity=0,
    )
    club_colombia = Beer(
        name="Club Colombia",
        price=110,
        quantity=3,
    )
    stock.allocate([corona, quilmes, club_colombia])
    return stock


@pytest.fixture(scope="function", autouse=True)
def clear_order_instances():
    Order.clear_instances()


@pytest.fixture(scope="function")
def order(stock):
    order = Order(ref="order-1")
    order.add_round(
        stock=stock,
        round=Round(
            RoundItem("Corona", 1),
            RoundItem("Club Colombia", 1),
        ),
    )
    order.add_round(
        stock=stock,
        round=Round(
            RoundItem("Club Colombia", 1),
        ),
    )
    order.add_round(
        stock=stock,
        round=Round(
            RoundItem("Corona", 1),
        ),
    )
    return order
