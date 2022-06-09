# try:
#     pass
# except Exception as e:
#     print('')
# finally:
#     pass

# def do_smth(a:int) -> str:
#     try:
#        # if something bad happens a
#         pass
#     except Exception as e:
#         pass
#         # I will use logger to understand what happened

# def my_money(money: int) -> bool:
#     if type(money) != int:
#         raise ZeroDivisionError()
#     else:
#         print(f'All good, money is {money}')

# #     except Exception as e:
# #         pass

# # my_money(25)

# # from typing import Any

# # class NoMoneyError(Exception):
# #     def __str__(self) -> str:
# #         return 'We recieved wrong type of money'

# # try:
# #     2 / 0 
# # except Exception as e:
# #     print(e)

# # finally:
# #     pass

# # from typing import Any

# # class NoMoneyError(Exception):
# #     def __init__(self, *args: message):
# #         pass 



# class Car:
#     def __init__(self, color: str):
#         self.color = color

#     def 
   

#     def __car_color() -> str:
#         return "It's white car"

# my_car = Car(color="White")

# print(my_car.color)

class Jazz:
    def __init__(self, performer: str) -> str:
       self.performer = performer

    def return_performer(self) -> str:
        return self.performer

my_performer = Jazz(performer = 'Miles Davis')

print(my_performer.return_performer())