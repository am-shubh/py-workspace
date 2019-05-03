# student
class Electronics:

    def __init__(self, brand: str, price: int):
        self.brand = brand
        self.price = price

    # unambiguous representation of objects
    def __repr__(self):
        return "Electronics({}, {})".format(self.brand, self.price)

    # readable representation of objects
    def __str__(self):
        return "Brand Name => {}, Price => {}".format(self.brand, self.price)

    def __avgPrice__(self, other):
        return (self.price + other.price) / 2

    def __add__(self, other):
        return self.price + other.price
    

device1 = Electronics('samsung', 45000)
device2 = Electronics('LG', 56000)

print(device1)
print(repr(device1))
print(str(device1))

print(Electronics.__avgPrice__(device1, device2))

print(device1 + device2)
