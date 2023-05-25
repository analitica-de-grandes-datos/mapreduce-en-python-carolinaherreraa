#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columns = linea.split(" ")
        column1 = columns[0]
        sys.stdout.write(f"{column1}\n")
        