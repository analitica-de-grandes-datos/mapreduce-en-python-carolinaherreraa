#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    dictionary = {}
    count = 0
    
    for line in sys.stdin:
        column = line.split(",")
        if len(column) >= 3:
            letter = column[0]
            date = column[1]
            num = int(column[2])
            
            if num in dictionary:
                if dictionary[num] > (letter, date):
                    dictionary[num] = (letter, date)
            else:
                dictionary[num] = (letter, date)
    
    dictionary_sort = sorted(dictionary.items())
    
    for num, (letter, date) in dictionary_sort:
        sys.stdout.write(f"{letter}\t{date}\t{num}\n")
        count += 1
        if count == 6:
            break



 
        
    
