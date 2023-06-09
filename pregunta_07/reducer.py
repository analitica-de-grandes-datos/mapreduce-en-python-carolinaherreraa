#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    group = []
    for line in sys.stdin:
        columns = line.split(",")
        if len(columns)==3:
            letter = columns[0]
            date = columns[1]
            num = int(columns[2])
            group.append((letter, date, num))

    sorted_group = sorted(group, key=lambda x: (x[0], x[2]))

    for elemento in sorted_group:
        sys.stdout.write(f"{elemento[0]}   {elemento[1]}   {elemento[2]}\n")




        