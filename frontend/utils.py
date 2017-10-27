import random
import re

def generate_username(name):
    number = '{:03d}'.format(random.randrange(1, 999))

    name = name.strip()
    #name contain at least firstname and lastname
    if " " in name:
        first_letter = name[0][0].lower()

        #Get Last name
        reg_last_name = r"\s(\w+)$"
        last_name_search = re.search(reg_last_name, name)

        last_name = last_name_search.group().strip().lower()

        username = (first_letter + last_name + number)
    else :
        #Only firstname
        username = (name.strip().lower() + number)

    return username