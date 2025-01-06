def assessment(names):
    """
    A function that evaluates student scores and returns results
    :param names:
    :return:
    """
    grades = {}
    while names:
        name = names.pop()
        grade = input(f"Talaba {name.title()}ning bahosini kiriting: ")
        grades[name] = int(grade)
    return grades


students = ['husan','hasan','malik','sardor']
grades1 = assessment(students[:])
print(grades1)
print(students)


def car_info(company, model, color, type, year, price = None):
    car = {
        "company": company,
        "model": model,
        "color": color,
        "type": type,
        "year": year,
        "price": price
    }
    return car

car1 = car_info("Chevrolet", "Lacetti", "white", "2015", "10000")
car2 = car_info("Chevrolet", "Nexia 3", "white", "2020", "9000")
cars = [car1, car2]
print(cars)
print(car1)
print(car2)