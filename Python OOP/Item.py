class Item:
    pay_rate = 0.8 #Instance variable

    #constructor in Python
    def __init__(self, name: str, price: float, quantity: int):
        #Validation to the recived argumrnt
        assert price>=0, f"Input the valid price"
        assert quantity>=0, f"Input the valid quantity"

        #value assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    #Method in python   
    def calculate_total_price(self):
        return self.price * self.quantity
    #Method in Python
    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = Item("Phone", 20, 10)
item1.apply_discount()
print("Item1 :",item1.calculate_total_price())

item2 = Item("laptop", 30, 10)
item2.pay_rate = 0.5
item2.apply_discount()
print("Item2 :",item2.calculate_total_price())
