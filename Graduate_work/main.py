from person_data import Person
from storage import Storage

storage = Storage()

while True:
    menu_input = input(
        'Press "1" and Enter if you want to save information about a person \n'
        'Press "2" and Enter if you want to search or delete information about a person: '
    ).strip(' ')

    if menu_input.upper() in '1':
        name = input(
            'Enter name (required): '
        ).strip(' ')
        surname = input(
            'Enter the surname (optional): '
        ).strip(' ')
        middle_name = input(
            'Enter the middle name (optional): '
        ).strip(' ')
        gender = input(
            'Enter the person\'s gender: "f"/"ж" or "m"/"м" (optional): '
        ).strip(' ')
        born_date = input(
            'Enter the date of birth (required) in the format DD.MM.YYYY: '
        ).strip(' ')
        death_date = input(
            'Enter the date of death if the person has already died. Format DD.MM.YYYY: '
        ).strip(' ')

        write = input('To save information, press "R" or "З": ').strip(' ')
        if write.upper() in 'R' or 'З':
            try:
                person = Person(name, born_date, gender, surname, middle_name, death_date)
                person.validate()
                storage.set_person(person)
                storage.save_to_csv_file()
            except Exception as e:
                print(e)
                continue

    if menu_input.upper() in '2':
        serch_input = input(
            'Enter a name or part of it to search: '
        ).strip(' ')
        try:
            storage.find_to_csv_file(serch_input)
            del_person = input(
                'Do you want to delete information about a person? "Y"/"Т" - Yes/Так, "N"/"Н" - No/Ні: '
            ).strip(' ')
            if del_person.upper() in ('Y', 'Т'):
                del_input = input(
                    'Enter the ID of the person whose information you want to delete: '
                ).strip(' ')
                try:
                    storage.remove_to_csv_file(del_input)
                except Exception as a:
                    print(a)
                    continue
            if del_person.upper() in ('N', 'Н'):
                continue
        except Exception as b:
            print(b)
            continue
