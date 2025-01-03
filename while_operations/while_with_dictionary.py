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