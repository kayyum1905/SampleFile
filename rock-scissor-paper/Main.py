objects = ('Rock', 'Paper', 'Scissor')


def list_objects():
    print('Choose your object by typing the first letter of your choice: ')
    print(objects)


def ask_user_input():
    user_input = input('Type here please: ')
    process_user_choice(str(user_input))


def process_user_choice(user_input):
    user_input = user_input.lower()
    user_object = ''
    if user_input == 'r':
        user_object = objects[0]
    elif user_input == 'p':
        user_object = objects[1]
    elif user_input == 's':
        user_object = objects[2]
    return user_object


list_objects()
ask_user_input()
