class Dog:
	"""Object class"""

	def speak(self):
		return "Woof!"

	def __str__(self):
		return "Dog"


class DogFactory:
	"""Concrete Factory"""

	def get_pet(self):
		return Dog()

	def get_food(self):
		return "Dog Food!"


class PetStore:
	"""Abstract Factory"""

	def __init__(self, pet_factory=None):

		self._pet_factory = pet_factory


	def show_pet(self):

		pet = self._pet_factory.get_pet()
		pet_food = self._pet_factory.get_food()

		print("Our pet is '{}'!".format(pet))
		print("Our pet says hello by '{}'".format(pet.speak()))
		print("Its food is '{}'!".format(pet_food))


factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()

