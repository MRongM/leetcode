def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == item:
            return mid
        elif arr[mid]<item:
            low = mid + 1
        else:
            high = mid - 1
   

my_list = [i for i in range(10) if i%2!=0]
print(my_list)
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

