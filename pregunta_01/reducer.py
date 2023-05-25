#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    atributte = {}
    for line in sys.stdin:
        column = line.split("\n")
        column1 = column[0]
        if column1 in atributte:
            atributte[column1] += 1
        else:
            atributte[column1] =1
    atribute_sort = sorted(atributte.items())
    for atribute,value in atribute_sort:
        sys.stdout.write(f"{atribute}\t{value}\n")