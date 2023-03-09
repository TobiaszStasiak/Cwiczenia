class Restaurant():

	def __init__(self, name, cuisine_type):
		self.name = name.title()
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		msg = (f"{self.name} serwuje niesamowite {self.cuisine_type}")
		print(f"\n{msg}")

	def open_restaurant(self):
		msg = (f"{self.name} jest otwarta, zapraszam")
		print(f"\n{msg}")

restaurant = Restaurant('Karczma', 'pizza')
restaurant_1 = Restaurant('Zapiecek', 'obiady')
restaurant_2 = Restaurant('Stusk', 'gofry')

restaurant_2.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.open_restaurant()