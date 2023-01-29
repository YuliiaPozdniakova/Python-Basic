# Прочитать сохранённый csv-файл из задания №19 и сохранить данные в excel-файл,
# кроме возраста – столбец с этими данными не нужен.
#
# К заданию прикреплён пример как должно выглядеть содержания итогового файла.
import csv
from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet(title="Data")
dest_filename = 'data_xlsx.xlsx'
age_index = False

with open('data_csv.csv', encoding='utf-8') as read_file:
    file_reader = csv.reader(read_file)
    for parent_idx, items in enumerate(file_reader):
        if len(items) != 0:
            if 'Age' in items:
                age_index = items.index('Age')
            if age_index:
                del items[age_index]
            for idx, item in enumerate(items):
                ws.cell(row=idx + 1, column=parent_idx + 1, value=item)
wb.save(filename=dest_filename)
