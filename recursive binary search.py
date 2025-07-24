# recursive binary search

def binarysearch(arr, key, l, r):
    if l > r:
        # Key not found
        return -1

    mid = (l + r) // 2

    if arr[mid] == key:
        print(f"Key {key} is found at index {mid}")
        return mid
    elif key < arr[mid]:
        return binarysearch(arr, key, l, mid - 1)
    else:
        return binarysearch(arr, key, mid + 1, r)

def main():
    arr = [1, 5, 6, 8, 9, 11, 44, 77]
    key = int(input("Enter a key to search: "))
    l = 0
    r = len(arr) - 1

    index = binarysearch(arr, key, l, r)
    if index == -1:
        print(f"Key {key} not found in the list")

if __name__ == "__main__":
    main()
