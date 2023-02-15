from datetime import date
from datetime import datetime


class Person:
    def __init__(
            self,
            name,
            born_date,
            gender=None,
            surname=None,
            middle_name=None,
            death_date=None
    ):
        self.name = name
        self.born_date = born_date
        self.gender = gender
        self.surname = surname
        self.middle_name = middle_name
        self.death_date = death_date

    @staticmethod
    def age_calculate(born_date, death_date=0):
        born_day = int(born_date[:2])
        born_month = int(born_date[3:5])
        born_year = int(born_date[6:10])

        if death_date:
            death_day = int(death_date[:2])
            death_month = int(death_date[3:5])
            death_year = int(death_date[6:10])

            age = death_year - born_year
            if death_month < born_month:
                age -= 1
            elif death_month == born_month and death_day < born_day:
                age -= 1
            return age

        else:
            today = date.today()
            age = today.year - born_year
            if today.month < born_month:
                age -= 1
            elif today.month == born_month and today.day < born_day:
                age -= 1
            return age

    def validate(self):
        if len(self.name) < 2 or len(self.born_date) < 10:
            raise Exception('Date or name too short or required line not filled \n')

        if not self.name.isalpha():
            raise Exception('Use only letters to enter the name \n')

        if len(self.gender) > 0 and not self.gender.isalpha():
            raise Exception('Use only letters to enter the gender \n')

        if len(self.surname) > 0 and not self.surname.isalpha():
            raise Exception('Use only letters to enter the surname\n')

        if len(self.middle_name) > 0 and not self.middle_name.isalpha():
            raise Exception('Use only letters to enter the middle name \n')

        if datetime.strptime(self.born_date, '%d.%m.%Y') > datetime.today():
            raise Exception('Entered a date of birth that has not yet arrived \n')

        if len(self.death_date) > 0:
            if datetime.strptime(self.death_date, '%d.%m.%Y') > datetime.today():
                raise Exception('Entered a date of death that has not yet arrived \n')

            if datetime.strptime(self.death_date, '%d.%m.%Y') < datetime.strptime(self.born_date, '%d.%m.%Y'):
                raise Exception('The date of death cannot be earlier than the date of birth \n')
