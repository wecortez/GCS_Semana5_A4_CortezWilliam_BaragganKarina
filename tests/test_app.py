# tests/test_app.py
# Responsable: Karina Barragán

from src.app import add_product, list_products


def test_add_and_list():
    add_product("Oso de peluche", 3)

    assert {"name": "Oso de peluche", "qty": 3} in list_products()