class MainScreen:
    """первый экран банкомата"""
    @staticmethod
    def show_welcom_screen():
        print(end='\n')
        print('\t ----------------------')
        print('\t\tВставьте карту')
        print('\t ----------------------')

    # проверка пин-код
    @staticmethod
    def check_pin(k, card):
        old = int(card.get_pin())
        print(old)
        _next = 0
        flag = 0
        for i in range(3, 0, -1):
            try:
                new_pin = int(input('Введите пин-код: '))
                if old == new_pin:
                    flag = 1
                    _next = 1
                    break
                else:
                    print('\tНеверный пин-код. Осталось попыток: ' + str(i - 1))
            except:
                print('\tНеверный пин-код. Осталось попыток: ' + str(i - 1))

            if flag == 0:
                _next = 0
        return _next
