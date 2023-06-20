# Class Methods
# add functionality to a class itself, not to instances of that class
# @classmethod is a function that we can use to add functionality to a class as a whole

# Here’s an example of not using a class method
# import random

# class Hat:
#     def __init__(self) :
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# # Notice that hat = Hat() instantiates a hat
# hat = Hat()

# # The sort functionality is always handled by the instance of the class Hat
# # By executing hat.sort("Harry"), we pass the name of the student to the sort method of the particular instance of Hat, which we’ve called hat
# hat.sort("Arnold")

# We may want, though, to run the sort function without creating a particular instance of the sorting hat (there’s only one, after all!)
import random


class Hat:
    # Notice how the __init__ method is removed because we don’t need to instantiate a hat anywhere in our code
    # self, therefore, is no longer relevant and is removed
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # We specify this sort as a @classmethod, replacing self with cls
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# notice how Hat is capitalized by convention near the end of this code, because this is the name of our class
Hat.sort("Arnold")
