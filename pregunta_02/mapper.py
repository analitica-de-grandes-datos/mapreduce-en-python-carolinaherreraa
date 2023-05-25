#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        column = line.split(",")
        purpose = column[3]
        amount = column[4]
        sys.stdout.write(f"{purpose}\t{amount}\n")