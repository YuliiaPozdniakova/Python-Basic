from person_data import Person
import csv
import uuid
import os


class Storage:
    def __init__(self):
        self.is_remove = None
        self.person = None
        self.search_input = None
        self.del_input = None

    @staticmethod
    def has_headers():
        if os.stat('data_csv.csv').st_size == 0:
            return True
        return False

    def set_person(self, person: Person):
        self.person = person

    def save_to_csv_file(self):
        person_id = uuid.uuid4()
        name_of_fields = [
            'ID',
            'Name',
            'Surname',
            'Middle_name',
            'Gender',
            'Born_date',
            'Death_date'
        ]
        person_list = [
            person_id,
            self.person.name,
            self.person.surname,
            self.person.middle_name,
            self.person.gender,
            self.person.born_date,
            self.person.death_date
        ]

        with open('data_csv.csv', mode='a', encoding='utf-8', newline='') as write_file:
            file_writer = csv.writer(write_file)
            if self.has_headers():
                file_writer.writerow(name_of_fields)
            file_writer.writerow(person_list)
            print('Information successfully saved to file! \n')

    def find_to_csv_file(self, serch_input):
        self.search_input = serch_input
        find_list = []
        with open('data_csv.csv', mode='r', encoding='utf-8', newline='') as data:
            lines = data.readlines()
            for row in lines:
                r = row[37:].upper()
                if serch_input.upper().strip() in r:
                    find_list.append(row)

            if len(find_list) == 0:
                raise Exception('No information about the person was found \n')

            for item in find_list:
                if item.endswith(',\r\n'):
                    item_1 = item.strip(',\r\n')
                    item_2 = item_1.split(',')
                    born_date = item_2[-1]
                    death_date = 0
                else:
                    item_1 = item
                    item_2 = item_1.split(',')
                    death_date = item_2[-1]
                    born_date = item_2[-2]

                print(f'{item_1}, age: {Person.age_calculate(born_date, death_date)}')

    def remove_to_csv_file(self, del_input):
        self.del_input = del_input
        origin_file = 'data_csv.csv'
        tempfile = 'temp.csv'
        self.is_remove = False

        with open(origin_file, mode='r', encoding='utf-8') as csvfile, \
                open(tempfile, mode='w', encoding='utf-8', newline='') as temp:
            csvreader = csv.reader(csvfile)
            csvwriter = csv.writer(temp)
            for row in csvreader:
                if del_input != ''.join(row)[:36]:
                    csvwriter.writerow(row)
                else:
                    self.is_remove = True

        os.remove(origin_file)
        os.rename(tempfile, origin_file)

        if not self.is_remove:
            raise Exception('The person ID was entered incorrectly \n')
        print('Removal successful \n')
