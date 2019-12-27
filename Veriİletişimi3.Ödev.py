import random
"""
This C 7,4 hamming implamentation is following this steps;
1-get input and print it:                                                         aa
2-print asci this input:                                                          ['01100001', '01100001']
3-convert 4 bit elements this each elements:                                      ['0110', '0001', '0110', '0001']
4-Generate hamming code for each elements and add 3 control bits and print it:    ['1100110', '1101001', '1100110', '1101001'] 
5-Add error bit each element:                                                     ['1100010', '1100001', '0100110', '1001001']
6-Check paritys correct errors:                                                   ['0110', '0001', '0110', '0001']
7-Generate asci bits using two corrected elements and print asci bits:            ['01100001', '01100001']
8-If same result to input hamming error correction is work:                       aa

"""
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

text = input("C (7,4) Hamming error correction code system \n Type the text to be hamming encoded (max. 100 character) \n")
fourbitarray = []
encodedarray = []
encodedaddedarray = []
bitarray = string2bits(text)
correctedfourbitarray = []
correcteasciarray = []

for i in range(0,len(bitarray)):
    fourbitarray.append((bitarray[i])[0:4])
    fourbitarray.append((bitarray[i])[4:9])


def hamcodedandAddError(p):
    #Encoding matrix
    G = ['1101', '1011', '1000', '0111', '0100', '0010', '0001']
    p = str(p)
    x = ''.join([str(bin(int(i, 2) & int(p, 2)).count('1') % 2) for i in G])
    encodedarray.append(x)
    #Add error 1 bit in 7 bit
    e = random.randint(1, 7)
    if e > 0:# İf error exist
        x = list(x)
        x[e - 1] = str(1 - int(x[e - 1]))
        x = ''.join(x)
    encodedaddedarray.append(x)
def correctionanddecode(x):
    # the parity-check matrix
    H = ['1010101', '0110011', '0001111']
    Ht = ['100', '010', '110', '001', '101', '011', '111']
    # the decoding matrix
    R = ['0010000', '0000100', '0000010', '0000001']
    z = ''.join([str(bin(int(j, 2) & int(x, 2)).count('1') % 2) for j in H])
    if int(z, 2) > 0:
        e = int(Ht[int(z, 2) - 1], 2)
    else:
        e = 0
    #Check parity and if have error bit, fix errored bit
    if e > 0:
        x = list(x)
        x[e - 1] = str(1 - int(x[e - 1]))
        x = ''.join(x)

    p = ''.join([str(bin(int(k, 2) & int(x, 2)).count('1') % 2) for k in R])
    correctedfourbitarray.append(p)

for i in range(0,len(fourbitarray)):
    hamcodedandAddError(fourbitarray[i])

print(bitarray)
print(fourbitarray)

print(encodedarray)   # hatabiti eklenmeden kodlanmış hali
print(encodedaddedarray)#  Hata biti eklenmiş kodlanmış hali

for i in range(0,len(fourbitarray)):
    correctionanddecode(str(encodedaddedarray[i]))

print(correctedfourbitarray)

j = 0
for i in range(0,len(correctedfourbitarray),2):
    correctedfourbitarray[j]= correctedfourbitarray[i]+correctedfourbitarray[i+1]
    j = j+1
m =int( len(correctedfourbitarray) /2)
for i in range(m,0,-1):
    del correctedfourbitarray[-1]
print(correctedfourbitarray)

cleanText = bits2string(correctedfourbitarray)
print(cleanText)
