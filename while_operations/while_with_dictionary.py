cars = ['nexia','lacetti','BMW','Mers.jpg','nexia','Volvo','nexia']
print(cars)
car = 'nexia'
while car in cars:
    cars.remove('nexia')
print(cars)

print("Do'stlarni yoshiga qo'shib saqlaymiz......")
friends = {}
lamp = True
while lamp:
    name = input("Do'stingizni ismini kiriting: ")
    age = input(f"{name.title()}ning yoshini kiriting: ")
    friends[name] = int(age)
    answer = input("Yana do'stingizni qo'shasimi (ha/yo'q)")
    if answer != "ha":
        lamp = False

for name, age in friends.items():
    print(f"{name.title()} {age} yoshda")
print("dastur tugadi")

print(friends)

students = ['hasan','husan','fotima','zuxra']
graded_students = {}

while students:
    student = students.pop()
    grade = input(f"{student.title()}ning bahosini kiriting: ")
    print(f"{student.title()} baholandi")
    graded_students[student] = int(grade)
print(graded_students)