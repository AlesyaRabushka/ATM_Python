from bank import Bank
from chosen import Chosen


class Card(Bank, Chosen):
    """карточка"""
    def __init__(self, chosen):
        self.chosen = chosen
        user = chosen - 1
        file = open('card.txt')
        amount = int(file.readline())

        # ищем именно ту карточку, которую выбрали
        for i in range(0, amount):
            if i == user:
                self.__card_number = file.readline()
                self.__card_data = file.readline()
                self.__card_holder = file.readline()
                self.__card_pin = int(file.readline())
                self.__card_cvv = file.readline()
                self.__card_balance = int(file.readline())
            else:
                # если невыбранная карточка, просто считываем, но нигде не сохраняем эти данные
                card_number = file.readline()
                data = file.readline()
                holder = file.readline()
                pin = int(file.readline())
                cvv = file.readline()
                balance = int(file.readline())
        file.close()

    # скрытие номера карточки, кроме последних 4х цифр
    @staticmethod
    def number_hiding(card_number):
        space = 0
        for i in range(0, len(card_number)):
            if space == 3:
                print(card_number[i] + card_number[i+1] + card_number[i+2] + card_number[i+3])
                break
            else:
                if card_number[i] == ' ':
                    print(end=' ')
                    space += 1
                else:
                    print('*', end='')

    # вывод на экран данные карточки
    def print_card_info(self):
        print('\t\t-----------------')
        print('\t\t Данные карточки')
        print('\t\t-----------------')

        print('\tНомер карточки: ', end=' ')
        self.number_hiding(self.get_number())
        print('\tВладелец карточки: ', end=' ')
        print(self.get_holder(), end='')
        print('\tСрок эксплуатации: ', end=' ')
        print(self.get_data(), end='')
        print('\tДоступные средства: ', end=' ')
        print(self.get_balance(), end='\n')

    def get_number(self) -> str:
        return self.__card_number

    def set_number(self, number: str):
        self.__card_number = number

    def get_holder(self) -> str:
        return self.__card_holder

    def set_holder(self, holder: str):
        self.__card_holder = holder

    def get_data(self) -> str:
        return self.__card_data

    def set_data(self, data: str):
        self.__card_data = data

    def get_pin(self) -> int:
        return self.__card_pin

    def set_pin(self, pin: int):
        self.__card_pin = pin

    def get_cvv(self):
        return self.__card_cvv

    def set_cvv(self, cvv):
        self.__card_cvv = cvv

    def get_balance(self) -> int:
        return self.__card_balance

    def set_balance(self, balance: int):
        self.__card_balance = balance