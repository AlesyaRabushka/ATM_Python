from bank import Bank
from chosen import Chosen


class Card(Bank, Chosen):
    def __init__(self, chosen):
        self.chosen = chosen
        find = chosen - 1
        file = open('card.txt')
        k = int(file.readline())

        for i in range(0, k):
            if i == find:
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
                ard_number = file.readline()
                data = file.readline()
                holder = file.readline()
                pin = int(file.readline())
                cvv = file.readline()
                balance = int(file.readline())
        file.close()

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