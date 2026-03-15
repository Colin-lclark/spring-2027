import csv

AUTHORS = ('Fabrizio Martinez Valiente', 'Colin Sheehan')

TREE_DATABASE_TABLES = [
    ['location', ['location_id', 'address', 'neighborhood'], [3, 4]],
    ['species', ['species_id', 'taxonomy', 'common_name', 'functional_type', 'mature_size'], [6, 7, 8]],
    ['site', ['site_id', 'site_type', 'site_size', 'site_width', 'wires', 'improvement'], [11, 12, 13, 14, 15]],
    ['tree', ['tree_id', 'x_coord', 'y_coord', 'diameter', 'health', 'date_inventoried', 'location_id', 'species_id', 'site_id'], [2, 0, 1, 9, 10, 5]]
  ]

def createTableCSVs(tables : list[str]):
    '''tables = [[tableName, [column1, column2, ...], [loc1, loc2, ...]], ...]'''
    database = getFilePath('Database')
    for tb in tables:
        writeCSV(getFilePath(tb[0] + '.csv'), tableData(tb[1], tb[2], database, tb[0]))


def getFilePath(table : str) -> str:
    print(table + 'File Path: ')
    file_path = input()
    return file_path


def tableData(columns : list[str], column_loc : list[int], database : str, name : str) -> list[tuple]:
    table = [columns]
    table_set = set()
    id = 0

    with open(database, mode='r') as row:
        value = csv.reader(row)
        for row in value:
            temp = []

            #Adds all values specified for the given table
            for index in column_loc:

                #Seperates taxonomy from common name for species so they can be inputed as seperate values
                if index == 6:
                    for val in row[index].split(' - '):
                        temp.append(val)
                else:
                    temp.append(row[index])

            length = len(table_set)
            table_set.add(tuple(temp))

            if length != len(table_set):
                id += 1
                temp.insert(0, id)
                table.append(temp)

    return table


def writeCSV(file : str, table : list[tuple]):

    with open(file, mode='w', newline='') as row:
        csv.writer(row).writerows(table)


if __name__ == '__main__':
    createTableCSVs(TREE_DATABASE_TABLES)