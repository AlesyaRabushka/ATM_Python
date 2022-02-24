class Bank:
    """хранилище денег"""
    def __init__(self):
        file = open('bank.txt')
        self.storage = int(file.readline())
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

    def get_storage(self) -> int:
        return self.storage

    def set_storage(self, storage: int):
        self.storage = storage

    def get_number(self) -> str:
        return self.card_number

    def set_number(self, number: str):
        self.card_number = number

    def get_holder(self) -> str:
        return self.card_holder

    def set_holder(self, holder: str):
        self.card_holder = holder

    def get_data(self) -> str:
        return self.card_data

    def set_data(self, data: str):
        self.card_data = data

    def get_pin(self) -> int:
        return self.card_pin

    def set_pin(self, pin: int):
        self.card_pin = pin

    def get_cvv(self):
        return self.card_cvv

    def set_cvv(self, cvv):
        self.card_cvv = cvv

    def get_balance(self) -> int:
        return self.card_balance

    def set_balance(self, balance: int):
        self.card_balance = balance

