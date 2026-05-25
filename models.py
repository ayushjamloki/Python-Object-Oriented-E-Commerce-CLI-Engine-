# 1. PARENT CLASS 
class Product:
    def __init__(self, p_id, name, price, stock):
        self.p_id = p_id
        self.name = name
        self.price = price
        self.stock = stock

    def get_details(self):
        return f"[{self.p_id}] {self.name} | Price: ₹{self.price} | Stock: {self.stock}"


# 2. CHILD CLASS 1 (Electronics) 
class ElectronicItem(Product):
    def __init__(self, p_id, name, price, stock, warranty_months):
        
        super().__init__(p_id, name, price, stock) 
        self.warranty_months = warranty_months

    # Polymorphism
    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} ⚡ [Warranty: {self.warranty_months} Months]"


class AccessoryItem(Product):
    def __init__(self, p_id, name, price, stock, material):
        super().__init__(p_id, name, price, stock)
        self.material = material

    def get_details(self):
        base_details = super().get_details()
        return f"{base_details} 🛠️ [Material: {self.material}]"