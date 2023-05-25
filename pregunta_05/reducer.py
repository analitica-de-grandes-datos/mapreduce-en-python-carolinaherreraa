#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    total_month = {}
    for line in sys.stdin:
        columns = line.split("\n")
        month = columns[0]
        if month in total_month:
            total_month[month] += 1
        else:
            total_month[month] = 1
    total_sort= sorted(total_month.items())
    for atributo,valor in total_sort:
        sys.stdout.write(f"{atributo}\t{valor}\n")