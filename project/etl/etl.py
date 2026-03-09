import csv

TREE_DATABASE_FILE_PATH = 'C:\Users\Colin\OneDrive\Documents\GitHub\Databases\spring-2026\project\etl'

def createDatabaseCSV(database : str, tables : list[str]):
    '''tables = [[tableName, [column1, column2, ...], [loc1, loc2, ...]], ...]'''
    for tb in tables:
        tableData()


def getFilePath() -> str:
    file_path = input()
    return file_path


def tableData(columns : list[str], column_loc : list[int], database : str, file : str) -> list:
    table = [columns]
    id = 1
    with open(database) as line:
        table.append([id])
        for i in column_loc:
            table[len(table) - 1].append(list(csv.reader(line)[i]))
        id += 1

    with open(file, mode='w', newline='') as row:
        csv.writer(file).writerows(table)

    return table