
#Returns an array of IDs from the given csv
def GetClassIds(csvPath, column):
    file = open(csvPath, 'r')
    count = 0
    res = []

    while True:
        count += 1

        line = file.readline()

        if not line:
            break
        
        res.append(line.split(",")[column])
    
    file.close()

    return res

def QueryCSV(file, col1, col2):
    return [GetClassIds(file, GetColumnNum(file, col1)), GetClassIds(file, GetColumnNum(file, col2))]

#Finds the column number based on the column name for a given csv
def GetColumnNum(csvPath, name):
    file = open(csvPath, 'r')
    line = file.readline()
    file.close()

    line = line.split(',')

    i = 0
    for string in line:
        string = string.strip()
        
        if string == name:
            return i
        i += 1
    print("Name not found: " + name)
    print("Path: " + csvPath)
    return "name not found"