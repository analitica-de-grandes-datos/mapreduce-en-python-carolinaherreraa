#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columns = line.split("   ")
        letter =columns[0]
        date=columns[1]
        num=columns[2]
        sys.stdout.write(f"{letter},{date},{num}\n")


