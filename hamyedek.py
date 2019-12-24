import random

def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


text = input()
fourbitarray = []
encodedarray = []
encodedaddedarray = []
bitarray = string2bits(text)
correctedfourbitarray = []

#print(bitarray)
#print(type(bitarray[0]))
for i in range(0,len(bitarray)):
    fourbitarray.append((bitarray[i])[0:4])
    fourbitarray.append((bitarray[i])[4:9])

print(fourbitarray)


def hamcodederdecoder(p):
    # the encoding matrix
    G = ['1101', '1011', '1000', '0111', '0100', '0010', '0001']
    # the parity-check matrix
    H = ['1010101', '0110011', '0001111']
    Ht = ['100', '010', '110', '001', '101', '011', '111']
    # the decoding matrix
    R = ['0010000', '0000100', '0000010', '0000001']

    #Get input       #p = 1001 #''.join([random.choice('01') for k in range(4)])
    p = str(p)
    #print ('Input bit string: ' + p)

    x = ''.join([str(bin(int(i, 2) & int(p, 2)).count('1') % 2) for i in G])
    encodedarray.append(x)
    #print ('Encoded bit string to send: ' + x)
   
    # add 1 bit error
    e = random.randint(1, 7)
    # counted from left starting from 1
    #print ('Which bit got error during transmission (0: no error): ' + str(e))
    
    x = list(x)
    x[e - 1] = str(1 - int(x[e - 1]))
    x = ''.join(x)
    #print ('Encoded bit string that got error during tranmission: ' + x )
    encodedaddedarray.append(x)

    #print ('Which bit found to have error (0: no error): ' + str(e))

testinput = 1101001
def correction(x):
    #print("Correction")
    # the encoding matrix
    G = ['1101', '1011', '1000', '0111', '0100', '0010', '0001']
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
     # correct the error
    if e > 0:
        x = list(x)
        x[e - 1] = str(1 - int(x[e - 1]))
        x = ''.join(x)

    p = ''.join([str(bin(int(k, 2) & int(x, 2)).count('1') % 2) for k in R])
    #print("value of p : " + p)
    correctedfourbitarray.append(p)
    #print(len(correctedfourbitarray))
    #print ('Corrected output bit string: ' + p )

for i in range(0,len(fourbitarray)):
    hamcodederdecoder(fourbitarray[i])
print(encodedarray)   # hatabiti eklenmeden kodlanmış hali
print(encodedaddedarray)#  Hata biti eklenmiş kodlanmış hali

for i in range(0,len(fourbitarray)):
    correction(str(encodedaddedarray[i]))

print(correctedfourbitarray)
#print(correctedfourbitarray)
#print(correction("1100111"))