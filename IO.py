from csvkit.utilities.csvsql import CSVSQL

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

    # ---- CSV SQL MEME ----
    # queryString = "Select Person_id from person"

    # query = ['--query', queryString, csvPath]
    # res = CSVSQL(query)

    # '--query "Select Person_id from person" Dataset/mimic-iv-demo-data-in-the-omop-common-data-model-0.9/1_omop_data_csv/person.csv > yeet.csv'

    # print(res.main())

def QueryCSV(file, col1, col2):
    return [GetClassIds(file, GetColumnNum(file, col1)), GetClassIds(file, GetColumnNum(file, col2))]

def GetColumnNum(csvPath, name):
    file = open(csvPath, 'r')
    line = file.readline()
    file.close()

    line = line.split(',')

    i = 0
    for string in line:
        if string == name:
            return i
        i += 1
    print(name)
    return "name not found"