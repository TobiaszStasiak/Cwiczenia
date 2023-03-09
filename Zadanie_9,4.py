class Restaurant():
	def __init__(self, name, time, number_served):
		self.name = name
		self.time = time
		self.number_served = number_served

	def nazwa(self):
		print(f"Restauracja nazywa się {self.name.title()}.")

	def godziny(self):
		print(f"Restauracja otwierana jest o godzinie {self.time}")

	def describe_restaurant(self):
		msg = f"{self.name.title()} jest otwarta od {self.time} i obsłużyła {self.number_served} gości"
		print(f"\n{msg}")

	def increment_number_served(self, additional_served):
		self.number_served += additional_served

my_restaurant = Restaurant('karczma', 6, 100)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(342)
my_restaurant.describe_restaurant()