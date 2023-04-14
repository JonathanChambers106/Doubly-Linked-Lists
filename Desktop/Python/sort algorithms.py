# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:40:35 2023

@author: crazy

Sort algorithms
"""
import time 
import timeit
import numpy.random as npr
import sys
import random
sys.setrecursionlimit(10**9) #necessary to prevent Quicksort for a large n hitting the recursion depth

#Size 1000 ascending array
ascend_array_1000 = []
for i in range(1000):
    ascend_array_1000.append(i)

#Size 10000 ascending array
ascend_array_10000 = []
for i in range(10000):
    ascend_array_10000.append(i)

#Size 100000 ascending array
ascend_array_100000 = []
for i in range(100000):
    ascend_array_100000.append(i)




#Size 1000 descending array
descend_array_1000 = []
for i in range(1000, 0, -1):
    descend_array_1000.append(i)

#Size 10000 descending array
descend_array_10000 = []
for i in range(10000, 0, -1):
    descend_array_10000.append(i)

#Size 100000 descending array
descend_array_100000 = []
for i in range(100000, 0, -1):
    descend_array_100000.append(i)
    
    
    
#The Randomized arrayis created by RNG_1 + i_1 * RNG_2 * i^2 * RNG_2  
#Size 1,000 random array
random_arr_1000 = []
for i in range(1000):
    random_arr_1000.append((random.randint(-2**31, 2**31) + i) * (int(npr.randint(-2**31, 2**31, size=1)) * (i**2)) * (int(npr.randint(-2**31, 2**31, size=1))))

#Size 10,000 random array
random_arr_10000 = []
for i in range(10000):
    random_arr_10000.append((random.randint(-2**31, 2**31) + i) * (int(npr.randint(-2**31, 2**31, size=1)) * (i**2)) * (int(npr.randint(-2**31, 2**31, size=1))))

#Size 100,000 random array
random_arr_100000 = []
for i in range(100000):
    random_arr_100000.append((random.randint(-2**31, 2**31) + i) * (int(npr.randint(-2**31, 2**31, size=1)) * (i**2)) * (int(npr.randint(-2**31, 2**31, size=1))))




#Generates the array
#By changing numbers I am able to create the different test cases amognst each of the sorting algorithms 
numbers = random_arr_1000

numberss = numbers.copy()
numbersss = numbers.copy()
numberssss = numbers.copy()

### Randomized Quicksort
"""Quick works by sorting an array into smaller ones and swappping the smaller ones based on the 'pivot'. 
It then will conitnue divide the array by placing values on the left side of the pivot like smaller values,
and bigger values on the right side until the array is sorted."""

def quickSort(myList, left, right):
    if right - left > 1:
        randIndex = npr.randint(left, right+1)
        pivot = myList[randIndex]
        #print(pivot)
    
        pivotIndex = partition(myList, pivot, left, right)
        quickSort(myList, left, pivotIndex)
        quickSort(myList, pivotIndex+1, right)
    
    elif right-left == 1:
        if myList[left] > myList[right]:
            temp = myList[right]
            myList[right] = myList[left]
            myList[left] = temp
    
    
def partition(myList, pivot, left, right):
    myList.remove(pivot)
    right = right-1
    
    while left <= right:
        if myList[left] <= pivot:
            left = left + 1
        elif myList[right] >= pivot:
            right = right - 1
        else:
            temp = myList[right]
            myList[right] = myList[left]
            myList[left] = temp
    
    myList.insert(left, pivot)

    #print(myList)
    #print(left)
    return left

# MergeSort
"""Merge sort uses a recursion algorithim that breaks the entire array into smaller arrays that look arrays similar to the sorted array.
It then sorts these smaller arrays using recursion that then puts the smaller sorted arrays into one big sorted array.
"""
def merge_sort(listy):
     if len(listy) > 1:
         mid = len(listy) // 2
         #left_half = listy[:mid]
         #right_half = listy[mid:]
 
         #left_half = merge_sort(left_half)
         #right_half = merge_sort(right_half)
         return merge(merge_sort(listy[:mid]), merge_sort(listy[mid:]))
     
     else:
         return listy
 
 
def merge(left_half, right_half):
     result = []
     i = j = 0
     while i < len(left_half) and j < len(right_half):
         if left_half[i] <= right_half[j]:
             result.append(left_half[i])
             i += 1
         else:
             result.append(right_half[j])
             j += 1
 
     result += left_half[i:]
     result += right_half[j:]
     return result





# Measure starting times
start_time = time.time_ns()
start_time2 = timeit.default_timer()

# Call MergeSort
numbersss = merge_sort(numbersss)

# report times
print("Total time: MergeSort " + str((time.time_ns()-start_time)/1000000000))
print("Doublecheck time using timeit:", timeit.default_timer() - start_time2)

#reset times
start_time = time.time_ns()
start_time2 = timeit.default_timer()

# Call Quicksort
quickSort(numberss, 0, len(numberss)-1)

# report times
print("Total time: Quick Sort " + str((time.time_ns()-start_time)/1000000000))
print("Doublecheck time using timeit:", timeit.default_timer() - start_time2)

#reset times
start_time = time.time_ns()
start_time2 = timeit.default_timer()


"""Selection sort works by iterating through all the elements in an unsorted array and 
bringing the smallest element to the front of the array. Once one is sorted and scans through the array again
and continues place the next smallest value to the front and so forth.
"""
# selection sort
for j in range(0, len(numbers)-1):
    
    if j%100 == 0 and j>0:
        time_elapsed = (time.time_ns() - start_time)/1000000000
        print("j = "+ str(j) + " time: " + str(time_elapsed))
    #Find the minimum of this list
    minimum = numbers[j]
    minPosn = j
    
    for i in range(j+1, len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]
            minPosn = i
    
    #Place the minimum in the first position of the list
    numbers.pop(minPosn)
    numbers.insert(j, minimum)
    
print("Total time: Selection Sort " + str((time.time_ns()-start_time)/1000000000))
print("Doublecheck time using timeit:", timeit.default_timer() - start_time2)