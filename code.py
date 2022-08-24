''' Count the number of nucleotide in a sequence'''

def function1(a):
	# create an empty dictionary
    b = dict()
	# Count the nucleotide number in a and return to the number of nucleotide which is b
    for c in a:
        if c not in b:
            b[c] = 1
        else:
            b[c] += 1
    return b

def function2(a):
    print('freqs')
    total = float(sum([a[b] for b in a.keys()]))
    for b in a.keys():
        print(b + ':' + str(a[b]/total))

function2(function1('ATCTGACGCGCGCCGC'))
