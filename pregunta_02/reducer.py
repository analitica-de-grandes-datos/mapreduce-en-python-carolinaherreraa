#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == "__main__":
    max_credit = {}
    for line in sys.stdin:
        column = line.split("\t")
        purpose = column[0]
        amount= int(column[1])
        if purpose in max_credit:
            max_credit[purpose] = max(max_credit[purpose], amount)
        else:
            max_credit[purpose] = amount
    max_credit_sort = sorted(max_credit.items())
    for max_credit,value in max_credit_sort:
        sys.stdout.write(f"{max_credit}\t{value}\n")