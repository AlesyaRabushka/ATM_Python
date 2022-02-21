from card import Card


class MainScreen:
    def __init__(self):
        print(end='\n')
        print('\t ----------------------')
        print('\t\tВставьте карту')
        print('\t ----------------------')

    def check_pin(self, k, Card):
        old = int(Card.get_pin())
        print(old)
        next = 0
        flag = 0
        for i in range(3, 0, -1):
            try:
                new_pin = int(input('Введите пароль: '))
                if old == new_pin:
                    flag = 1
                    next = 1
                    break
                else:
                    print('Неверный пин-код. Попробуйте ещё раз!')
            except :
                print('Неверный пин-код. Осталось попыток: ' + str(i - 1))

            if flag == 0:
                next = 0
        return next