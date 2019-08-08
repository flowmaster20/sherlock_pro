from ui_sherlock_pro import *
import functions

name, surname, l_number, nickname, birthday_date, pet_name, known_username = get_data()

all_possibilites = l_number + nickname + birthday_date + pet_name + known_username
all_possibilites.append(name)
all_possibilites.append(surname)

everything = []
for word in all_possibilites:
    everything = everything + functions.create_mutations(word)
everything = everything + standard_set
everything = set(everything)
print(everything)
functions.create_all_combinations(everything)#podzielenie na pod tablice to multithreding
