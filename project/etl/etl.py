import csv

TREE_DATABASE_TABLES = [
    ['location', ['location_id', 'address', 'neighborhood'], [3, 4]],
    ['species', ['species_id', 'taxonomy', 'common_name', 'functional_type', 'mature_size'], [6, 7, 8]],
    ['site', ['site_id', 'site_type', 'site_size', 'site_width', 'wires', 'improvement'], [11, 12, 13, 14, 15]],
    ['tree', ['tree_id', 'x_coord', 'y_coord', 'diameter', 'health', 'date_inventoried', 'location_id', 'species_id', 'site_id'], [0, 1, 9, 10, 5]]
  ]

def createTableCSVs(tables : list[str]):
    '''tables = [[tableName, [column1, column2, ...], [loc1, loc2, ...]], ...]'''
    database = getFilePath()
    for tb in tables:
        tableData(tb[2], database)


def getFilePath() -> str:
    print('Database File Path: ')
    file_path = input()
    return file_path


def tableData(column_loc : list[int], database : str) -> csv:
    table = set()
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
            table.add(tuple(temp))

    print(table)

    return table


def writeCSV(file : str, table : set):
    with open(file, mode='w', newrow='') as row:
        for row in :
            csv.writer(file).writerows(table)
    
    return None


if __name__ == '__main__':
    createTableCSVs(TREE_DATABASE_TABLES)