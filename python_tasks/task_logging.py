# # 1 užduotis

# # Sukurti funkcijas, kurios:

# # # Gražintų visų paduotų skaičių sumą (su *args argumentu)
# # # Gražintų paduoto skaičiaus šaknį (panaudoti math.sqrt())
# # # Gražintų paduoto sakinio simbolių kiekį (su len())
# # # Gražintų rezultatą, skaičių x padalinus iš y

# import math

# def sum(*args):
#     total = 0
#     for x in args:
#         total += x
#     return total

# sum(2, 5, 6)

# def square_root(x: float) -> float:
#     answer = math.sqrt(x)
    # logging.info(f'square root: {answer}')
 
#     return answer

# print(square_root(9))

# def len_of_sentence(x) -> int:
#     answer = len(x)
#     return answer

# print(len_of_sentence("How we doing?"))

# def divide (x, Y) -> int:
#     return x / Y

# print(divide(9, 3))


# Nustatyti standartinį logerį (logging) taip, kad jis:

# Saugotų pranešimus į norimą failą
# Saugotų INFO lygio žinutes
# Pranešimai turi būti tokiu formatu: data/laikas, lygis, žinutė

import logging

# logging.basicConfig(filename='matematika.log', level=logging.DEBUG)
logging.basicConfig(filename='aritmetika.log',
 level=logging.DEBUG, 
 format='%(asctime)s:%(levelname)s:%(message)s')



def sum(*args):
    total = 0
    for x in args:
        total += x
    
    logging.debug(f'suma: {total}')
    print(total)
    logging.basicConfig(filename='aritmetika.log',
 level=logging.DEBUG, 
 format='%(asctime)s:%(levelname)s:%(message)s')
    
    return total


print(sum(2, 5, 6))