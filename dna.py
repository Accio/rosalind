## count nucleotides in DNA sequence

def countNuc(dnaString):
    res = {'A':0, 'C':0, 'G':0, 'T':0}
    for dna in dnaString:
        res[dna] += 1
    return(res)

myStr = 'ATGCATTC'
myStrCounts = countNuc(myStr)

print(myStrCounts)
print(myStrCounts.values())
print(myStrCounts.keys())
