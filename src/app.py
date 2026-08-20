# src/app.py
# list_products: William Cortez
# add_product: Karina Barragán
# filter_products_by_date: William Cortez

products = []


def list_products():
    """Retorna los productos registrados en la mini juguetería."""
    return products


def add_product(name, qty, entry_date=None):
    """Agrega un producto después de validar su nombre y cantidad."""
    if not name:
        raise ValueError("name required")

    if qty < 0:
        raise ValueError("qty must be >= 0")

    product = {"name": name, "qty": qty}

    if entry_date:
        product["entry_date"] = entry_date

    products.append(product)
    return True


def filter_products_by_date(entry_date):
    """Retorna los productos registrados en una fecha determinada."""
    return [
        product
        for product in products
        if product.get("entry_date") == entry_date
    ]