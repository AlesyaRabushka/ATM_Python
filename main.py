from mainscreen import MainScreen
from card import Card
from chosen import Chosen
from menuoperations import MenuOperations
from singleton import Singleton

# объект singleton
single_t = Singleton()
# приветствие
MainScreen.show()
# выбор карточки
chosen = Chosen()
if chosen.operations():
    # загрузка инфы о выбранной карточке
    card = Card(chosen.get_chosen())

    # проверка пин-код
    # если успешно, вывод список опций
    if MainScreen.check_pin(chosen.get_chosen(), card):
        single_t.log('Вход в систему', True)
        MenuOperations.print(card, single_t)
    else:
        single_t.log('Вход в систему', False)
        print('Попробуйте ещё раз позже!')
        exit()
else:
    exit()
