# Automat de cafea
# cu if-uri
#
# pret_capuccino = 4
# pret_cafea = 3.5
#
#
# print(f'''
# Meniu
# 1. Capuccino ... {pret_capuccino}
# 2. Cafea ... {pret_cafea}''')
#
# optiune = input('Alege o optiune [1,2]: ')
# if optiune == str(1):
#     plata = int(input('Introduceti o bancnota [5, 10] '))
#     print(f'Ai ales capuccino.\nVei primi rest de {plata- pret_capuccino} lei\nProdusul se livreaza...')
# elif optiune == str(2):
#     plata = int(input('Introduceti o bancnota [5, 10] '))
#     print(f'Ai ales cafea.\nVei primi rest de {plata - pret_cafea} lei\nProdusul se livreaza...')
# else:
#     print('optiune incorecta.')


# #     #########################################################################################################
#
# pret_capuccino = 4
# pret_cafea = 3.5
#
#
# print(f'''
# Meniu
# 1. Capuccino ... {pret_capuccino}
# 2. Cafea ... {pret_cafea}''')
#
# optiune = input('Alege o optiune [1,2]: ')
# if optiune == str(1):
#     plata = input('Introduceti o bancnota [5, 10] ')
#     if plata == str(5) or plata == str(10):
#         print(f'Ai ales capuccino.\nVei primi rest de {float(plata) - float(pret_capuccino)} lei\nProdusul se livreaza...')
#         break
#     else:
#         print('suma incorecta')
#
#
#
# elif optiune == str(2):
#     plata = input('Introduceti o bancnota [5, 10] ')
#     if plata == str(5) or plata == str(10):
#         print(f'Ai ales cafea.\nVei primi rest de {float(plata) - float(pret_cafea)} lei\nProdusul se livreaza...')
#     else:
#         print('suma incorecta')
# else:
#     print('optiune incorecta.')
##############################################################################################################
# OK-ish

# pret_capuccino = 4
# pret_cafea = 3.5
#
# print(f'''
# Meniu
# 1. Capuccino ... {pret_capuccino}
# 2. Cafea ... {pret_cafea}''')
#
# optiune = input('Alege o optiune [1,2]: ')
# if optiune == str(1):
#     plata = input('Introduceti o bancnota [5 lei, 10 lei] ')
#     while plata != str(5) and plata != str(10):
#         plata = input('suma incorecta. introdu o bancnota valida [5 lei, 10 lei]:')
#     else:
#         print(
#             f'Ai ales capuccino.\nVei primi rest de {float(plata) - float(pret_capuccino)} lei\nProdusul se livreaza...')
# elif optiune == str(2):
#     plata = input('Introduceti o bancnota [5 lei, 10 lei] ')
#     while plata != str(5) and plata != str(10):
#         plata = input('suma incorecta. introdu o bancnota valida [5 lei, 10 lei]:')
#     else:
#         print(
#             f'Ai ales cafea.\nVei primi rest de {float(plata) - float(pret_cafea)} lei\nProdusul se livreaza...')
# else:
#     print('optiune incorecta.')
################################################################################################################

# #
# pret_capuccino = 4
# pret_cafea = 3.5
#
# print(f'''
# Meniu
# 1. Capuccino ... {pret_capuccino}
# 2. Cafea ... {pret_cafea}''')
#
# optiune = input('Alege o optiune [1,2]: ')
# while optiune != str(1) and optiune != str(2):
#     optiune = input('Optiune invalida. Alege o optiune [1,2]: ')
#     continue
# else:
#     if optiune == str(1):
#         plata = input('Introduceti o bancnota [5 lei, 10 lei] ')
#         while plata != str(5) and plata != str(10):
#             plata = input('suma incorecta. introdu o bancnota valida [5 lei, 10 lei]:')
#             if plata == str(5) or plata == str(10):
#                 print(
#                     f'Ai ales capuccino.\nVei primi rest de {float(plata) - float(pret_capuccino)} lei\nProdusul se livreaza...')
#                 break
#     elif optiune == str(2):
#         plata = input('Introduceti o bancnota [5 lei, 10 lei] ')
#         while plata != str(5) and plata != str(10):
#             plata = input('suma incorecta. introdu o bancnota valida [5 lei, 10 lei]:')
#             if plata == str(5) or plata == str(10):
#                 print(
#                     f'Ai ales cafea.\nVei primi rest de {float(plata) - float(pret_cafea)} lei\nProdusul se livreaza...')
#                 break
# #


############################################################################################################
#
#
# pret_capuccino = 4
# pret_cafea = 3.5
# plata = int()
# optiuni = ['1', '2']
#
# print(type(optiuni))
#
# print(f'''
# Meniu
# 1. Capuccino ... {pret_capuccino}
# 2. Cafea ... {pret_cafea}''')
#
#
# optiune = input('Alege o optiune [1,2]: ')
# while optiune in optiuni:
#     plata = input('Introduceti o bancnota [5, 10] ')
#     if plata == str(5):
#         print(f'Ai ales cafea.\nVei primi rest de {float(plata) - float(pret_cafea)} lei\nProdusul se livreaza...')
#     else:
#         print('suma incorecta')
#
#     break
#
# else:
#     print('gresit')
# #
###################################################################################3

pret_capuccino = 4
pret_cafea = 3.5

print(f'''Meniu\n1. Capuccino ... {pret_capuccino}\n2. Cafea ... {pret_cafea}''')

optiune = input('\nAlege o optiune [1,2]: ')
while optiune != str(1) and optiune != str(2):
    optiune = input('Optiune invalida. Alege o optiune [1,2]: ')
    continue
else:
    if optiune == str(1):
        plata = input('Introduceti o bancnota [5 lei, 10 lei]: ')
        while plata != str(5) and plata != str(10):
            plata = input('suma incorecta. introdu o bancnota valida [5 lei, 10 lei]: ')
        else:
            print(
                f'Ai ales capuccino.\nVei primi rest de {float(plata) - float(pret_capuccino)} lei\nProdusul se livreaza...')
    elif optiune == str(2):
        plata = input('Introduceti o bancnota [5 lei, 10 lei]: ')
        while plata != str(5) and plata != str(10):
            plata = input('suma incorecta. introdu o bancnota valida [5 lei, 10 lei]: ')
        else:
            print(
                f'Ai ales cafea.\nVei primi rest de {float(plata) - float(pret_cafea)} lei\nProdusul se livreaza...')
