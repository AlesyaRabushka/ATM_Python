from card import Card


class mainscreen():
    def __init__(self):
        print(end='\n')
        print('\t ----------------------')
        print('\t\tВставьте карту')
        print('\t ----------------------')


    def check_str(self, st, old_pin):
        alphabet =  ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ч','ш','щ','ъ','ы','ь','э','я']
        flag = 0
        i = 0
        s = str(st)
        if len(s) >= 5:
            flag = 0
        else:
            out = 0
            for i in range(0, len(alphabet)):
                if s[out] == alphabet[i]:
                    flag = 1
                    break
        return flag

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