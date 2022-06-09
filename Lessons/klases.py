class BaseMoney:
    def __init__(self, money: int):
        self.money = money

    def return_amount(self) -> int:
        return self.money


class MySalaray(BaseMoney):
    def __init__(self, my_mood: str, money: int):

        print('Ups, no money, because my mood is {my_mood} ')

        super().__init__(money=money)

    def am_i_rich(self) -> None:
        print(' of course NOT')

    def return_amount(self) -> None:
        return 

my_salary = MySalaray(my_mood='Tired', money=25)

# print(my_salary.am_i_rich())

# print(my_salary.return_amount())

