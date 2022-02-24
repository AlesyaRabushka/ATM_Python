from bank import Bank
from chosen import Chosen


class Card(Bank, Chosen):
    """карточка"""
    def __init__(self, chosen):
        self.chosen = chosen
        user = chosen - 1
        file = open('card.txt')
        k = int(file.readline())

        # ищем именно ту карточку, которую выбрали
        for i in range(0, k):
            if i == user:
                card_number = file.readline()
                self.set_number(card_number)
                data = file.readline()
                self.set_data(data)
                holder = file.readline()
                self.set_holder(holder)
                pin = int(file.readline())
                self.set_pin(pin)
                cvv = file.readline()
                self.set_cvv(cvv)
                balance = int(file.readline())
                self.set_balance(balance)
            else:
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
    def print(self):
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