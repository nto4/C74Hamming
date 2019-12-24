#res = [i + j for i, j in zip(test_list1, test_list2)] 
list =["a","b","c","d"]
j = 0
for i in range(0,len(list),2):
    list[j]= list[i]+list[i+1]
    j = j+1
m =int( len(list) /2)
print(m)
for i in range(m,0,-1):
    del list[-1]
print(list)