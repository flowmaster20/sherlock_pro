from ui_sherlock_pro import *
import functions

if __name__ == '__main__':
    name, surname, l_number, nickname, birthday_date, pet_name, known_username = get_data()
    everything = functions.prepare(name, surname, l_number, nickname, birthday_date, pet_name, known_username)
    all = functions.idioticly_create_combinations(list(everything))

    for word in everything:
        print(word,"\n")
