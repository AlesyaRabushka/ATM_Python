from cardSessions import giveMoney
from cardSessions import changePin
from cardSessions import getMoney
from cardSessions import Telephone


class MenuOperations:
    """меню опций"""

    @staticmethod
    def print(card, single_t):
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
                card.print()
                single_t.log('Данные банковской карты', True)

            # выдача наличных
            elif k == 2:
                gvm = giveMoney()
                money = int(input("Введите сумму выдачи: "))
                gvm.money_out(card, money)

            # валютные операции
            elif k == 3:
                t = Telephone()
                print('1 - +375 44 730 81 28\n2 - +375 33 895 12 04\n3 - +375 25 234 10 23')
                tel = int(input('Выберите номер телефона: '))
                if tel == 1 or tel == 2 or tel == 3:
                    money = int(input("Введите сумму платежа: "))
                    t.pay(card, money, tel)
                else:
                    print('\tНеверный номер операции. Повторите попытку позже.\n')
                    single_t.log('Пополнение счета телефона', False)
                """cur = Currency()
                money = cur.print()
                print('Money = ', end = ' ')
                print(money)
                cur.moneyOut(Card, money)"""

            # смена пин-код
            elif k == 4:
                chp = changePin()
                chp.changeCardPin(card,card.get_pin())

            # пополнение средств
            elif k == 5:
                gtm = getMoney()
                gtm.moneyIn(card)

            # выход из проги
            elif k == 0:
                single_t.log('Завершение работы', True)
                exit()
            else:
                print('Неверный номер операции')
