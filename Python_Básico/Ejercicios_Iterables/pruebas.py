
first_list = [
	'A',
	'B',
	'C',
]

second_list = [
	'D',
	'E',
	'F',
]

first_list.extend(second_list)
print(first_list)




my_favorite_records = [
	'Dark Side Of The Moon','Fear of a Blank Planet','Signify',
]

for index in range(0, len(my_favorite_records)):
	record = my_favorite_records[index]
	print(f'Record {index}: {record}')

print("                  ")
print("                  ")

my_string = "Pizza con piña"

# [inicio:fin:paso] -> al dejar inicio y fin vacíos y paso -1, invierte todo
for letra in my_string[::-1]:
    print(letra)

print("                  ")
print("                  ")

