# m1 = input("First movie: ")
# m2 = input("Second movie: ")
# m3 = input("Third movie: ")

# list = []
# list.append(m1)
# list.append(m2)
# list.append(m3)
# print(list)

# ======================================================================

# # list = [1,2,3,2,1]
# list = [1,"abc", "abc", 1]

# cList = list.copy()
# cList.reverse()

# if list == cList:
#     print("It is palindrome")
# else:
#     print("It is not palindrome")

# ======================================================================

# grade = ["C", "D", "A", "A", "B", "B", "A"]
# grade.sort()
# print(grade)

# ======================================================================

# set = {"python", "java", "javascript", "C", "C++", "java", "java","C++", "python", "python"}
# print(len(set))

# ======================================================================

# subject = {}

# sub1 = int(input("Enter the marks of physics: "))
# sub2 = int(input("Enter the marks of english: "))
# sub3 = int(input("Enter the marks of maths: "))

# subject.update({"physics":  sub1})
# subject.update({"english":  sub2})
# subject.update({"maths":  sub3})

# print(subject)

# ======================================================================

# sets = {9, "9.0"}
# print(sets)

# ======================================================================

# n = 5
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
# print(factorial)

# ======================================================================

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod #decorator
#     def hello():
#         print("Hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg marks is: ", sum/3)


# s1 = Student("Rafay", [12, 32, 24])
# s1.get_avg()
# s1.hello()