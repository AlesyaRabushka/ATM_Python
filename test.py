from unittest import TestCase, main
from card import Card
from mainscreen import MainScreen


class CardTest(TestCase):
    # проверка имени пользователя выбранной банковской карточки
    def test_holder_name(self):
        card = Card(1)
        self.assertEqual(card.get_holder(), 'ALESIA RABUSHKA\n')

    # проверка пин-код
    def test_pin(self):
        card = Card(2)
        self.assertEqual(card.get_pin(), 2248)

if __name__ == '__main__':
    main()
