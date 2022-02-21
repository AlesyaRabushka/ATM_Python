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
            #flag = self.check_str(new_pin, old)
            try:

                new_pin = int(input('Введите пароль: '))
                if old == new_pin:
                    flag = 1
                    next = 1
                    break
                #if int(new_pin) > 9999 or flag == 0:
                 #   print('Недопустимый ввод пин-код')
            except :
                print('Попробуйте еще раз!')
                print('неверный пин-код. Осталось попыток: ' + str(i - 1))

            if flag == 0:
                next = 0
        return next