def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input. Please provide name and phone number(the number must be numeric) separated by space."
        except IndexError:
            print('except IndexError')
            return "Invalid input. Give me name and phone please."
    return wrapper


contacts = {}


def print_hello():
    print('How can I help you?')


@input_error
def add_contact(command_line):
    name = command_line.split(" ")[1]
    phone = int(command_line.split(" ")[2])
    contacts[name] = phone
    return f"Contact {name} with phone number {phone} added."


@input_error
def change_contact(command_line):
    name = command_line.split(" ")[1]
    phone = int(command_line.split(" ")[2])
    contacts[name] = phone
    return f"Phone number for contact {name} changed to {phone}."


@input_error
def show_phone(command_line):
    name = command_line.split(" ")[1]
    return contacts[name]


def show_all_contacts():
    if not contacts:
        return "No contacts found."
    else:
        result = ""
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()


COMMANDS = {
    'hello': print_hello,
    'add': add_contact,
    'change': change_contact,
    'phone': show_phone,
    'show all': show_all_contacts
}


def main():
    print('''Hello! I'm an assistant that helps the user to add, edit and view contacts.
            I'm aware of the following commands:
            'hello' - just hello :-)
            'add'  - I will create a new contact (enter name and number(must be numeric) separated by a space)
            'change' - I will change the number (enter the name and the new number separated by a space)
                    if there is no such name, a new contact will be created
            'phone' - I will show the user's phone number (enter name )
            'show all' - I will show all saved contacts
            'good bye', 'close', 'exit' - If all the work is done, it's time to say goodbye 
        ''')
    while True:
        command_line = input().lower()
        command = command_line.split(" ")[0]

        def get_handler(command):
            if command in COMMANDS:
                return COMMANDS[command]
        handler = get_handler(command)
        if command in ['hello', 'show all']:
            print(handler())
        elif command in ['add', 'change', 'phone']:
            print(handler(command_line))
        elif command in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
