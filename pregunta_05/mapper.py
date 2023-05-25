#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    for line in sys.stdin:
        columns = line.split("   ")
        date = columns[1]
        month=date.split("-")
        real_month=month[1]
        sys.stdout.write(f"{real_month}\n")


      