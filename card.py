from bank import Bank
from chosen import Chosen
from singleton import Singleton


class Card(Bank, Chosen):
    def __init__(self, ch):
        super().__init__(ch)
        self.chosen = ch

    def secret(self, s):
        space = 0
        for i in range(0, len(s)):
            if space == 3:
                print(s[i] + s[i+1] + s[i+2] + s[i+3])
                break
            else:
                if s[i] == ' ':
                    print(end = ' ')
                    space += 1
                else:
                    print('*', end='')

    # вывод на экран данные карточки
    def print(self):
        print('\t\t-----------------')
        print('\t\t Данные карточки')
        print('\t\t-----------------')

        print('\tНомер карточки: ', end = ' ')
        self.secret(self.get_number())
        print('\tВладелец карточки: ', end = ' ')
        print(self.get_holder(), end = '')
        print('\tСрок эксплуатации: ', end=' ')
        print(self.get_data(), end ='')
        print('\tДоступные средства: ', end=' ')
        print(self.get_balance())