class Restaurant():
	def __init__(self, name, time):
		self.name = name
		self.time = time

	def nazwa(self):
		print(f"Restauracja nazywa się {self.name.title()}.")

	def godziny(self):
		print(f"Restauracja otwierana jest o godzinie {self.time}")

my_restaurant = Restaurant('karczma', 6)

print(f"Nazwa restauracji {my_restaurant.name.title()}")
print(f"Restauracja zayczna pracę o {my_restaurant.time}")
my_restaurant.godziny()
my_restaurant.nazwa()

