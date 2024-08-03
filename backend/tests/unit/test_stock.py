import pytest

from domain.stock import Beer, Stock, OutOfStock


def test_add_beers():
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
    stock.allocate(corona)
    assert stock.beers["Corona"] == corona
    first_last_update = stock.last_update

    stock.allocate(quilmes)
    assert stock.beers["Quilmes"] == quilmes
    second_last_update = stock.last_update

    assert first_last_update < second_last_update


def test_modify_stock():
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

    # Modify Corona price.
    stock.allocate(corona)
    corona.price = 130
    stock.allocate(corona)
    assert stock.beers["Corona"] == corona

    # Modify Quilmes quantity.
    stock.allocate(quilmes)
    quilmes.quantity = 5
    stock.allocate(quilmes)
    assert stock.beers["Quilmes"] == quilmes


def test_modify_beers_list_stock():
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

    stock.allocate([corona, quilmes])
    assert stock.beers["Corona"] == corona
    assert stock.beers["Quilmes"] == quilmes

    # Modify Corona price and Quilmes quantity.
    corona.price = 130
    quilmes.quantity = 5
    assert stock.beers["Corona"] == corona
    assert stock.beers["Quilmes"] == quilmes


def test_allocate_invalid_stock():
    stock = Stock()
    corona = Beer(
        name="Corona",
        price=115,
        quantity=2,
    )
    quilmes = Beer(
        name="Quilmes",
        price=120,
        quantity=-1,
    )
    with pytest.raises(OutOfStock, match="Quantity can not be negative"):
        stock.allocate([corona, quilmes])
