import csv

TREE_DATABASE_TABLES = [
    ['location', ['location_id', 'address', 'neighborhood'], [3, 4]],
    ['species', ['species_id', 'taxonomy', 'common_name', 'functional_type', 'mature_size'], [6, 7, 8]],
    ['site', ['site_id', 'site_type', 'site_size', 'site_width', 'wires', 'improvement'], [11, 12, 13, 14, 15]],
    ['tree', ['tree_id', 'x_coord', 'y_coord', 'diameter', 'health', 'date_inventoried', 'location_id', 'species_id', 'site_id'], [0, 1, 9, 10, 5]]
  ]

ALL_TABLES = []

def createTableCSVs(tables : list[str]):
    '''tables = [[tableName, [column1, column2, ...], [loc1, loc2, ...]], ...]'''
    database = getFilePath('Database')
    for tb in tables:
        ALL_TABLES.append(tableData(tb[1],tb[2], database, tb[0]))
    writeCSV(getFilePath(tb[0] + '.csv'), TREE_DATABASE_TABLES[3][1])


def getFilePath(table : str) -> str:
    print(table + ' File Path: ')
    file_path = input()
    return file_path


def getLocation(table : str):
    for i in range(TREE_DATABASE_TABLES):
        if TREE_DATABASE_TABLES[i][0] == table:
            return TREE_DATABASE_TABLES[i][2]
    return 0


def tableData(columns : str, column_loc : list[int], database : str, name : str) -> csv:
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

            #Get the species, site, and location ids for tree
            table.add(tuple(temp))

    return setToList(table, columns)


def setToList(table : set, columns : list[str]):
    id = 1
    table_list = [columns]
    for tup in table:
        temp = list(tup)
        temp.insert(0, id)
        table_list.append(temp)
        id += 1
    return table_list


def writeCSV(file : str, table):

    with open(file, mode='w', newline='') as row:
        csv.writer(row).writerows(table)


if __name__ == '__main__':
    createTableCSVs(TREE_DATABASE_TABLES)