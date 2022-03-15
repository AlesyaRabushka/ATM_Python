class pinValueException(Exception):
    """класс для генерации исключений"""
    def __init__(self, error):
        self.error_pin = error
    #возвращает строку с названием ошибки
    def __str__(self):
        return f'{self.error_pin} пин-код должен содержать только цифры'

class MyException(Exception):
    def __init__(self, pin):
        self.error = pin
        # возвращает строку с названием ошибки
    def __str__(self):
        return f'{self.error} пин-код должен содержать 4 символа'