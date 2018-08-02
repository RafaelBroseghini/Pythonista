#!/usr/bin/env python

'''
Implementation of Sorting Algorithms in Python.
'''
import time
import random

#Bubble sort with temp buffer. O(n^2).
def bubbleSort(aray):
    for num in range(len(array)-1,0,-1):
        for i in range(num):
            if array[i]>array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                
#Bubble sort with simultaneuos assignment. O(n^2).     
def bubble_Sort(array):
    for number in range(len(array)-1,0,-1):
        for i in range(number):
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                
#Selection sort. O(n^2).
def selection_sort(array):
    for num in range(len(array)-1,0,-1):
        positionOfMax = 0
        for i in range(num+1):
          if array[i] > array[positionOfMax]:
            positionOfMax = i
        array[i],array[positionOfMax] = array[positionOfMax], array[i]
    return array

#Quick Sort. O(log(n))
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

# Merge sort. O(n(log(n)).
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
