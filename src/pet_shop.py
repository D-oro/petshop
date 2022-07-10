# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    name = pet_shop["name"]
    return name

def get_total_cash(pet_shop):
    sum = pet_shop["admin"]["total_cash"]
    return sum

def add_or_remove_cash(pet_shop, number):
    pet_shop["admin"]["total_cash"]+= number

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, count):
    pet_shop["admin"]["pets_sold"] += count

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# def all_pets_by_breed():

# def all_pets_by_breed_not_found()

def find_pet_by_name(pet_shop, pet):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet:
            return pet

def remove_pet_by_name(pet_shop, pet):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet:
            del pet["name"]

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash (customers):
    return customers["cash"]


# def remove_customer_cash (customer, number):
#     result = (customer["cash"] - number)
#     return result

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)    