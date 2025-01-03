print("Do'stlar ro'yhatini tuzamiz")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingiz ismini kiriting"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana is qo'shasizmi (ha/yo'q)")
    n += 1
    if takrorlash != "ha":
        break


print("Do'stlar ro'yhati")
i = 1
for ism in ismlar:
    print(i ,"-", ism.title())
    i += 1
print("Dastur tugadi")
