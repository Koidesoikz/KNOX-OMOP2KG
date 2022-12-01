def WriteFile(lines):
    f = open("Mapping(1).txt", 'w')
    f.writelines(lines)
    f.close

def Rejig(lines):
    goodLines = []

    for line in lines:
        line = line.split(';')
        line[0] = line[0].strip()
        line[1] = line[1].strip()
        goodLines.append(str(line[1] + ";" + line[0]) + "\n")

    return goodLines

def ReadFile():
    f = open("dingdong.txt", 'r')
    lines = f.readlines()
    f.close
    return lines

WriteFile(Rejig(ReadFile()))
