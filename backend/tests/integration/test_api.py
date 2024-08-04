from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_get_order_success(order):
    response = client.get("/api/v1/orders/order-1")
    assert response.status_code == 200
    assert response.json().get("subtotal") == order.subtotal
    assert len(response.json().get("items")) == len(order.items)
    assert len(response.json().get("rounds")) == len(order.rounds)


def test_get_order_structure(order):
    response = client.get("/api/v1/orders/order-1")
    assert response.status_code == 200
    data = response.json()
    items = data["items"]
    # Corona.
    item_corona = items[0]
    assert item_corona["name"] == "Corona"
    assert item_corona["price_per_unit"] == 115
    assert item_corona["total"] == 2
    # Club Colombia.
    item_corona = items[1]
    assert item_corona["name"] == "Club Colombia"
    assert item_corona["price_per_unit"] == 110
    assert item_corona["total"] == 2


def test_not_found_order():
    response = client.get("/api/v1/orders/invalid-order")
    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}
    # A not instanciated order.
    response = client.get("/api/v1/orders/order-1")
    assert response.status_code == 404
    assert response.json() == {"detail": "Order not found"}
