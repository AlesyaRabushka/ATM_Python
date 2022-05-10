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
                self.__card_balance_byn = float(file.readline())
                self.__card_balance_usd = float(file.readline())

            else:
                # если невыбранная карточка, просто считываем, но нигде не сохраняем эти данные
                card_number = file.readline()
                data = file.readline()
                holder = file.readline()
                pin = int(file.readline())
                cvv = file.readline()
                balance_by = float(file.readline())
                balance_us = float(file.readline())
        file.close()


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

    def get_balance_byn(self) -> float:
        return self.__card_balance_byn

    def set_balance_byn(self, balance: int):
        self.__card_balance_byn = balance

    def get_balance_usd(self) -> float:
        return self.__card_balance_usd

    def set_balance_usd(self, balance: int):
        self.__card_balance_usd = balance

