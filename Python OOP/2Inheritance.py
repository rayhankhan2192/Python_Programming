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



#Inheritance
class Phone(Item):#Phone extend item
      def __init__(self, name: str, price: float, quantity: int, brokenPhone = 0):
        #call the super function to access the all attribute/method of parents class
        super().__init__(
            name, price, quantity
        )
        
        #Validation to the recived argumrnt
        assert brokenPhone>=0, f"Input valid Broken number"

        #value assign to self object
        self.brokenPhone = brokenPhone

print("\nInheritance\n")
Phone1 = Phone("Samsung", 100, 3, 1)
print("Phone1:",Phone1.calculate_total_price())


Phone2 = Phone("OPPO", 200, 5, 2)
print("Phone2:",Phone2.calculate_total_price())
Phone2.pay_rate = 0.9
Phone2.apply_discount()
print("Phone2 after Discount: ",Phone2.calculate_total_price())
