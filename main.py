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
    name, phone, new_phone = args
    record = book.find(name)
    if not record:
        return f"record with {name} not found"
    record.change_phone(phone, new_phone)
    return f"for {name} number {phone} changed to {new_phone}"


def debug_add_data(book: AddressBook):
    r01 = Record("Name01")
    r01.add_phone("1234567890")
    r01.add_phone("1234567891")
    book.add_record(r01)

    r02 = Record("Name02")
    r02.add_phone("2234567890")
    book.add_record(r02)


def not_implemented(args, command):
    return f"{command} with {args} not implemented"

def main():
    DEBUG = True

    book = AddressBook()

    if DEBUG:
        debug_add_data(book)

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
            print(not_implemented(args, command))

        elif command == "show-birthday":
            print(not_implemented(args, command))

        elif command == "birthdays":
            print(not_implemented(args, command))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()