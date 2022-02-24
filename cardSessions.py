# операции с карто
import os

from bank import Bank


class GiveMoney(Bank):
    """выдача наличных"""
    def money_out(self, card, money: int, single_t):
        card.copy_data()
        storage = self.get_storage()

        if money > storage:
            print('\tЛимит средств привышен!\n')
            single_t.log('Выдача наличных', False)
        else:
            if money > int(card.get_balance()) or money < 0:
                print('\tНедостаточно средств\n')
                single_t.log('Выдача наличных', False)
            else:
                self.set_storage(storage - money)
                f_storage = open('bank.txt', 'w')
                f_storage.write(str(self.get_storage()))
                f_storage.close()

                new_money = int(card.get_balance()) - money
                l = int(card.get_chosen()) - 1
                from_card = open('newcard.txt')
                to_card = open('card.txt', 'w')

                single_t.log('Выдача наличных', True)
                k1 = from_card.readline()
                to_card.write(k1)
                for i in range(0, int(k1)):
                    if i == l:
                        from_card.readline()
                        from_card.readline()
                        from_card.readline()
                        from_card.readline()
                        from_card.readline()
                        from_card.readline()

                        to_card.write(card.get_number())
                        to_card.write(card.get_data())
                        to_card.write(card.get_holder())
                        to_card.write(str(card.get_pin()) + '\n')
                        to_card.write(card.get_cvv())
                        card.set_balance(new_money)
                        to_card.write(str(card.get_balance()) + '\n')
                    else:
                        to_card.write(from_card.readline())
                        to_card.write(from_card.readline())
                        to_card.write(from_card.readline())
                        to_card.write(from_card.readline())
                        to_card.write(from_card.readline())
                        to_card.write(from_card.readline())

                from_card.close()
                to_card.close()


class ChangePin:
    """смена пин-код"""
    @staticmethod
    def change_card_pin(card, pin: int, single_t):
        flag = 0
        for i in range(3, 0, -1):
            try:
                old_pin = int(input('Введите старый пин-код: '))

                if pin == old_pin:
                    flag = 1
                    card.copy_data()
                    try:
                        new_pin = int(input('Введите новый пин-код: '))
                        if len(str(new_pin)) > 4:
                            single_t.log('Cмена пин-код', False)
                        card.set_pin(new_pin)
                        single_t.log('Cмена пин-код', True)
                    except:
                        single_t.log('Cмена пин-код', False)

                    from_card = open('newcard.txt')
                    to_card = open('card.txt', 'w')
                    l = int(card.get_chosen()) - 1

                    k = from_card.readline()
                    to_card.write(str(k))
                    for i in range(0, int(k)):
                        if i == l:
                            from_card.readline()
                            from_card.readline()
                            from_card.readline()
                            from_card.readline()
                            from_card.readline()
                            from_card.readline()

                            to_card.write(card.get_number())
                            to_card.write(card.get_data())
                            to_card.write(card.get_holder())
                            to_card.write(str(card.get_pin()) + '\n')
                            to_card.write(card.get_cvv())
                            to_card.write(str(card.get_balance()) + '\n')
                        else:
                            to_card.write(from_card.readline())
                            to_card.write(from_card.readline())
                            to_card.write(from_card.readline())
                            to_card.write(from_card.readline())
                            to_card.write(from_card.readline())
                            to_card.write(from_card.readline())
                    from_card.close()
                    to_card.close()
                    os.remove('newcard.txt')
                    break
                else:
                    if i - 1 == 0:
                        flag = 0
                        break
                    else:
                        flag = 0
                        print('Попробуйте еще раз!')
                        single_t.log('Смена пин-код', False)
            except:
                print('Попробуйте еще раз!')
                single_t.log('Смена пин-код', False)


class GetMoney(Bank):
    """пополнение денежных средств"""
    def money_in(self, card, single_t):
        money = int(input('Вставьте купюру: '))
        new_money = int(card.get_balance()) + money
        find = int(card.get_chosen()) - 1
        single_t.log('Пополнение счета', True)

        # пополнение средств хранилища
        storage = self.get_storage()
        self.set_storage(storage + money)
        file = open('bank.txt', 'w')
        file.write(str(self.get_storage()))
        file.close()

        # изменение данных о средствах пользователя
        from_card = open('newcard.txt')
        to_card = open('card.txt', 'w')
        k = from_card.readline()
        to_card.write(k)
        for i in range(0, int(k)):
            if i == find:
                from_card.readline()
                from_card.readline()
                from_card.readline()
                from_card.readline()
                from_card.readline()
                from_card.readline()

                to_card.write(card.get_number())
                to_card.write(card.get_data())
                to_card.write(card.get_holder())
                to_card.write(str(card.get_pin()) + '\n')
                to_card.write(card.get_cvv())
                card.set_balance(new_money)
                to_card.write(str(new_money) + '\n')
            else:
                to_card.write(str(from_card.readline()))
                to_card.write(str(from_card.readline()))
                to_card.write(str(from_card.readline()))
                to_card.write(str(from_card.readline()))
                to_card.write(str(from_card.readline()))
                to_card.write(str(from_card.readline()))
        from_card.close()
        to_card.close()


