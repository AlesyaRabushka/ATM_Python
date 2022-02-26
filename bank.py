class Bank:

    def __init__(self, chosen):
        user = chosen - 1
        file = open('card.txt')
        amount = int(file.readline())

        # ищем именно ту карточку, которую выбрали
        for i in range(0, amount):
            if i == user:
                self.__card_number = file.readline()
                self.__card_data = file.readline()
                self.__card_holder = file.readline()
                self.__card_pin = int(file.readline())
                self.__card_cvv = file.readline()
                self.__card_balance = int(file.readline())
            else:
                # если невыбранная карточка, просто считываем, но нигде не сохраняем эти данные
                card_number = file.readline()
                data = file.readline()
                holder = file.readline()
                pin = int(file.readline())
                cvv = file.readline()
                balance = int(file.readline())
        file.close()

    # копирование данных о карточке
    def copy_data(self):
        card = open("card.txt", "r")
        new_card = open("newcard.txt", "w")

        k = int(card.readline())
        new_card.write(str(k) + '\n')
        for i in range(0, k):
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
            new_card.write(str(card.readline()))
        card.close()
        new_card.close()

    def get_number(self) -> str:
        return self.__card_number

    def set_number(self, number: str):
        self.__card_number = number

    def get_holder(self) -> str:
        return self.__card_holder

    def set_holder(self, holder: str):
        self.__card_holder = holder

    def get_data(self) -> str:
        return self.__card_data

    def set_data(self, data: str):
        self.__card_data = data

    def get_pin(self) -> int:
        return self.__card_pin

    def set_pin(self, pin: int):
        self.__card_pin = pin

    def get_cvv(self):
        return self.__card_cvv

    def set_cvv(self, cvv):
        self.__card_cvv = cvv

    def get_balance(self) -> int:
        return self.__card_balance

    def set_balance(self, balance: int):
        self.__card_balance = balance

