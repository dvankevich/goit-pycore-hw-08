from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        # check is value not empty
        if len(value) == 0:
            raise ValueError("Name is not be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        # Pnone number validation
        # ToDo зробити валідацію за допомогою регулярного виразу.
        if (len(value) != 10) or (not value.isdigit()):
             raise ValueError("Incorrect phone number format")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        self.phones.append(Phone(number))

    def del_phone(self, number):
        self.phones = [phone for phone in self.phones if phone.value != number]

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                 return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        record = self.data.get(name)
        #print("find record result", record)
        return record
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(name, "not found")


# Тестові функції
def test_phone_number_validation():
    # Тестування коректних номерів телефону
    try:
        phone1 = Phone("1234567890")  # коректний номер
        assert phone1.value == "1234567890"  # перевірка, чи правильно зберігся номер

        phone2 = Phone("9876543210")  # коректний номер
        assert phone2.value == "9876543210"

    except ValueError as e:
        assert False, f"Unexpected ValueError: {e}"

    # Тестування некоректних номерів телефону
    try:
        phone3 = Phone("123")  # некоректний номер
        assert False, "Expected ValueError for short phone number"
    except ValueError:
        pass  # Очікувана помилка, тест проходить

    try:
        phone4 = Phone("12345678901")  # некоректний номер
        assert False, "Expected ValueError for long phone number"
    except ValueError:
        pass  # Очікувана помилка, тест проходить

    try:
        phone5 = Phone("12345abcde")  # некоректний номер
        assert False, "Expected ValueError for non-digit characters"
    except ValueError:
        pass  # Очікувана помилка, тест проходить

if __name__ == "__main__":
    # ToDo спробувати unittest або pytest для тестування
    print("TEST phone number validation")
    test_phone_number_validation()
    print("TEST phone number validation PASS")

    record01 = Record("Name01")
    #print(record01.name, len(record01.phones))
    assert str(record01.name) == "Name01"

    record01.add_phone("1234567890")
    record01.add_phone("1234567891")
    #print(record01, len(record01.phones))
    assert len(record01.phones) == 2

    record01.del_phone("1234567891")
    assert len(record01.phones) == 1

    record01.add_phone("1234567891")
    record01.add_phone("1234567891")
    assert len(record01.phones) == 3

    record01.del_phone("1234567891")
    assert len(record01.phones) == 1

    # number not found
    assert record01.find_phone("1234567891") == None
    # number found
    assert record01.find_phone("1234567890") != None
    assert record01.find_phone("1234567890").value == "1234567890"

    #print(record01, len(record01.phones))

    book = AddressBook()
    assert len(book.data.items()) == 0
    #print(len(book.data.items()))
    book.add_record(record01)
    #print(len(book.data.items()))
    assert len(book.data.items()) == 1

    name01 = book.find("Name01")
    assert str(name01.name) == "Name01"
    #print(name01)
    name02 = book.find("Name02")
    assert name02 == None
    #print(name02)

    book.delete("Name02")
    assert len(book.data.items()) == 1
    book.delete("Name01")
    assert len(book.data.items()) == 0