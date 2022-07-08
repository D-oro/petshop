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
