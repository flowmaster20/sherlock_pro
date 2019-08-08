def create_mutations(word):
    tab = []
    for i in range(len(word)):
        tab.append(word[:i+1]) #dla kazdej mozliwej dlugosci slowa tworze osobna zmienna i dodaje ja do tablicy ktora zwracam
    return tab

def create_all_combinations(tab,how_many):
    for i in range(how_many**len(tab)): #jakis pomysl na laczenie wszytskich wyrazow do siebie ale na razie jeszcze sam nie wiem jak to ma dzialac do konca
