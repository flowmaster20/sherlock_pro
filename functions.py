def create_mutations(word):
    tab = []
    for i in range(len(word)):
        tab.append(word[:i+1])
    return tab
