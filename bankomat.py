class Bankomat:
    """хранилище денег"""
    storage = 0

    def __int__(self):
        file = open('bankomat.txt')
        self.storage = int(file.readline())
        file.close()

    def get_storage(self) -> int:
        return self.storage

    def set_storage(self, storage: int):
        self.storage = storage