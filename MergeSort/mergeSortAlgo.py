#Merge Sort in Python
def MergeSort(LeftArray,RightArray):

    #Initialize the variables and loop
    #Initialize Newlist of length = length(LeftArray) + length(RightArray)
    Newlist=[] # can allocate memory for elements dynamically in python
    #Initialize i=0, j=0
    i=0
    j=0

    #Loop 
    while i < len(LeftArray) and j < len(RightArray):

        #Sorting the list or elements 
        if LeftArray[i] <= RightArray[j]:
            Newlist.append(LeftArray[i])
            i = i + 1
        else:
            Newlist.append(RightArray[j])
            j = j + 1
    if i< len(LeftArray):
        while i < len(LeftArray):
            Newlist.append(LeftArray[i])
            i = i + 1
    elif j < len(RightArray):
        while j < len(RightArray):
            Newlist.append(RightArray[j])
            j = j + 1
        
    print("Merged sorted list returned by MergeSort():",Newlist)
    print("".center(50,"-"))
    return Newlist

def MergeSortAlgorithm(Array, L, R):

    print("Array Recieved to MergeSortAlgorithm(): ", Array)
    #Base Case of Recursion
    if len(Array) == 1:
        print("Returned single element: ", Array)
        return Array

    #Finding the midpoint to divide the list
    mid = ( L + R ) // 2
    print("mid point found", mid)
    print("".center(80,"-"))

    #Recursion for left and right array
    print("Calling Left side: MergeSortAlgorithm(",Array[L:mid],",", L,",", mid,")")
    print("Array: ", Array[L:mid])
    print("".center(80,"-"))
    LeftArray = MergeSortAlgorithm(Array[L:mid], L, mid)

    print("Calling Right side: RightArray = MergeSortAlgorithm(",Array[mid:R],",", 0,",", R-mid,") ")
    print("Array: ", Array[mid:R])
    print("".center(80,"-"))
    RightArray = MergeSortAlgorithm(Array[mid:R], 0, R-mid)
    
    #Return the combined result
    print("Call to MergeSort(LeftArray, RightArray) combine and return the merged result")
    print("L Array: ", LeftArray,"\nR Array",RightArray)
    
    return MergeSort(LeftArray, RightArray)

AArray = MergeSortAlgorithm([10,5,2,6,3],0,5)
print("Final sorted array is : ",AArray)
