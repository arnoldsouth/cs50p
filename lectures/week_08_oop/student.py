# Object-oriented Programming

# name = input("Name: ")
# house = input("House: ")
# print(f"{name} from {house}")


# abstract parts
# def main():
#     name = get_name()
#     house = get_house()

#     print(f"{name} from {house}")


# def get_name():
#     return input("Name: ")


# def get_house():
#     return input("House: ")


# if __name__ == "__main__":
#     main()


# tuple is a sequences of values. unlike a list, tuples can't be modified
# def main():
#     name, house = get_student()

#     print(f"{name} from {house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")

#     return name, house


# if __name__ == "__main__":
#     main()


# Packing that tuple, such that we are able to return both items to a variable called student
# tuples are immutable, meaning we cannot change those values
# Immutability is a way by which we can program defensively
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"

#     # notice how we can index into tuples using student[0] or student[1]
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")

#     # Notice that (name, house) explicitly tells anyone reading our code that we are returning two values within one
#     return name, house


# if __name__ == "__main__":
#     main()


# If we wanted to provide our fellow programmers flexibility, we could utilize a list as follows
# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]


# if __name__ == "__main__":
#     main()


# A dictionary could also be utilized in this implementation. Recall that dictionaries provide a key-value pair
# def main():
#     student = get_student()
#     print(f"{student['name']} from {student['house']}")


# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student
#     # Notice in this case, two key-value pairs are returned
#     # An advantage of this approach is that we can index into this dictionary using the keys


# if __name__ == "__main__":
#     main()


# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     # we can utilize the key names to index into our student dictionary
#     print(f"{student['name']} from {student['house']}")


# # Notice that there is an unneeded variable. We can remove student = {} because we don’t need to create an empty dictionary
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}
#     # Notice we can utilize {} braces in the return statement to create the dictionary and return it all in the same line


# if __name__ == "__main__":
#     main()


# Classes

# Classes are a way by which, in object-oriented programming, we can create our own type of data and give them names
# A class is like a mold for a type of data – where we can invent our own data type and give them a name


# We can modify our code as follows to implement our own class called Student
# Notice by convention that Student is capitalized
# class Student:
#     ...
#     # ... simply means that we will later return to finish that portion of our code


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# # we can create a student of class Student using the syntax student = Student()
# # notice that we utilize “dot notation” to access attributes of this variable student of class Student
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student
#     # Any time you create a class and you utilize that blueprint to create something, you create what is called an “object” or an “instance”. In the case of our code, student is an object


# if __name__ == "__main__":
#     main()


# Further, we can lay some groundwork for the attributes that are expected inside an object whose class is Student
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     # Notice that within Student, we standardize the attributes of this class
#     # We can create a function within class Student, called a “method”, that determines the behavior of an object of class Student
#     # Within this function, it takes the name and house passed to it and assigns these variables to this object


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     student = Student(name, house)
#     return student

#     # Further, notice how the constructor student = Student(name, house) calls this function within the Student class and creates a student. self refers to the current object that was just created


# if __name__ == "__main__":
#     main()


# We can simplify our code as follows
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

#     # Notice how return Student(name, house) simplifies the previous iteration of our code where the constructor statement was run on its own line


# if __name__ == "__main__":
#     main()


# Raise


# What if something goes wrong? What if someone tries to type in something random? What if someone tries to create a student without a name? Modify your code as follows
# class Student:
#     def __init__(self, name, house, patronus):
#         # Notice how we check now that a name is provided and a proper house is designated
#         # we can create our own exceptions that alerts the programmer to a potential error created by the user called raise
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#         # Notice how def __str__(self) provides a means by which a student is returned when called
#         # Therefore, you can now, as the programmer, print an object, its attributes, or almost anything you desire related to that object

#         # __str__ is a built-in method that comes with Python classes. It just so happens that we can create our own methods for a class as well


# def main():
#     student = get_student()
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)


# if __name__ == "__main__":
#     main()


# class Student:
#     def __init__(self, name, house, patronus=None):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
#             raise ValueError("Invalid patronus")
#         self.name = name
#         self.house = house
#         self.patronus = patronus

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell terrier":
#                 return "🐶
#             case _:
#                 return "🪄"

#     # Notice how we define our own method charm
#     # Unlike dictionaries, classes can have built-in functions called methods
#     # In this case, we define our charm method where specific cases have specific results


# def main():
#     student = get_student()
#     print("Expecto Patronumm ~~")
#     print(student.charm())


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ") or None
#     return Student(name, house, patronus)


# if __name__ == "__main__":
#     main()


# class Student:
#     def __init__(self, name, house, patronus=None):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     # Notice how we have only two methods: __init__ and __str__

# def main():
#     student = get_student()
#     student.house = "Number Four, Privet Drive"
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()


# Decorators
# Properties can be utilized to harden our code

# In Python, we define properties using function “decorators”, which begin with @
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Invalid name")
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"


#     # Getter for house
#     @property
#     def house(self):
#         return self._house

#     # Notice how we’ve written @property above a function called house
#     # Doing so defines house as a property of our class
#     # With house as a property, we gain the ability to define how some attribute of our class, _house, should be set and retrieved

#     # Setter for house
#     @house.setter
#     def house(self,house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house

#     # Indeed, we can now define a function called a “setter”, via @house.setter, which will be called whenever the house property is set—for example, with student.house = "Gryffindor"
#     # Here, we’ve made our setter validate values of house for us
#     # Notice how we raise a ValueError if the value of house is not any of the Harry Potter houses, otherwise, we’ll use house to update the value of _house

#     # Why _house and not house? house is a property of our class, with functions via which a user attempts to set our class attribute
#     # _house is that class attribute itself. The leading underscore, _, indicates to users they need not (and indeed, shouldn’t!) modify this value directly. _house should only be set through the house setter
#     # Notice how the house property simply returns that value of _house, our class attribute that has presumably been validated using our house setter

#     # When a user calls student.house, they’re getting the value of _house through our house “getter”


# def main():
#     student = get_student()
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()


# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     # Getter for name
#     @property
#     def name(self):
#         return self._name

#     # Setter for name
#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Invalid name")
#         self._name = name

#     # Getter for house
#     @property
#     def house(self):
#         return self._house

#     # Setter for house
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house


# def main():
#     student = get_student()
#     print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)


# if __name__ == "__main__":
#     main()


class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter for name
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")


def main():
    # Notice that get_student is removed and a @classmethod called get is created. This method can now be called without having to create a student first
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main()
