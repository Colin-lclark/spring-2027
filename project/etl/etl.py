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
        tableData(tb[0] + '.csv', tb[1], tb[2], database)


def getFilePath() -> str:
    print('Database File Path: ')
    file_path = input()
    return file_path


def tableData(file : csv, columns : list[str], column_loc : list[int], database : str) -> csv:
    table = [columns]
    id = 1
    with open(database, mode='r') as line:
        value = csv.reader(line)
        for line in value:
            table.append([id])
            id += 1
            for index in column_loc:
                if index == 6:
                    for val in line[index].split(' - '):
                        table[len(table) - 1].append(val)
                else:
                    table[len(table) - 1].append(line[index])

    #Turns row into tuple so that it can be used in a set
    for value in table:
        value = tuple(value)

    #Ensures that values are not redundant by checking if turning table into a set decreases its length
        '''if table > set(table):
            table.pop()
        else:
            id += 1'''
    print(table[:4])


def writeCSV():
    with open(file, mode='w'):
      csv.writer(file).writerows(columns)

    with open(file, mode='w', newline='') as row:
        csv.writer(file).writerows(table)
    
    return None


if __name__ == '__main__':
    createTableCSVs(TREE_DATABASE_TABLES)