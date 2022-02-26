from cardSessions import GiveMoney
from cardSessions import ChangePin
from cardSessions import GetMoney
from cardSessions import Telephone
from bankomat import Bankomat


class MenuOperations(Bankomat):
    """меню опций"""

    @staticmethod
    def print_menu(card, single_t):
        # приезжают инкассаторы и кладут денежку в банкомат
        storage = Bankomat()
        storage.set_storage(10000)
        file = open('bankomat.txt', 'w')
        file.write(str(storage.get_storage()))
        file.close()

        while 1 == 1:
            print("\tВыберите операцию:")
            print("\t1 - Данные банковской карты")
            print("\t2 - Выдача наличных")
            print("\t3 - Оплата телефона")
            print("\t4 - Смена пин-кода")
            print("\t5 - Добавить средства на карточку")
            print("\t0 - Забрать карту и закончить работу")
            k = int(input())

            # данные о карточке
            if k == 1:
                card.print_card_info()
                single_t.log('Данные банковской карты', True)

            # выдача наличных
            elif k == 2:
                money = int(input("Введите сумму выдачи: "))
                give_money = GiveMoney()
                give_money.money_out(card, money, storage, single_t)

            # оплата телефона
            elif k == 3:
                print('1 - +375 44 730 81 28\n2 - +375 33 895 12 04\n3 - +375 25 234 10 23')
                tel = int(input('Выберите номер телефона: '))
                if tel == 1 or tel == 2 or tel == 3:
                    money = int(input("Введите сумму платежа: "))
                    telephone = Telephone()
                    telephone.telephone_pay(card, money, tel, storage, single_t)
                else:
                    print('\tНеверный номер операции. Повторите попытку позже.\n')
                    single_t.log('Пополнение счета телефона', False)

            # смена пин-код
            elif k == 4:
                ChangePin.change_card_pin(card, card.get_pin(), single_t)

            # пополнение средств
            elif k == 5:
                money = int(input('Вставьте купюру: '))
                get_money = GetMoney()
                get_money.money_in(card, money, storage, single_t)

            # выход из проги
            elif k == 0:
                single_t.log('Выход из системы', True)
                exit()
            else:
                print('Неверный номер операции')
