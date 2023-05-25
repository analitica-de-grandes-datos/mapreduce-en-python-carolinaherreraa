#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    count_column = {}
    for line in sys.stdin:
        columns = line.split("\n")
        letter = columns[0]
        if letter in count_column:
            count_column[letter] += 1
        else:
            count_column[letter] = 1
    count_column_sort= sorted(count_column.items())
    for atributo,valor in count_column_sort:
        sys.stdout.write(f"{atributo},{valor}\n")



       