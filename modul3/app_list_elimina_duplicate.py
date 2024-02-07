# remove duplicates from a list
# cu doua liste
# duplicated = [1, 3, 4, 5, 6, 7, 7, 7, 7, 9, 3]
# new_list = []
# lista_duplicate = []
#
# for element in duplicated[::]:
#     if element not in new_list:
#         new_list.append(element)
#     else:
#         print(element, 'is duplicate')
#         lista_duplicate.append(element)
#
# print(duplicated, 'lista bruta')
# print(new_list, 'lista cu unice')
# print(lista_duplicate, 'elemente duplicate')


duplicated = [1, 3, 5, 7, 7, 7, 7, 7, 9, 3]  # remove duplicates

new_list = []
for number in duplicated[::]:
    if number not in new_list:
        new_list.append(number)
    else:
        duplicated.remove(number)
        print(number, 'is duplicate')

duplicated.sort()
print(new_list)
print(duplicated)