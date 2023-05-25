#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for linea in sys.stdin:
        columns = linea.split(",")
        if len(columns) == 2:
            letter = columns[0]
            num=int(columns[1])
            sys.stdout.write(f"{letter}\t{num}\n")


