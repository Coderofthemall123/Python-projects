L = [4,5,1,2,9,7,10,8]
print("Original list:",L)

#variable to store the sum of
#the list
count = 0

#finding the sum
for i in L:
    count += i

#divide the total elements by
#number of elements
avg = count/len(L)

print("sum = ",count)
print("average =",avg)

#Sorting the elements of the list
L.sort()

#printing the fist element
print("Smallest element is:",L[0])

#printing the last element
print("Lergest element is:",L[-1])
