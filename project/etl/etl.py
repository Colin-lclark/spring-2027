import csv

AUTHORS = ('Fabrizio Martinez Valiente', 'Colin Sheehan')

TREE_DATABASE_TABLES = [
    ['location', ['location_id', 'address', 'neighborhood'], [3, 4]],
    ['species', ['species_id', 'taxonomy', 'common_name', 'functional_type', 'mature_size'], [6, 7, 8]],
    ['site', ['site_id', 'site_type', 'site_size', 'site_width', 'wires', 'improvement'], [11, 12, 13, 14, 15]],
    ['tree', ['tree_id', 'x_coord', 'y_coord', 'diameter', 'health', 'date_inventoried', 'location_id', 'species_id', 'site_id'], [0, 1, 9, 10, 5]]
  ]

def createTableCSVs(tables : list[str]):
    '''tables = [[tableName, [column1, column2, ...], [loc1, loc2, ...]], ...]'''
    database = getFilePath('Database')
    id_dicts = []
    for tb in tables:
        if tb[0] != 'tree':
            id_dicts.append(createIDDictionary(getFilePath(tb[0] + '.csv'), ))
        writeCSV(getFilePath(tb[0] + '.csv'), tableData(tb[1], tb[2], database, tb[0]))


def getFilePath(name : str) -> str:
    print(name + 'File Path: ')
    file_path = input()
    return file_path


def tableData(columns : list[str], column_loc : list[int], database : str, name : str, id_dicts : list[dict]) -> list[tuple]:
    table = [columns]
    table_set = set()
    id = 0
    n = 0

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

                #Truncate x and y coords to 6 decimal places
                elif index == 0 or index == 1:
                    temp.append(truncate(row[index], 6))

                #Truncate diameter and site_width to 2 decimal places
                elif index == 9 or index == 13:
                    temp.append(truncate(row[index], 2))

                else:
                    temp.append(row[index])

            if name == 'tree':
                for ids in id_dicts:
                    

            length = len(table_set)
            table_set.add(tuple(temp))

            if length != len(table_set) and n != 0:
                id += 1
                temp.insert(0, id)
                table.append(temp)
            
            if n == 0:
                n += 1

    return table

def truncate(num : str, dec : int) -> str:
    if num.find('.') != -1:
        trunc = num.split('.')
        if len(trunc[1]) > dec:
            trunc[1] = trunc[1][:dec]
            return trunc[0] + trunc[1]
    return num


def createIDDictionary(file : str, index : int):

    ids = {}
    with open(file, mode='r') as row:
        value = csv.reader(row)
        for row in value:
            ids[row[index]] = row[0]
    return ids


def writeCSV(file : str, table : list[tuple]):

    with open(file, mode='w', newline='') as row:
        csv.writer(row).writerows(table)


if __name__ == '__main__':
    createTableCSVs(TREE_DATABASE_TABLES)