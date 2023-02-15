from person_data import Person
from storage import Storage

storage = Storage()

while True:
    menu_input = input(
        'If you want to save information about a person, press "S" and Enter \n'
        'If you want to search or delete information about a person, press "D" and Enter: '
    ).replace(' ', '')

    if menu_input.upper() in 'S':
        name = input(
            'Enter name (required): '
        ).replace(' ', '')
        surname = input(
            'Enter the surname (optional): '
        ).replace(' ', '')
        middle_name = input(
            'Enter the middle name (optional): '
        ).replace(' ', '')
        gender = input(
            'Enter the person\'s gender: "f" or "m" (optional): '
        ).replace(' ', '')
        born_date = input(
            'Enter the date of birth (required) in the format DD.MM.YYYY: '
        ).replace(' ', '')
        death_date = input(
            'Enter the date of death if the person has already died. Format DD.MM.YYYY: '
        ).replace(' ', '')

        write = input('To save information, press "R": ').replace(' ', '')
        if write.upper() in 'R':
            try:
                person = Person(name, born_date, gender, surname, middle_name, death_date)
                person.validate()
                storage.set_person(person)
                storage.save_to_csv_file()
            except Exception as e:
                print(e)
                continue

    if menu_input.upper() in 'D':
        serch_input = input(
            'Enter a name or part of it to search: '
        ).replace(' ', '')
        try:
            storage.find_to_csv_file(serch_input)
            del_person = input(
                'Do you want to delete information about a person? "Y" - Yes, "N" - No: '
            ).replace(' ', '')
            if del_person.upper() in 'Y':
                del_input = input(
                    'Enter the ID of the person whose information you want to delete: '
                ).replace(' ', '')
                try:
                    storage.remove_to_csv_file(del_input)
                except Exception as a:
                    print(a)
                    continue
            if del_person.upper() in 'N':
                continue
        except Exception as b:
            print(b)
            continue
