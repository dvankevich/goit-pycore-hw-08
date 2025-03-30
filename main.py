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
def show_phones(args, book):
    if len(args) != 1:
        return "You must provide a name."
    name = args[0]
    record = book.find(name)
    if  not record:
        return f"record with {name} not found"
    return '; '.join(p.value for p in record.phones)





def main():
    book = AddressBook()
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
            pass

        elif command == "phone":
            print(show_phones(args, book))

        elif command == "all":
            if len(book) == 0:
                print("No contacts")
            else:
                print(book)

        elif command == "add-birthday":
            pass

        elif command == "show-birthday":
            pass

        elif command == "birthdays":
            pass

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()