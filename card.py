from bank import Bank
from chosen import Chosen


class Card(Bank, Chosen):
    """карточка"""
    def __init__(self, chosen):
        self.chosen = chosen
        super().__init__(chosen)#метод супер класса(считываем)

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
        print('\tДоступные средства (BYN): ', end=' ')
        print(self.get_balance_byn(), end='\n')
        print('\tДоступные средства (USD): ', end=' ')
        print(self.get_balance_usd(), end='\n\n')

    # копирование данных о карточке
    def copy_data(self):
        card = open("card.txt", "r")
        new_card = open("newcard.txt", "w")

        amount = int(card.readline())
        new_card.write(str(amount) + '\n')
        for i in range(0, amount):
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
        card.close()
        new_card.close()

