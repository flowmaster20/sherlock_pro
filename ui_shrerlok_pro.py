import json as j

print("helloworld!")

# arkusz = open("arkusz.json")
# print(arkusz)


name = input("paste name:")
surname = input("paste surname:")
l_number = input("paste any known lucky numbers:").split(",")
nickname = input("paste any known nicknames:").split(",")
print("date format must be days.monts.year like: 24.04.1998")
birthday_date = input("paste birthday date:").split(".")
pet_name = input("paste any known pet names:").split(",")
known_username = input("paste any known usernames, that were used on socjal media before:").split(",")
print(name, surname, l_number, nickname, birthday_date, pet_name, known_username)
