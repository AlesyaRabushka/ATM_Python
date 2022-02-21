class Bankomat():
    def __init__(self):
        file = open("ac.txt", "r")
        self.number = file.readline()
        self.holder = file.readline()
        self.money = file.readline()

        file.close()