#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        column = line.split(",")
        credit_history = column[2]
        sys.stdout.write(f"{credit_history}\n")
    