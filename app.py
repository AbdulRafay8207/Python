# course = "Python Programming"
# print(len(course))
# print(course[0: 4])

# first = "Abdul"
# last = "Rafay"
# full = F"{first} {last}"
# print(full)

# ============================ Methods ============================

# course = "  Python Programming"
# print(course)
# print(course.strip()) In JS we use trim to remove white space and in Python we use strip

# course = "Python Programming"
# print(course.find("Pro"))
# print(course.replace("P","j"))
# print("Pro" in course) this one is like .includes() method from JS
# print("run" not in course)

# ============================ Arithmetic Operations ============================

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 % 3)
# print(10 // 3) # To avoid floats
# print(10 ** 3) # is like 10 to the power of 3

# ============================ Input From User ============================

# x = input("x: ")
# y = int(x) + 1
# print(y)

# ============================ If, else if, else satement ============================

# temperature = 12
# if temperature > 30:
#     print("Too hot today")
#     print("Stay hyderated")
# elif temperature > 20:
#     print("Better")
# else:
#     print("cold")

# ============================ Python Ternary Operator ============================

# age = 18

# message = "Eligible" if age >= 18 else "Not eligilble"
# print(message)

# ============================ And, Or, Not Operator ============================

# high_income = True
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("Eligible")
# else:
#     print("Not eligible")

# ============================ For Loop, For...Else, Nested Loop ============================

# for number in range(1, 10, 2):
#     print("Ola", number, (number + 1) * ".")

# successfull = False
# for number in range(3):
#     print("Attempt")
#     if successfull:
#         print("Successfull")
#         break
# else:
#     print("Attempted 3 times and failed.")

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# for char in "Python":
#     print(char)

# ============================ While loop ============================

# command = ""
# while command.lower() != "quite":
#     command = input(">")
#     print("ECHO", command)

# ============================ While loop ============================

# total = 0
# for x in range(1, 10):
#     if (x % 2) == 0:
#         print(x)
#         total += 1
# else:
#     print(f"we have {total} even numbers")

# ============================ Function ============================

# def greeting(name):
#     return f"Hi {name}"
#     # print(f"Hi {name}")


# # greet = greeting("Abdul")
# print(greeting("Abdul"))

# ============================ List ============================

# list = [3,5,1,6,1]
# # list.append(4)
# # list.sort(reverse=True)
# # list.reverse()
# # list.insert(1,2)
# # list.remove(1) # Remove first occurence
# # list.pop(2)
# print(list)

# ============================ Tuple ============================

# tup = (1,2,3,4)
# tup1 = (1,) # We create tup which contain single element like this, other wise python will understand it as an integer
# tup2 = (1) # This is an integer
# print(type(tup))
# print(tup)

# ============================ Dictionary ============================

# student = {
#     "name": "Abdul",
#     "age" : "18",
# }

# # print(student.get("name")) # If wrong key, then it returns none instead of error
# # print(student["name"]) # If wrong key, it will throw error.

# student["city"] = "Karachi"
# student.update({"Job": "Dev"})
# print(student)

# ============================ Dictionary ============================

# collections = {1,2,3,4,4,5,5,"hello","hello", 2, 1,9}

# print(type(collections))
# print(collections)

# To create an empty set:

# set = {1,2,3,4,5,6}
# set = set()
# set.add(1)
# set.add(2)
# set.add(3)
# set.add(4)
# set.add(5)
# # set.remove(1)
# # set.clear()
# set.pop() # It removes random values, but im seeing it alawys remove first value.
# print(set)

# ---- union and intersection ----

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.intersection(set2))

# ============================ Class ============================

class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("hi")
    print("ola")

s1 = Students("Abdul", 20)
s2 = Students("Rafay", 90)
print(s1.name)
print(s2.marks)
