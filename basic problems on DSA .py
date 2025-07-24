# facrotial of given number
def factorial(n):
    res = 1
    for i in range (1,n+1):
        res = res * i
    return res

# print table of guiven number
def printtable(n):
    print(f"print table of {n}")
    for i in range (1 , 10+1):
        print(n * i)
    print()
    
# convert decimal number to binary number
def decimalTObinary(n):
    print(f"decimal number {n} to binary conversion is : ")
    while(n > 0):
        print(n % 2 , end = '' )
        n = int(n / 2)
    print()
    
# print a 2D matrix        
def print_matrix(mat):
    print("2D matris is : ")
    for i in range (len(mat)):
        for j in range (len(mat)):
            print(mat[i][j] , end = '  ')
        print()

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"{key} is found at index {i}")
            return i  # stop after finding the key
    # If the loop completes without finding the key
    print(f"{key} is not found in the list")
    return -1


# main function
def main():
    # for factorial
    result = factorial(5)
    print(f"5! = {result}")
    print()
    
    # for print a table 
    printtable(10)
    
    # for decimal to binary
    decimalTObinary(10)
    print()
    
    # 2D matric print
    mat = [[1,2,3] , [4,5,6] , [7,8,9]]
    print_matrix(mat)
    print()
    
    # linear search
    arr = [88 , 6 , 99 , 43 , 22 , 11 ]
    key = int(input("enter a key to search"))
    linear_search(arr , key)

# using this it can define main is a main function
if __name__ == "__main__":
    main()
