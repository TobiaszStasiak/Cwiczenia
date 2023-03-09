class User():

	def __init__(self, first_name, last_name, email, location):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.email = email
		self.location = location.title()

	def describe_user(self):
		print(f"\n{self.first_name} {self.last_name}")
		print(f"email: {self.email}")
		print(f"Lokalizacja: {self.location}")
	
	def greet_user(self):
		print(f"\nWitaj ponownie {self.first_name}")

tobiasz = User('tobiasz', 'stasiak', 'tobiasz.stasiak@o2.pl', 'dobra')

tobiasz.describe_user()
tobiasz.greet_user()

