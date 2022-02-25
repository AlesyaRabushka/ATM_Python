class MyException(Exception):
    """класс для генерации исключений"""
    def __init__(self, error):
        self.error_type = error

    #возвращает строку с названием ошибки
    def __str__(self):
        return f'{self.error_type}'