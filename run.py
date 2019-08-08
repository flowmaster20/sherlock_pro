from ui_sherlock_pro import *
import functions

name, surname, l_number, nickname, birthday_date, pet_name, known_username = get_data() #wrzucam kolejne zmnienne z funckcji do kolejnych zmieennnych


#dodaje wszytskie elementy i tablice w jedna
all_possibilites = l_number + nickname + birthday_date + pet_name + known_username
all_possibilites.append(name)
all_possibilites.append(surname)


#dla kazdego slowa tworze jego mutacje tzn auto --> a ,au ,aut ,auto
everything = []
for word in all_possibilites:#idzie przez wszytskie slowa
    everything = everything + functions.create_mutations(word)#robi mutacje slowa word
everything = everything + standard_set#dodaje standard set w zamysle rzeczy takie jak kropki podkreslnki itd ktore beda takie same zawsze
everything = set(everything)#usuwa powtorzenia i sortuje
print(everything)


functions.create_all_combinations(everything)#podzielenie na pod tablice to multithreding
