from pathlib import Path
from datetime import datetime


def create_empty_file():
    root = Path('files')
    for i in range(20, 41):
        file = root / Path(f'{i}.txt')
        print(file)
        file.touch()

def create_file():
    list_of_files = ['november/a.txt', 'november/b.txt', 'december/c.txt', 'december/d.txt']

    for file in list_of_files:
        with open(f'files/{file}', 'w') as f:
            f.write(file)

    files = Path('files')
    for file in files.glob('**/*'):
        if file.is_file():
            create_date = datetime.fromtimestamp(file.stat().st_ctime)
            print(f'File: {file.name}, Created: {create_date}, {file}')
            updated_filename = f'{create_date.strftime("%d-%m-%Y_%H-%M-%S")}_{file.name}'
            new_name = file.with_name(updated_filename)
            file.rename(new_name)

    for file in files.rglob('*.txt'):
        if file.is_file():
            file_name_withCSV = file.with_suffix('.csv')
            file.rename(file_name_withCSV)


if __name__ == '__main__':
    # create_file()
    create_empty_file()