import re
from prettytable import PrettyTable


def headersToSnakeCase(headers: list):
    new_headers = []
    for elem in headers:
        new_headers.append(strToSnakeCase(elem))
    return new_headers


def strToSnakeCase(_str):
    _str = _str.split()
    _str[0] = _str[0].lower()
    for elem in range(1, len(_str)):
        _str[elem] = _str[elem].title()
    _str = ''.join(_str)
    return _str


def printPrettyTable(data: list):
    myTable = PrettyTable()
    headers = data[0]
    headers.insert(0, '#')
    myTable.field_names = headers
    for row in range(1, len(data)):
        cur_row = data[row]
        cur_row.insert(0, row)
        myTable.add_row(cur_row)
    print(myTable)


def deleteUnnecessary(line: list):
    new_line = []
    for element in line:
        new_element = re.sub("[\n]", "", element)
        new_element = re.sub("[\r]", "", new_element)
        new_element = deleteUnnecessarySpaces(new_element)
        new_line.append(new_element)
    return new_line


def deleteUnnecessarySpaces(element):
    if element[:1] == ' ':
        element = element[1:]
    if element[-1:] == ' ':
        element = element[:-1]
    return element


def count_lines(filename, chunk_size=1 << 13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))


def readCsv(file='example.csv', delimiter=';'):
    read_data = []
    with open(file, newline='') as cur_doc:
        lines = cur_doc.readlines()
        for line in lines:
            if len(line) > 1:
                clean_line = deleteUnnecessary(line.split(delimiter))
                read_data.append(clean_line)
    return read_data


def saveCsv(data: list, file='new_example.csv'):
    with open(file, 'w', newline='') as cur_doc:
        for row in data:
            cur_row = ''
            number = 1
            for element in row:
                element = deleteUnnecessarySpaces(element)
                cur_row += element + ';' if number < len(row) else element + '\n'
                number += 1
            cur_doc.write(cur_row)


def exportToJson(data: list, table_name='table name', element_name="element name", file='new_example.json'):
    with open(file, 'w', newline='') as cur_doc:
        headers = data[0]
        cur_doc.write('{\n')
        cur_doc.write('\t"' + table_name + '": ' + '{\n')
        for row in range(1, len(data)):
            cur_doc.write('\t\t"' + element_name + '_' + str(row) + '": {\n')
            for elem in range(0, len(headers)):
                cur_doc.write('\t\t\t')
                if elem < len(headers)-1:
                    cur_doc.write('"' + headers[elem] + '":\t"' + data[row][elem] + '",\n')
                else:
                    cur_doc.write('"' + headers[elem] + '":\t"' + data[row][elem] + '"\n')
            cur_doc.write('\t\t},\n') if row < len(data)-1 else cur_doc.write('\t\t}\n')
        cur_doc.write('\t}')
        cur_doc.write('\n}')


def exportToXml(data: list, table_name='table name', element_name='element name', file='new_example.xml'):
    with open(file, 'w', newline='') as cur_doc:
        headers = data[0]
        headers = headersToSnakeCase(headers)
        table_name = strToSnakeCase(table_name)
        element_name = strToSnakeCase(element_name)
        cur_doc.write('<' + table_name + '>\n')
        for row in range(1, len(data)):
            cur_doc.write('\t<' + element_name + '>\n')
            for elem in range(0, len(headers)):
                cur_doc.write('\t\t<' + headers[elem] + '>' + data[row][elem] + '</' + headers[elem] + '>\n')
            cur_doc.write('\t</' + element_name + '>\n')
        cur_doc.write('</' + table_name + '>\n')


if __name__ == "__main__":
    users = readCsv("username.csv")
    exportToXml(users, 'users', 'user')
    saveCsv(users)
    exportToJson(users, 'users', 'user')
    printPrettyTable(users)
