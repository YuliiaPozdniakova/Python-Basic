# Прочитать сохранённый csv-файл из задания №19 и сохранить данные в excel-файл,
# кроме возраста – столбец с этими данными не нужен.
#
# К заданию прикреплён пример как должно выглядеть содержания итогового файла.
import csv
import openpyxl
# from openpyxl import Workbook
from openpyxl.utils import get_column_letter


with open('data_csv.csv', encoding='utf-8') as read_file:
    file_reader = csv.reader(read_file)
    data = []
    for index, item in enumerate(file_reader):
        if index == 0:
            name_of_columns = item
            del name_of_columns[-2]
        else:
            data.append(item)

wb = openpyxl.Workbook()
sheet = wb['Sheet']

# for row_index, value in enumerate(name_of_columns):
#     cell = sheet.cell(value=row_index + 1, column=row_index + 1)
#     cell.value = value



# wb = Workbook()
#
# dest_filename = 'empty_book.xlsx'
#
# ws3 = wb.create_sheet(title="Data")
# for row in range(10, 15):
#     for col in range(5, 10):
#         ws3.cell(column=col, row=row, value=col)
#
# wb.save(filename=dest_filename)

# wb = Workbook()
#
# dest_filename = 'empty_book.xlsx'
#
# ws4 = wb.create_sheet(title="Customer Data")
#
# for col_idx, col_val in enumerate(name_of_columns):
#     print(type(col_val))
#     if type(col_val):
#         ws4.cell(row=1, column=1, value=col_val)
#     else:
#         ws4.cell(row=2, column=col_idx * 1, value=col_val)
#
# wb.save(filename=dest_filename)


for data_list in data:
    del data_list[-2]
    # ['Person 6', '523481', 'Becca', '581946311']

    for col_index, col in enumerate(name_of_columns, data_list):
        for row_index, value in enumerate(col):
            cell = sheet.cell(row=row_index+1, column=col_index+1)
            cell.value = value


        # print(col_index)
        # print(col)
wb.save('data_excel.xlsx')

# for data_list in data:
#     del data_list[-2]
#     # ['Person 6', '523481', 'Becca', '581946311']
#     name_of_columns.append(data_list)
#
#     for col_index, col in enumerate(name_of_columns):
#         for row_index, value in enumerate(col):
#             cell = sheet.cell(row=row_index+1, column=col_index+1)
#             cell.value = value