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

def greeting(name):
    return f"Hi {name}"
    # print(f"Hi {name}")


# greet = greeting("Abdul")
print(greeting("Abdul"))
