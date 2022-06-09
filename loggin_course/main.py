# # # def dalyba(a, b):
# # #     return a / b

# # # a = 10
# # # b = 5

# # # padalinom = dalyba(a, b)
# # # print(f"Dalyba: {a} / {b} = {padalinom}")

# # # # Dalyba: 10 / 5 = 2.0

# # # import logging

# # # def dalyba(a, b):
# # #     return a / b

# # # a = 10
# # # b = 5

# # # # padalinom = dalyba(a, b)
# # # # logging.warning(f"Dalyba: {a} / {b} = {padalinom}")

# # # # # WARNING:root:Dalyba: 10 / 5 = 2.0

# # # # import logging

# # # # logging.basicConfig(
# # # #     filename='aritmetika.log', 
# # # #     level=logging.DEBUG,
# # # #     format="%(asctime)s:%(levelname)s:%(messege)s",)

# # # import logging

# # # logging.basicConfig(filename='asmenys.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

# # # class Asmuo:

# # #     def __init__(self, vardas, pavarde):
# # #         self.vardas = vardas
# # #         self.pavarde = pavarde
# # #         logging.info(f"Sukurtas darbuotojas: {self.vardas} {self.pavarde}")

# # # tadas = Asmuo("Tomas", "Kucinskas")
# # # rokas = Asmuo("Rokas", "Radzevicius")


# # import logging
# # logger = logging.getLogger(__name__)
# # file_handler = logging.FileHandler('aritmetika.log') #bus logai rasomi i aritmetikia.log
# # logger.addHandler(file_handler)

# # logger.setLevel(logging.DEBUG)

# # formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# # file_handler.setFormatter(formatter)

# # def dalyba(a, b):
# #     return a / b

# # a = 10
# # b = 5

# # padalinom = dalyba(a, b)
# # logger.info(f"Dalyba: {a} / {b} = {padalinom}")


# # import logging
# # logger = logging.getLogger(__name__)
# # file_handler = logging.FileHandler('aritmetika.log')
# # logger.addHandler(file_handler)

# # logger.setLevel(logging.DEBUG)

# # formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# # file_handler.setFormatter(formatter)

# # stream_handler = logging.StreamHandler()
# # stream_handler.setFormatter(formatter)
# # logger.addHandler(stream_handler)

# # def dalyba(a, b):
# #     return a / b

# # a = 10
# # b = 5

# # padalinom = dalyba(a, b)
# # logger.info(f"Dalyba: {a} / {b} = {padalinom}")

# import logging
# logger = logging.getLogger(__name__)
# file_handler = logging.FileHandler('aritmetika.log')
# logger.addHandler(file_handler)

# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
# file_handler.setFormatter(formatter)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# logger.addHandler(stream_handler)

# def dalyba(a, b):
#     try:
#         rezultatas = a / b

#     except ZeroDivisionError:
#         logger.exception("Dalyba is nulio")
#     else:
#         return rezultatas

# a = 20
# b = 0

# padalinom = dalyba(a, b)
# logger.info(f"Dalyba: {a} / {b} = {padalinom}")

class Kate:
    def __init__(self, spalva, kojos):
        self.spalva = spalva
        self.kojos = kojos

kate1 = Kate("pilka", 4)
kate2 = Kate("juoda", 3)

print(kate1.spalva)
print(kate2.kojos)

# juoda
# 3