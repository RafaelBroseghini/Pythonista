'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Date: 04/08/2017
Filename: ComparingSortingAlgorithms.py
'''
import time
import random

print('Perfoming a benchmark analysis of a "slow" and a "fast" sorting algorithm:')
print()
print('Slow algorithm: ')
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
mylist = [random.randint(1, 1000) for i in range(10000)]
start = time.process_time()
bubbleSort(mylist)
end = time.process_time()
print('My list sorted using the bubble sort method:')
print(mylist)
print('Time elapsed during the bubble sort method :', end - start, 'sec')
print()
print('Fast algorithm: Quick Sort ')
def quick_Sort(alist):
   quick_SortHelper(alist,0,len(alist)-1)

def quick_SortHelper(alist,first,last):
   if first<last:

       splitpoint = Partition(alist,first,last)

       quick_SortHelper(alist,first,splitpoint-1)
       quick_SortHelper(alist,splitpoint+1,last)


def Partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
alist = []
for i in range(10000):
    number = random.randint(1, 1000)
    alist.append(number)
start = time.process_time()
quick_Sort(alist)
end = time.process_time()
print('My list using the quick sort:')
print(alist)
print('Time elapsed during the quick sort method :', end - start, 'sec')


def bubble_Sort(mylist):
    for number in range(len(mylist)-1,0,-1):
        for i in range(number):
            if mylist[i]>mylist[i+1]:
                mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
                

mylist = [random.randint(1, 1000) for i in range(10000)]
start = time.process_time()
bubble_Sort(mylist)
end = time.process_time()
print()
print('My list sorted using the bubble sort method using simultaneous assignment:')
print(mylist)
print('Time elapsed during the bubble sort method using simultaneous assignment:', end - start, 'sec')
print()






def shellSort(alist):
    sublistcount = len(alist)//3
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)
      sublistcount = sublistcount // 3
      
def shellsort(alist):
    sublistcount = len(alist)//4
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)

      sublistcount = sublistcount // 4
      
def shell_Sort(alist):
    sublistcount = len(alist)//5
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print("After increments of size",sublistcount,
                                   "The list is",alist)
      sublistcount = sublistcount // 5

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

alist = []
mylist = []
onelist = []
for i in range(10000):
    number = random.randint(1, 1000)
    alist.append(number)
    mylist.append(number)
    onelist.append(number)
print('Sorting using shell method subslists of count 3:')
start = time.process_time()
shellSort(alist)
end = time.process_time()
print('Time elapsed during the shell sort method (sublists of count 3):', end - start, 'sec')
print()
print()
print('Sorting using shell method subslists of count 4:')
start = time.process_time()
shellsort(mylist)
end = time.process_time()
print('Time elapsed during the shell sort method (sublists of count 4):', end - start, 'sec')
print()
print()
print('Sorting using shell method subslists of count 5:')
start = time.process_time()
shell_Sort(onelist)
end = time.process_time()
print('Time elapsed during the shell sort method (sublists of count 5):', end - start, 'sec')
print()
print('My list using the shell sort method (sublist = 3 elements):')
print(alist)
print()
print('My list using the shell sort method (sublist = 4 elements):')
print(mylist)
print()
print('My list using the shell sort method (sublist = 5 elements):')
print(onelist)
print()


def mergeSort(alist):
    print("Splitting ",alist)
    lefthalf = []
    righthalf = []
    if len(alist)>1:
        mid = len(alist)//2
        for i in range(mid):
            lefthalf.append(alist[i])
        print(lefthalf)
        
        for i in range(mid, len(alist)):
            righthalf.append(alist[i])
        print(righthalf)
            

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

alist = []
for i in range(1000): # Merge sort for 10000 numbers omitts output but it is one of the fastest algorithms. I have changed the number of loops to not omitt output.
    x = random.randint(1, 1000)
    alist.append(x)
start = time.process_time()
mergeSort(alist) 
end = time.process_time()
print(alist)
print('Time elapsed during the merge sort method:', end - start, 'sec')
print()

def swap(array,a,b):
    array[a],array[b] = array[b],array[a]
    
def partition(array,start,end):
    median = (end - 1 - start) % 2
    median = median + start
    left = start + 1
    if (array[median] - array[end-1])*(array[start]-array[median]) >= 0:
        swap(array,start,median)
    elif (array[end - 1] - array[median]) * (array[start] - array[end - 1]) >=0:
        swap(array,start,end - 1)
    pivot = array[start]
    for right in range(start,end):
        if pivot > array[right]:
            swap(array,left,right)
            left = left + 1
    swap(array,start,left-1)
    return left-1

def quickSortHelper(array,start,end):
    if start < end:
        splitPoint = partition(array,start,end)
        quickSortHelper(array,start,splitPoint)
        quickSortHelper(array,splitPoint+1,end)
        
def quickSort(array):
    quickSortHelper(array,0,len(array))
    

array = []
for i in range(10000):
    number = random.randint(1, 1000)
    array.append(number)
start = time.process_time()
quickSort(array)
end = time.process_time()
print('My list using the quick sort median-of-three method:')
print(array)
print('Time elapsed during the quick sort median-of-three method:', end - start, 'sec')

def quick_Sort(alist):
   quick_SortHelper(alist,0,len(alist)-1)

def quick_SortHelper(alist,first,last):
   if first<last:

       splitpoint = Partition(alist,first,last)

       quick_SortHelper(alist,first,splitpoint-1)
       quick_SortHelper(alist,splitpoint+1,last)


def Partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
print()
alist = []
for i in range(10000):
    number = random.randint(1, 1000)
    alist.append(number)
start = time.process_time()
quick_Sort(alist)
end = time.process_time()
print('My list using the quick sort:')
print(alist)
print('Time elapsed during the quick sort method :', end - start, 'sec')
