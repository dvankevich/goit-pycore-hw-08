from classes import Field, Name, Phone, Record, AddressBook
from print_help import print_help

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Argument expected. Use help command for help."
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def show_phones(args, book: AddressBook):
    if len(args) != 1:
        return "You must provide a name."
    name = args[0]
    record = book.find(name)
    if  not record:
        return f"record with {name} not found"
    return '; '.join(p.value for p in record.phones)

@input_error
def change_phone(args, book: AddressBook):
    if len(args) != 3:
        return "Incorrect number of arguments. Use change [ім'я] [старий телефон] [новий телефон]"
    name, phone, new_phone, *_ = args
    record = book.find(name)
    if not record:
        return f"record with {name} not found"
    record.change_phone(phone, new_phone)
    return f"for {name} number {phone} changed to {new_phone}"

@input_error
def add_birthday(args, book: AddressBook):
    name, birhday, *_ = args
    record = book.find(name)
    #print(record)
    if not record:
       return f"record with {name} not found"
    try:
        record.add_birthday(birhday)
    except ValueError:
        return "Incorrect data format"
    return f"for {name} birthday {birhday} added"

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    if not record:
       return f"record with {name} not found"
    birthday = str(record.birthday)
    return f"contact {name} was born {birthday}"


def debug_add_data(book: AddressBook):
    r01 = Record("Name01")
    r01.add_phone("1234567890")
    r01.add_phone("1234567891")
    r01.add_birthday("29.01.1999")
    book.add_record(r01)

    r02 = Record("Name02")
    r02.add_phone("2234567890")
    r02.add_birthday("02.04.2001")
    book.add_record(r02)

    r03 = Record("Name03")
    r03.add_phone("3234567890")
    r03.add_birthday("04.04.2001")
    book.add_record(r03)

    r04 = Record("Name04")
    r04.add_phone("4234567890")
    r04.add_birthday("04.08.2008")
    book.add_record(r04)


def not_implemented(args, command):
    return f"{command} with {args} not implemented"

def main():
    DEBUG = True 

    book = AddressBook()

    if DEBUG:
        debug_add_data(book) # generate test data

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "help":
            print(print_help())

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_phone(args, book))

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all":
            if len(book) == 0:
                print("No contacts")
            else:
                print(book)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(book.birthdays())

        elif command == "save":
            print(not_implemented(args, command))

            show_birthday

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()