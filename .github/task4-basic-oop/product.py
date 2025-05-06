class Product:
    """
    A class to represent a product in inventory.
    """

    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("Price and quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount

    def remove_stock(self, amount):
        if amount > self.quantity:
            raise ValueError("Not enough stock to remove.")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} - ${self.price} × {self.quantity} units"

# Example usage
if __name__ == "__main__":
    p = Product("Pen", 1.5, 20)
    print(p)
    p.add_stock(5)
    p.remove_stock(3)
    print(f"Total value: ${p.total_value()}")