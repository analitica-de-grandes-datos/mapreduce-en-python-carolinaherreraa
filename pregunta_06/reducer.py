#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    dictionary = {}
    for line in sys.stdin:
        columns = line.split(",")
        if len(columns) == 2:
            letter = columns[0]
            amount = float(columns[1])
            if letter in dictionary:
                dictionary[letter] = {
                    'max': max(dictionary[letter]['max'], amount),
                    'min': min(dictionary[letter]['min'], amount)
                }
            else:
                dictionary[letter] = {'max': amount, 'min': amount}
    
    dictionary_sort = sorted(dictionary.items(), key=lambda x: x[0])
    for atributo, valor in dictionary_sort:
        sys.stdout.write(f"{atributo}\t{valor['max']}\t{valor['min']}\n")

