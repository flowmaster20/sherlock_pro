def create_mutations(word):
    tab = []
    for i in range(len(word)):
        # dla kazdej mozliwej dlugosci slowa tworze osobna zmienna i dodaje ja do tablicy ktora zwracam
        tab.append(word[:i + 1])
    return tab


def prepare(name, surname, l_number, nickname, birthday_date, pet_name, known_username):

    # dodaje wszytskie elementy i tablice w jedna
    all_possibilites = l_number + nickname + \
        birthday_date + pet_name + known_username
    all_possibilites.append(name)
    all_possibilites.append(surname)

    # dla kazdego slowa tworze jego mutacje tzn auto --> a ,au ,aut ,auto
    everything = []
    for word in all_possibilites:  # idzie przez wszytskie slowa
        # robi mutacje slowa word
        everything = everything + create_mutations(word)
    # + standard_set#dodaje standard set w zamysle rzeczy takie jak kropki podkreslnki itd ktore beda takie same zawsze
    everything = everything
    everything = set(everything)  # usuwa powtorzenia i sortuje
    # print(everything)
    return everything

    # functions.create_all_combinations(everything)#podzielenie na pod tablice to multithreding


"""
def create_all_combinations(tab,how_many):
    for i in range(how_many**len(tab)): #jakis pomysl na laczenie wszytskich wyrazow do siebie ale na razie jeszcze sam nie wiem jak to ma dzialac do konca
"""


def idioticly_create_combinations(tab):
    all = []

    # losujemy wszytskie kombinacje z  3 skladinikow tabeli
    for x in range(len(tab)):
        for y in range(len(tab)):
            for z in range(len(tab)):
                # laczymy 3 skladni ki w jeden
                query = tab[x] + tab[y] + tab[z]
                all.append(query)  # dodajemy do tablicy wynikow
    all.sort()  # soortujemy tablice alfabetycznie
    return all
