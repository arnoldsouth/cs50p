class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


# Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard as the line super().__init__(name) runs the init method of Wizard
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts ")

# both Student and Professor inherit the characteristics of Wizard. Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard as the line super().__init__(name) runs the init method of Wizard
# Both students and professors have names. Also, both students and professors are wizards. Therefore, both Student and Professor inherit the characteristics of Wizard
# Finally, notice that the last lines of this code create a wizard called Albus, a student called Harry, and so on


# Inheritance and Exceptions
# It just so happens that exceptions come in a heirarchy, where there are children, parent, and grandparent classes. These are illustrated below:
# BaseException
#  +-- KeyboardInterrupt
#  +-- Exception
#       +-- ArithmeticError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- KeyError
#       +-- NameError
#       +-- SyntaxError
#       |    +-- IndentationError
#       +-- ValueError
