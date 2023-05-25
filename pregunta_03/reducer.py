#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    dictionary = {}
    for line in sys.stdin:
        columns = line.split("\t")
        if len(columns) == 2:
            letter = columns[0] 
            num = int(columns[1])
            dictionary[letter] = num
            
    dictionary_sort = sorted(dictionary.items(), key=lambda x: x[1])
    for atributo,valor in dictionary_sort:
        sys.stdout.write(f"{atributo},{valor}\n")