# simpleCsvParser
just a simple csv parser (doesn't use default csv library)

- parse .csv files:
  def readCsv(file, delimiter=';'),
  takes a name of a file, that you want to parse, and a delimiter,
  returns a list of parsered data.
- save to .csv file:
  def saveCsv(data: list, file),
  takes a list of data, that you want to save into a .csv file, and a name of a file, that you want to save;
- export into .json file,
  def exportToJson(data: list, file, table_name, element_name):
  takes a list of data, that you want to save into a .json file, a name of a file, that you want to save, a name of a table, and a name of elements;
- additional functions:
    + delete unnecessary spaces and '/n', '/r' symbols:
      def deleteUnnecessary(line: list),
      takes a list, that represents a row in a .csv file, and deletes unnecessary spaces and '/n', '/r' symbols,
      returns a new list without unnecessary symbols,
      this is ann additional function in readCsv(file, delimiter=';'),
      this function uses a subfunction that deletes unnecessary spaces:
        * def deleteUnnecessarySpaces(element),
          takes an element (str) of a row in a parent function (def deleteUnnecessary(line: list)) and deletes unnecessary spaces from it,
          return a new element (str);
    + count lines of a .csv file:
      def count_lines(filename, chunk_size=1 << 13),
      it takes a .csv file (actually any kind of text file, but i haven't checked this) and counts lines in it,
      returns numbers of lines (int)
