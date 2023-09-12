from Item import Item

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
