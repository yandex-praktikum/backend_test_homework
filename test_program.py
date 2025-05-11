from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
dir_files = [filename.name.lower() for filename in BASE_DIR.iterdir()]

files_list = ['program.py', 'readme.md']


def test_program():
    for filename in files_list:
        assert filename in dir_files, f'Файл `{filename}` не найден.'

    try:
        import program
    except Exception as e:
        assert False, (
            'Не удалось запустить `program.py`. '
            'Исправьте в нем ошибки:\n'
            f'{e}'
        )
