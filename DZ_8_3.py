class Car:
    def __init__(self, model, vin, number)  :
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_number(number):
            self.__number = number

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise InCorrectVinNumber('Некорректный тип vin номера')
        if (vin_number<1000000) or (vin_number>9999999):
           raise InCorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_number(self, number):
        if not isinstance(number, str):
            raise InCorrectNumber('Некорректный тип данных для номера')
        if len(number) != 6:
            raise InCorrectNumber('Неверная длина номера')
        return True

class InCorrectVinNumber(Exception):
     def __init__(self, message):
         self.message = message

class InCorrectNumber(Exception):
     def __init__(self, message):
         self.message = message

if __name__ == '__main__':
    try:
        first  = Car('Модель1', 1000000, 'f123dj')
    except InCorrectVinNumber as exc:
        print(exc.message)
    except InCorrectNumber as exc:
        print(exc.message)
    else:
        print(f'{first.model} успешно создан')

    try:
        second = Car('Модель2', 300, 'т001тр')
    except InCorrectVinNumber as exc:
        print(exc.message)
    except InCorrectNumber as exc:
        print(exc.message)
    else:
        print(f'{second.model} успешно создан')

    try:
        third = Car('Модель3', 2020202, 'нет номера')
    except InCorrectVinNumber as exc:
        print(exc.message)
    except InCorrectNumber as exc:
        print(exc.message)
    else:
        print(f'{third.model} успешно создан')

