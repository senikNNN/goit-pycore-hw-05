
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid number of arguments entered!"
    return inner

def dict_error(func): 
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
@dict_error
def change_contact(args, contacts): 
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return "Contact changed."
    else:
        raise KeyError

@input_error
@dict_error
def show_phone(args, contacts):
    name = args[0]
    if contacts[name]:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError

def show_all(contacts):
    if contacts:
        for contact in contacts:
            print("\t" + contact + ":", contacts[contact])
    else:
        print("Empty...")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()