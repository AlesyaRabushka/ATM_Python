from cardSessions import GiveMoney
from cardSessions import ChangePin
from cardSessions import GetMoney
from cardSessions import Telephone, Currency
from cardSessions import Currency_transactions

from bankomat import Bankomat


class MenuOperations(Bankomat):
    """меню опций"""

    @staticmethod
    def print_menu(card, single_t):
        # приезжают инкассаторы и кладут денежку в банкомат
        storage = Bankomat()
        storage.set_storage_byn(10000)
        storage.set_storage_usd(1000)

        file = open('bankomat.txt', 'w')
        file.write(str(storage.get_storage_byn()))
        file.write(str(storage.get_storage_usd()))
        file.close()

        while 1 == 1:
            print("\tВыберите операцию:")
            print("\t1 - Данные банковской карты")
            print("\t2 - Выдача наличных")
            print("\t3 - Оплата телефона")
            print("\t4 - Смена пин-кода")
            print("\t5 - Добавить средства на карточку")
            print("\t6 - Обмен валют")
            print("\t7 - Перевод между счетами")
            print("\t0 - Забрать карту и закончить работу")

            try:
                k = int(input())

                # данные о карточке
                if k == 1:
                    card.print_card_info()
                    single_t.log('Данные банковской карты', True,'')

                # выдача наличных
                elif k == 2:
                    print('Выберите счет: ')
                    print('\t1 - BYN')
                    print('\t2 - USD')
                    try:
                        s = int(input())
                        if s == 1:
                            print("\tВыберите нужную сумму:")
                            print("\t1 - 5")
                            print("\t2 - 10")
                            print("\t3 - 20")
                            print("\t4 - 50")
                            print("\t5 - 100")
                            print("\t6 - Другая сумма")

                            try:
                                m = int(input())

                                if m == 6:
                                     money = input("Введите сумму выдачи: ")
                                     if money.isdigit():
                                         give_money = GiveMoney()
                                         give_money.money_out(card, int(money), storage, single_t, 'BYN')
                                     else:
                                         print('\n----------Неверный формат ввода данных-----------\n')

                                elif m == 1:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 5, storage, single_t, 'BYN')
                                elif m == 2:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 10, storage, single_t, 'BYN')
                                elif m == 3:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 20, storage, single_t, 'BYN')
                                elif m == 4:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 50, storage, single_t, 'BYN')
                                elif m == 5:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 100, storage, single_t, 'BYN')
                                else:
                                    print("\t----------Неверный код операции----------\n")

                            except ValueError:
                                print("\t----------Неверный код операции----------\n\n")
                        elif s == 2:
                            print("\tВыберите нужную сумму:")
                            print("\t1 - 5$")
                            print("\t2 - 10$")
                            print("\t3 - 20$")
                            print("\t4 - 50$")
                            print("\t5 - 100$")
                            print("\t6 - Другая сумма")
                            try:
                                f = int(input())
                                if f == 6:
                                    money = input("Введите сумму выдачи: ")
                                    if money.isdigit():
                                        give_money = GiveMoney()
                                        give_money.money_out(card, int(money), storage, single_t, 'USD')
                                    else:
                                        print('\n----------Неверный формат ввода данных-----------\n')
                                elif f == 1:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 5, storage, single_t, 'USD')
                                elif f == 2:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 10, storage, single_t, 'USD')
                                elif f == 3:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 20, storage, single_t, 'USD')
                                elif f == 4:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 50, storage, single_t, 'USD')
                                elif f == 5:
                                    give_money = GiveMoney()
                                    give_money.money_out(card, 100, storage, single_t, 'USD')
                                else:
                                    print("\t----------Неверный код операции----------\n")
                            except ValueError:
                                print("\t----------Неверный код операции----------\n\n")

                    except ValueError:
                        print("\t----------Неверный код операции----------\n\n")

                # оплата телефона
                elif k == 3:
                    print('1 - +375 44 730 81 28\n2 - +375 33 895 12 04\n3 - +375 25 234 10 23')
                    tel = int(input('Выберите номер телефона: '))
                    if tel == 1 or tel == 2 or tel == 3:
                        money = int(input("Введите сумму платежа: "))
                        telephone = Telephone()
                        telephone.telephone_pay(card, money, tel, storage, single_t)
                    else:
                        print('\t----------Неверный код операции. Повторите попытку позже.----------\n')
                        single_t.log('Пополнение счета телефона', False, 'Неверный номер операции')

                # смена пин-код
                elif k == 4:
                    ChangePin.change_card_pin(card, card.get_pin(), single_t)

                # пополнение средств
                elif k == 5:
                    print('Выберите валюту:')
                    print('1 - BYN')
                    print('2 - USD')
                    try:
                        choose_money = int(input())
                        money = input('Вставьте купюру: ')
                        if money.isdigit():
                            if choose_money == 1:
                                get_money = GetMoney()
                                get_money.money_in(card, int(money), storage, single_t, 'BYN')
                            elif choose_money == 2:
                                get_money = GetMoney()
                                get_money.money_in(card, int(money), storage, single_t, 'USD')
                        else:
                            print('\t----------Неверный формат ввода данных-----------\n')


                    except ValueError:
                        print('\n\t----------Неверный код операции----------\n\n')

                elif k == 6:
                    currency = Currency()
                    money = currency.print()
                    if money != 0:
                        currency.moneyOut(card, money)
                    else:
                        pass

                elif k == 7:
                    try:
                        print('Выберите счет на который хотите перевести: ')
                        print('1 - BUN')
                        print('2 - USD')
                        g = int(input())
                        if g == 1:
                            money=float(input('Введите сумму: '))
                            transaction=Currency_transactions()
                            transaction.fromUSDtoBUN(card,money)
                        elif g == 2:
                            money = float(input('Введите сумму: '))
                            transaction = Currency_transactions()
                            transaction.fromBUNtoUSD(card, money)
                        else:
                            print('----------Неверный код операции----------\n\n')
                    except ValueError:
                        print('\n\t----------Неверный код операции----------\n\n')
                # выход из проги
                elif k == 0:
                    single_t.log('Выход из системы', True,'')
                    exit()
                else:
                    print('----------Неверный код операции----------\n\n')

            except ValueError:
                print("\t----------Неверный код операции----------\n")
