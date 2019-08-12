from ui_sherlock_pro import *
import functions
from multiprocessing import Pool
from looker.sherlock import *

if __name__ == '__main__':
    name, surname, l_number, nickname, birthday_date, pet_name, known_username = get_data()
    everything = functions.prepare(name, surname, l_number, nickname, birthday_date, pet_name, known_username)
    all = functions.idioticly_create_combinations(list(everything))

#wyswietlamy wszytskie utworzone nazwy uzytkownika
    for word in everything:
        main(word)
