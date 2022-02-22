class MainScreen:
    """первый экран банкомата"""
    @staticmethod
    def show():
        print(end='\n')
        print('\t ----------------------')
        print('\t\tВставьте карту')
        print('\t ----------------------')

    @staticmethod
    def check_pin(k, card):
        old = int(card.get_pin())
        print(old)
        _next = 0
        flag = 0
        for i in range(3, 0, -1):
            try:
                new_pin = int(input('Введите пароль: '))
                if old == new_pin:
                    flag = 1
                    _next = 1
                    break
                else:
                    print('Неверный пин-код. Попробуйте ещё раз!')
            except:
                print('Неверный пин-код. Осталось попыток: ' + str(i - 1))

            if flag == 0:
                _next = 0
        return _next
