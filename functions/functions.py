print("Salom beruvchi funksiya")
def salom_ber(ism):
    print(f"Assalomu alaykum {ism.title()}")

salom_ber("Kamoliddin")

def full_name(first_name, last_name):
    """
    Printing the full name of a given name
    :param first_name:
    :param last_name:
    """
    print(f"{first_name} {last_name}")

full_name(first_name="John", last_name="Smith")


def calculate_age(birthday,name):
    """
    Printing the age of a given name
    :param birthday:
    :param name:
    """
    print(f"name: {name}, age: {2024 - birthday}")


calculate_age(birthday=2007, name="Kamoliddin")

def create_full_name(first_name, last_name):
    """
    Returns a full name given a first name and last name.
    :param first_name:
    :param last_name:
    :return:
    """
    full_name = f"{first_name} {last_name}"
    return full_name

full_name(first_name="John", last_name="Smith")


def calculate_age(birthday,name):
    """
    Printing the age of a given name
    :param birthday:
    :param name:
    """
    print(f"name: {name}, age: {2024 - birthday}")

calculate_age(birthday=2007, name="Kamoliddin")

