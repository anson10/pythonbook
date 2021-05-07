class Restaurant():
    def __init__(self,restaurant_name,cuisine_style):
        self.restaurant_name = restaurant_name
        self.cuisine_style = cuisine_style
    def describe_restaurant(self):
        print(f"{self.restaurant_name} is worth a shot")
        print(f"{self.restaurant_name} is famous for their {self.cuisine_style} flavor")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is opened!")

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_style = "icecream"):
        super().__init__(restaurant_name,cuisine_style)
        self.flavours = []

    def display_flavours(self):
        print("We have the following flavours :")
        for flavor in self.flavours:
            print(f" - {flavor}")


hotel1 = Restaurant("Pizza Hut","Italian")
hotel2 = Restaurant("KFC" , "Fast Food")
hotel3 = Restaurant("King's Chic","Chinise")

ice_cream1 = IceCreamStand("The Jumbo One")
ice_cream1.flavours = ["Chocolate" , "Vannila" , "ButterScotch"]
hotel1.describe_restaurant()
hotel2.describe_restaurant()
hotel3.describe_restaurant()

ice_cream1.display_flavours()