import os
import openpyxl
import datetime

TIME_SPLIT_SHORTCUTS = 'time_split_shortcuts.xlsx'
TIME_SPLIT_RECORDS = 'time_split_records.xlsx'

SEP = os.path.sep
HOME = os.path.expanduser('~')

TIME_SPLIT_SHORTCUTS_PATH = HOME + SEP + 'Documents' + SEP + TIME_SPLIT_SHORTCUTS
TIME_SPLIT_RECORDS_PATH = HOME + SEP + 'Documents' + SEP + TIME_SPLIT_RECORDS

def read_shortcurts():
    ''' Read shortcut list file into a dictionary.
    
    return - A dictionary with the shortcuts and task name combinations.
    '''
    sc = {}
    wb = openpyxl.load_workbook(TIME_SPLIT_SHORTCUTS_PATH)
    sheet = wb.active
    row_modifyer = 0
    while True:
        cell_1 = sheet.cell(row = 2 + row_modifyer, column = 1)
        cell_2 = sheet.cell(row = 2 + row_modifyer, column = 2)
        if cell_1.value == None or cell_2.value == None:
            break
        sc[cell_1.value] = cell_2.value
        row_modifyer += 1
    wb.close()
    return sc

# TODO
'''
Input dialog for the user with the following options:
- type of input (e = end task, s = start task)
- shortcut (shortcut to be used for task identification)
'''

def set_task(task_name = ''):
    ''' Write a task to the Excel-Document.

    If the task_name is provided, a new task will be appended.
    Regardless if a task_name is provided, the last open task will be closed.

    task_name - optional paramenter with the name of the task.
    '''
    wb = openpyxl.load_workbook(TIME_SPLIT_RECORDS_PATH)
    sheet = wb.active
    row_count = len(sheet['A'])
    print(row_count)

    last_end = sheet.cell(row = row_count, column = 3)
    if last_end.value == None:
        last_end.value = datetime.datetime.now()

    if task_name:
        new_row = [task_name, datetime.datetime.now()]
        sheet.append(new_row)

    wb.save(TIME_SPLIT_RECORDS_PATH)
    wb.close()



if __name__ == '__main__':
    shortcut_list = read_shortcurts()
    for k, v in shortcut_list.items():
        print(k, v)
    set_task()
    # set_task(shortcut_list['a'])
    pass
