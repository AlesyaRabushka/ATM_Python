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
            for i in range(0, len(s)):
                for j in range(0, len(alphabet)):
                    if s[i] == alphabet[j]:
                        print('yes')
                        flag = 0
                        out = 1
                        break
                if out == 1:
                    break
            if int(old_pin) == int(s):
                flag = 1
        return flag

    def check_pin(self, k, Card):
        old = int(Card.get_pin())
        print(old)
        next = 0
        flag = 0
        for i in range(3, 0, -1):
            new_pin = input('Введите пароль: ')
            flag = self.check_str(new_pin, old)
            print(flag)

            try:
                if int(new_pin) > 9999 or flag == 0:
                    print('Недопустимый ввод пин-код')
            except int(new_pin) > 9999:
                print('Попробуйте еще раз!')

            if old == int(new_pin):
                flag = 1
                next = 1
                break
            else:
                flag = 0
                if i - 1 == 0:
                    break
                else:
                    print('неверный пин-код. Осталось попыток: ' + str(i - 1))
        if flag == 0:
            next = 0
        return next