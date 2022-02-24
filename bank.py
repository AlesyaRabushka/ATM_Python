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



