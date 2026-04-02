import csv

AUTHORS = ('Fabrizio Martinez Valiente', 'Colin Sheehan')

TABLE_COLUMN_NAMES = {
    'location': ('location_id', 'address', 'neighborhood'),
    'species': ('species_id', 'taxonomy', 'common_name', 'functional_type', 'mature_size'),
    'site': ('site_id', 'site_type', 'site_size', 'site_width', 'wires', 'improvement'),
    'tree': ('tree_id', 'x_coord', 'y_coord', 'diameter', 'health', 'date_inventoried', 'location_id', 'species_id', 'site_id')
}

DATABASE_COLUMN_LOCATIONS = {
    'location': (3, 4),
    'species': (6, 7, 8),
    'site': (11, 12, 13, 14, 15),
    'tree': (0, 1, 9, 10, 5)                
}

TABLE_NAMES = ['location', 'species', 'site', 'tree']


def createTableCSVs(columns : dict[str], indices : dict[int], names : list[str]):
    database = getFilePath('Database')
    id_dicts = {}
    for name in names:
        path = getFilePath(name + '.csv')
        if name != 'tree':
            id_dicts[name] = createIDDictionary(path)
        else:
            writeCSV(path, tableData(columns[name], indices, database, name, id_dicts, names))


def getFilePath(name : str) -> str:
    print(name + 'File Path: ')
    file_path = input()
    return file_path


def tableData(columns : dict[tuple], indices : tuple[int], database : str, name : str, id_dicts : list[dict], names : list[str]) -> list[tuple]:
    table = [columns]
    table_set = set()
    id = 0
    n = 0

    with open(database, mode='r') as row:
        value = csv.reader(row)

        for row in value:
            temp = createRow(row, indices[name])

            #Gives the foreign keys to tree
            if name == 'tree' and n != 0:
                for val in names[:len(names) - 1]:
                    temp.append(id_dicts[val][tuple(createRow(row, indices[val]))])

            length = len(table_set)
            table_set.add(tuple(temp))
            
            #Only gives a unique id if a row is new to table
            if length != len(table_set) and n != 0:
                id += 1
                temp.insert(0, id)
                table.append(temp)
            
            #Makes sure n is only increased one time in order to avoid the first row
            if n == 0:
                n += 1

    return table


def createRow(row : list[str], column_loc : tuple[int]):
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

    return temp


def truncate(num : str, dec_places : int) -> str:

    #Check for a decimal
    if num.find('.') != -1:
        trunc = num.split('.')

        #Only truncate if num has too many decimal places
        if len(trunc[1]) > dec_places:
            trunc[1] = trunc[1][:dec_places]
            return trunc[0] + '.' + trunc[1]
        
    return num


def createIDDictionary(file : str):

    ids = {}
    with open(file, mode='r') as row:
        value = csv.reader(row)
        for row in value:
            ids[tuple(row[1:])] = row[0]
    return ids


def writeCSV(file : str, table : list[list[str]]):

    with open(file, mode='w', newline='') as row:
        csv.writer(row).writerows(table)


if __name__ == '__main__':
    createTableCSVs(TABLE_COLUMN_NAMES, DATABASE_COLUMN_LOCATIONS, TABLE_NAMES)