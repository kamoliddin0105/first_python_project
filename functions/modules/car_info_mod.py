def car_info(company, model, color, type, year, price=None):
    """
    function that wraps the machine into a dictionary
    :param company:
    :param model:
    :param color:
    :param type:
    :param year:
    :param price:
    :return:
    """
    car = {
        'company': company,
        'model': model,
        'color': color,
        'type': type,
        'year': year,
        'price': price
    }
    return car


def auto_enter():
    """
    adding data by the user with car_info() function
    :return:
    """
    cars = []
    while True:
        print("Enter the following information")
        company = input("Company name: ")
        model = input("Model: ")
        color = input("Color: ")
        type = input("Type: ")
        year = input("Year: ")
        price = input("Price: ")
        cars.append(car_info(company, model, color, type, year, price))

        answer = input("Continue? (y/n): ")
        if answer == "n":
            break
    return cars

def info_print(car_info):
    """
    A function that outputs a dictionary containing a list of cars to the console
    :param car_info:
    :return:
    """
    print(f"{car_info['color'].title()} {car_info['company'].upper()} "
          f"{car_info['model'].upper()}, {car_info['type']} korobka, "
          f"{car_info['year']}-yil, {car_info['price']}$")

