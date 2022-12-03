

from cProfile import label
import random
import time
import numpy as np

import matplotlib.pyplot as plt

#tri par selection
def selectionSort(arr):

    size = len(arr)
    for step in range(size):
        minIndx = step

        for i in range(step+1,size):
            if(arr[i] < arr[minIndx]):
                minIndx = i
        
        (arr[step],arr[minIndx]) = (arr[minIndx],arr[step])  #swapping

#tri par fusion
def mergeSort(array):
    if len(array) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(array)//2
        L = array[:r]
        M = array[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def partition(array, low, high):

  # choose the middle element as pivot
  pivot = array[(high+low)//2 ]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)



    



    


if __name__ == "__main__":

   
    
    
    

    randomStart = 0
    randomEnd = 1000000
    randomTarget = 0
    times = 30

    #arr_lengths = [1000 , 2000 , 3000 , 4000 , 5000 , 6000 , 7000 , 8000 , 9000 , 10000]
    arr_lengths = [100 , 120 , 140 , 160 , 180 , 200 , 220 , 240 , 240 , 260 , 280 , 300 , 400 , 600 , 900 , 1300]
    
    arr_lengths_length = len(arr_lengths)

    selectionSortResult = np.arange(arr_lengths_length , dtype=float)
    mergeSortResult = np.arange(arr_lengths_length, dtype=float)
    quickSortResult = np.arange(arr_lengths_length, dtype=float)



    for k in range(arr_lengths_length):

        selectionSortSum = 0
        mergeSortSum = 0
        quickSortSum = 0

        arr_length = arr_lengths[k]
        arr = [0] * arr_length

        for i in range(times):


            #Remplissage
            for j in range(arr_length):
                arr[j] = random.randint(randomStart,randomEnd)

            #randomTarget = random.randint(randomStart,randomEnd)

            startTime = time.time()
            selectionSort(arr)
            endTime = time.time()
            selectionSortSum = selectionSortSum + (endTime - startTime)

            startTime = time.time()
            mergeSort(arr)
            endTime = time.time()
            mergeSortSum = mergeSortSum + (endTime - startTime)

            startTime = time.time()
            quickSort(arr,0,arr_length-1)
            endTime = time.time()
            quickSortSum = quickSortSum + (endTime - startTime)

        
        selectionSortResult[k] = selectionSortSum / times
        mergeSortResult[k] = mergeSortSum / times
        quickSortResult[k] = quickSortSum / times




    plt.plot(arr_lengths,selectionSortResult,label = "Selection Sort")
    plt.plot(arr_lengths,mergeSortResult,label = "Merge Sort")
    plt.plot(arr_lengths,quickSortResult,label = "Quick Sort")

    plt.xlabel("Array length")
    plt.ylabel("Time")
    plt.title("Comparison between Sorting Algorithms")

    plt.legend()

    plt.show()






    

    