class Currency:
    """валютные операции"""
    def print(self):
        print('КУРС ВАЛЮТ')
        print('\t1 - 174.00 (казахстанский тенге) - \t* минимальная доступная сумма: 1740 тенге')
        print('\t2 - 7.00 (замбийская квача) - \t* минимальная доступная сумма: 70 квач')
        print('\t3 - 35.00 (киргизская сома) - \t*минимальная доступная сумма: 350 сом')
        print('\t4 - 11.00 (украинская гривна) - \t*минимальная доступная сумма: 110 гривен')
        print('\t5 - 777.00 (мьянманский кьят) - \t*минимальная доступная сумма: 7770 кьят')

        a = int(input('Выберите валюту: '))
        value = int(input('Введите сумму: '))

        if a == 1:
            if value < 1740:
                print('Минимально допустимая сумма: 1740 тенге. Попробуйте еще раз!')
                value = 0
            else:
                value = value / 174
        elif a == 2:
            if value < 70:
                print('Минимально допустимая сумма: 70 квач. Попробуйте еще раз!')
                value = 0
            else:
                value = value / 7
        elif a == 3:
            if value < 350:
                print('Минимально допустимая сумма: 350 сом. Попробуйте еще раз!')
                value = 0
            else:
                value = value / 35
        elif a == 4:
            if value < 110:
                print('Минимально допустимая сумма: 110 гривен. Попробуйте еще раз!')
                value = 0
            else:
                value = value / 11
        elif a == 5:
            if value < 7770:
                print('Минимально допустимая сумма: 7770 кьят. Попробуйте еще раз!')
                value = 0
            else:
                value = value / 777
        else:
            print('Неверный номер операции! Попробуйте еще раз!')

        return value

    def moneyOut(self, card, money):
        card.copy_data()

        if int(money) > int(card.get_balance()) or money < 0:
            print('no')
        else:
            new_money = int(card.get_balance()) - money
            card.set_balance(new_money)
            l = card.get_chosen() - 1

            from_card = open('newcard.txt', 'r')
            to_card = open('card.txt', 'w')
            k = from_card.readline()
            to_card.write(k)

            for i in range(0, int(k)):
                if i == l:
                    from_card.readline()
                    from_card.readline()
                    from_card.readline()
                    from_card.readline()
                    from_card.readline()
                    from_card.readline()

                    to_card.write(card.get_number())
                    to_card.write(card.get_data())
                    to_card.write(card.get_holder())
                    to_card.write(card.get_pin())
                    to_card.write(card.get_cvv())
                    to_card.write(str(card.get_balance()) + '\n')
                else:
                    to_card.write(from_card.readline())
                    to_card.write(from_card.readline())
                    to_card.write(from_card.readline())
                    to_card.write(from_card.readline())
                    to_card.write(from_card.readline())
                    to_card.write(from_card.readline())
            from_card.close()
            to_card.close()


class Telephone(GiveMoney):
    """оплата телефона"""

    def pay(self, card, money: int, tel_number: int, single_t):
        self.money_out(card, money, single_t)
        Telephone.copy_data()

        from_card = open('newtelephone.txt', 'r')
        to_card = open('telephone.txt', 'w')
        k = from_card.readline()
        to_card.write(k)
        single_t.log('Пополнение счета телефона', True)

        for i in range(0, int(k)):
            if i == tel_number - 1:
                number = from_card.readline()
                balance = int(from_card.readline())

                to_card.write(number)
                to_card.write(str(balance + money) + '\n')
            else:
                to_card.write(from_card.readline())
                to_card.write(from_card.readline())
        from_card.close()
        to_card.close()

    @staticmethod
    def copy_data():
        card = open("telephone.txt", "r")
        new_card = open("newtelephone.txt", "w")

        k = int(card.readline())
        new_card.write(str(k) + '\n')
        for i in range(0, k):
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
        card.close()
        new_card.close()
