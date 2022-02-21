from singleton import Singleton


class Chosen():
    def __init__(self):
        self.chosen = 0

    def set_chosen(self, number: int):
        self.chosen = number

    def get_chosen(self) -> int:
        return self.chosen

    def operations(self):
        # print('Выберите карточку:')
        print('\t1 - ALESIA RABUSHKA')
        print('\t2 - ALEKSEY SMELOV')
        print('\t3 - ALENA SKLEMA')
        n = int(input())
        if n == 1:
            self.set_chosen(1)
           # self.log('Вход в систему', True)
        elif n == 2:
            self.set_chosen(2)
           # self.log('Вход в систему', True)
        elif n == 3:
            self.set_chosen(3)
          #  self.log('Вход в систему', True)
        else:
            print('Неверный код операции')
           # self.log('Вход в систему', False)