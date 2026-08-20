# src/app.py
# Función list_products: William Cortez
# Función add_product: Karina Barragán

products = []


def list_products():
    """Retorna los productos registrados en la mini juguetería."""
    return products


def add_product(name, qty):
    """Agrega un producto después de validar su nombre y cantidad."""
    if not name:
        raise ValueError("name required")

    if qty < 0:
        raise ValueError("qty must be >= 0")

    products.append({"name": name, "qty": qty})
    return True