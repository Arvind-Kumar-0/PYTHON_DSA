array = [10,1,-1,-4,11,0,5,12,19]

print(array)

def QuickSort(arr,start,end):
    if start >= end:
        return
    left = start 
    right = end  
    pivot = left+(right-left)//2
    pivot_number = arr[pivot]
    while left < right:
        while arr[left] < pivot_number:
            left += 1
        while arr[right] > pivot_number:
            right -= 1
        if left < right:
            arr[left] , arr[right] = arr[right] , arr[left]
            left += 1
            right -= 1
        
        QuickSort(arr,start,right)
        QuickSort(arr,left,end)
QuickSort(array,0,len(array)-1)
print(array)
 
n log n
