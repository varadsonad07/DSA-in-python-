# binary search

def binarysearch(arr, key):
    l = 0
    r = len(arr) - 1  # last valid index
    
    while l <= r:
        mid = (l + r) // 2  # integer division
        
        if arr[mid] == key:
            print(f"key {key} is found at index {mid}")
            return mid
            
        elif key < arr[mid]:
            r = mid - 1
            
        else:
            l = mid + 1
    
    print(f"key {key} not found in the list")
    return -1

def main():
    arr = [1, 5, 6,8,9,11,44,77]
    key = int(input("Enter a key to search: "))
    binarysearch(arr, key)
    
if __name__ == "__main__":
    main()
