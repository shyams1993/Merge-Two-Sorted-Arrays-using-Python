arr1 = [0,3,4,31,32]
arr2 = [4,6,30]
def mergeSortedArray(arr1,arr2):
    if len(arr1)==0 or len(arr2)==0:
        return arr1+arr2
    new=[]
    i=0
    j=0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<=arr2[j]:
            new.append(arr1[i])
            i+=1
        elif arr2[j]<arr1[i]:
            new.append(arr2[j])
            j+=1
    return new+arr1[i:]+arr2[j:]

print(mergeSortedArray(arr1,arr2))
