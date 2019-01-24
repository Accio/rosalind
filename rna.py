#python
def transcribe(dnaString):
   transmap = {'A':'A', 'G':'G', 'C':'C', 'T':'U'}
   res = ''
   for dna in dnaString:
      res += transmap[dna]
   return(res)

def transcribe2(dnaString):
    return(dnaString.replace('T', 'U'))

exampleInput = 'GATGGAACTTGACTACGTAAATT'
exampleOutput = transcribe(exampleInput)
exampleOutput2 = transcribe2(exampleInput)

exampleExpectOutput = 'GAUGGAACUUGACUACGUAAAUU'

if exampleOutput != exampleExpectOutput:
    error('Something went wrong with dict method')

if exampleOutput2 != exampleExpectOutput:
    error('Something went wrong with replace')

with open('rosalind_rna.txt', 'r') as f:
    rnaInput = f.readline().rstrip('\n')

with open('rosalind_rna_output.txt', 'w') as f:
    f.write(transcribe(rnaInput))
