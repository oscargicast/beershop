import pytest

from domain.stock import Beer, Stock, OutOfStock
from domain.order import Round, RoundItem, Order


def make_stock() -> Stock:
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


def test_after_one_round():
    stock = make_stock()
    round_1 = Round(
        RoundItem("Corona", 2),
        RoundItem("Club Colombia", 1),
    )

    order = Order(ref="order_1")
    order.add_round(
        stock=stock,
        round=round_1,
    )
    # Check stock.
    assert stock.beers["Corona"].quantity == 0
    assert stock.beers["Club Colombia"].quantity == 2

    # Check subtotal and taxes.
    assert order.subtotal == 340
    assert order.taxes == 340 * Order.IVA

    # Check items.
    assert order.items["Corona"].price_per_unit == stock.beers["Corona"].price
    assert order.items["Corona"].total == round_1.get_item("Corona").quantity


def test_after_two_rounds():
    stock = make_stock()
    order = Order(ref="order_1")

    round_1 = Round(
        RoundItem("Corona", 1),
        RoundItem("Club Colombia", 1),
    )
    order.add_round(
        stock=stock,
        round=round_1,
    )
    # Check stock after first round.
    assert stock.beers["Corona"].quantity == 1
    assert stock.beers["Club Colombia"].quantity == 2
    # Check subtotal and taxes.
    assert order.subtotal == 225
    assert order.taxes == 225 * Order.IVA
    # Check order items.
    assert order.items["Corona"].price_per_unit == stock.beers["Corona"].price
    assert (
        order.items["Club Colombia"].price_per_unit
        == stock.beers["Club Colombia"].price
    )
    assert order.items["Corona"].total == 1
    assert order.items["Club Colombia"].total == 1

    round_2 = Round(
        RoundItem("Corona", 1),
        RoundItem("Club Colombia", 2),
    )
    order.add_round(
        stock=stock,
        round=round_2,
    )
    # Check stock after second round.
    assert stock.beers["Corona"].quantity == 0
    assert stock.beers["Club Colombia"].quantity == 0
    # Check subtotal and taxes.
    assert order.subtotal == 560
    assert order.taxes == 560 * Order.IVA
    # Check order items.
    assert order.items["Corona"].price_per_unit == stock.beers["Corona"].price
    assert (
        order.items["Club Colombia"].price_per_unit
        == stock.beers["Club Colombia"].price
    )
    assert order.items["Corona"].total == 2
    assert order.items["Club Colombia"].total == 3

    # Check round creation time.
    assert order.rounds[0].created < order.rounds[1].created


def test_order_out_of_stock():
    stock = make_stock()
    round_1 = Round(
        RoundItem("Corona", 2),
        RoundItem("Club Colombia", 4),
    )

    order = Order(ref="order_out_of_stock")
    with pytest.raises(OutOfStock, match="Quantity can not be negative"):
        order.add_round(
            stock=stock,
            round=round_1,
        )
    # Check stock.
    assert stock.beers["Corona"].quantity == 2
    assert stock.beers["Club Colombia"].quantity == 3

    # Check subtotal and taxes.
    assert order.subtotal == 0
    assert order.taxes == 0 * Order.IVA

    # Check items.
    assert order.items == dict()
    assert order.rounds == list()
