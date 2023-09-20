import os

import program

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_files = [filename.lower() for filename in os.listdir(BASE_DIR)]

files_list = ['program.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in (dir_files, f'Файл `{filename}`'
                            f'не найден в корне репозитория')

    try:
        program
    except Exception as e:
        assert False, (
            'Не удалось запустить `program.py`. '
            'Исправьте в нем ошибки:\n'
            f'{e}'
        )
