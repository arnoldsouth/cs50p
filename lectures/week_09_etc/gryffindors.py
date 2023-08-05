# https://cs50.harvard.edu/python/2022/notes/9/#list-comprehensions

# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]


# gryffindors = []
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]

# gryffindors = [
#     student["name"]
#     for student in students
#     if student["house"] == "Gryffindor"
#     # Notice how the list comprehension is on a single line!
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]


# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"


# gryffindors = filter(is_gryffindor, students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])


# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]


# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])
# # Notice how the same list of students is provided.


# https://cs50.harvard.edu/python/2022/notes/9/#dictionary-comprehensions

# students = ["Hermione", "Harry", "Ron"]

# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# print(gryffindors)


# students = ["Hermione", "Harry", "Ron"]

# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

# print(gryffindors)


# students = ["Hermione", "Harry", "Ron"]

# gryffindors = {student: "Gryffindor" for student in students}

# print(gryffindors)

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

# Notice how enumerate presents the index and the value of each student.
