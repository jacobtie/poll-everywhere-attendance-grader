import csv
import json
from os import path
import re
import sys


def main() -> None:
    """Runs the script as a CLI app"""
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print('Usage: python main.py <module-number> <class-number> -e?')
        return
    module_num = sys.argv[1]
    class_num = sys.argv[2]
    if re.match('[01][0-9]', module_num) is None:
        print('module-number must be a valid module number')
        return
    if re.match('[12]', class_num) is None:
        print('class-number must be a valid class number')
        return
    is_extra_credit = False
    if len(sys.argv) == 4:
        flag = sys.argv[3]
        if flag != '-e' and flag != '--extra-credit':
            print('Invalid flag, must be -e or --extra-credit')
            return
        is_extra_credit = True
    fn = get_extra_credit_students if is_extra_credit else get_absent_students
    student_names = list(fn(module_num, class_num))
    student_names.sort(key=lambda n: n.split(' ')[1])
    print(*student_names, sep='\n')


def get_absent_students(module_num: str, class_num: str, is_test=False) -> set[str]:
    """Gets the list of students absent from class"""
    all_student_names = get_student_names(is_test)
    present_student_names = get_present_student_names(module_num, class_num)
    return all_student_names.difference(present_student_names)


def get_extra_credit_students(module_num: str, class_num: str) -> set[str]:
    """Gets the list of students present for an extra credit session"""
    present_student_names = get_present_student_names(module_num, class_num)
    return present_student_names


def get_student_names(is_test=False) -> set[str]:
    """Gets the full list of enrolled students"""
    with open('student_names.json' if not is_test else 'student_names_test.json', 'r') as file:
        student_names: list[str] = json.load(file)
    return set(student_names)


def get_present_student_names(module_num: str, class_num: str, is_extra_credit=False) -> set[str]:
    """Gets the students present in class given the module and class number"""
    poll_ev_file_lines = None
    file_name = f'class-{class_num}.csv' if not is_extra_credit else f'class-{class_num}-extra-credit.csv'
    with open(path.join('attendance', f'module-{module_num}', file_name), 'r', encoding='utf-8-sig') as file:
        poll_ev_file_lines = file.readlines()
    # Find the row starting with "Response,Via,Screen name" and remove all fluff before it so we just get the CSV
    header_row_index = -1
    for i, row in enumerate(poll_ev_file_lines):
        if row.strip().startswith('Response,Via,Screen name'):
            header_row_index = i
            break
    if header_row_index == -1:
        raise Exception('Never found header row')
    csv_lines = poll_ev_file_lines[header_row_index + 1:]
    csv_file = csv.reader(csv_lines)
    student_names = [row[3] for row in csv_file]
    return set(student_names)


if __name__ == '__main__':
    main()
