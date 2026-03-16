import csv

AUTHORS = ('Fabrizio Martinez Valiente', 'Colin Sheehan')

TREE_DATABASE_TABLES = [
    ['tree', ['tree_id', 'x_coord', 'y_coord', 'diameter', 'health', 'date_inventoried', 'location_id', 'species_id', 'site_id'], [0, 1, 9, 10, 5]],
    ['location', ['location_id', 'address', 'neighborhood'], [3, 4, 2]],
    ['species', ['species_id', 'taxonomy', 'common_name', 'functional_type', 'mature_size'], [6, 7, 8, 2]],
    ['site', ['site_id', 'site_type', 'site_size', 'site_width', 'wires', 'improvement'], [11, 12, 13, 14, 15, 2]],
]

def createTableCSVs(tables : list[str]):
    '''tables = [[tableName, [column1, column2, ...], [loc1, loc2, ...]], ...]'''
    database = getFilePath('Database')
    ids = []
    for n in range(252206):
        ids.append([])
    i = 0
    for tb in tables:
        new = tableData(tb[2], database, tb[0])
        formatCSVs(new, tb[0])
        writeCSV(getFilePath(tb[0] + '.csv'), new)


def getFilePath(table : str) -> str:
    print(table + 'File Path: ')
    file_path = input()
    return file_path


def tableData(column_loc : list[int], database : str, name : str) -> list[tuple]:
    table = []
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
                else:
                    temp.append(row[index])
            if n != 0:
                table.append(temp)
            if n == 0:
                n += 1

    return table

def formatCSVs(table : list[list[str]], ids : list[list[int]], name : str):
    table_set = set()
    id = 0

    if name != 'tree':
        for i in table:
            length = len(table_set)
            temp = i[:len(i) - 1]
            table_set.add(tuple(temp))

            if length != len(table_set):
                id += 1
                temp.insert(0, id)
            
            ids[int(i[len(i) - 1])].append()
    
    return table


def writeCSV(file : str, table : list[tuple]):

    with open(file, mode='w', newline='') as row:
        csv.writer(row).writerows(table)


if __name__ == '__main__':
    createTableCSVs(TREE_DATABASE_TABLES)