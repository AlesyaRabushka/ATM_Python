class Bankomat:
    """хранилище денег"""
    storage = 0

    def __int__(self):
        file = open('bankomat.txt')
        self.storage_byn = int(file.readline())
        self.storage_usd = int(file.readline())
        file.close()

    def get_storage_byn(self) -> int:
        return self.storage_byn

    def set_storage_byn(self, storage: int):
        self.storage_byn = storage

    def get_storage_usd(self) -> int:
        return self.storage_usd

    def set_storage_usd(self, storage: int):
        self.storage_usd = storage