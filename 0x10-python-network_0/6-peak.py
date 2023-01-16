#!/usr/bin/python3
"""Find a peak model"""
def find_peak(list_of_integers):
    def helper(arr, low, high, n):
        mid = low + (high - low) // 2
        if ((mid == 0 or arr[mid-1] <= arr[mid]) and
            (mid == n-1 or arr[mid+1] <= arr[mid])):
            return mid
        elif (mid > 0 and arr[mid-1] > arr[mid]):
            return helper(arr, low, (mid-1), n)
        else:
            return helper(arr, (mid+1), high, n)
    n = len(list_of_integers)
    return list_of_integers[helper(list_of_integers, 0, n-1, n)]
