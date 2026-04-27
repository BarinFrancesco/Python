import random as rnd

def main():
    arr = Getarray()
    
    print("Original array:")
    for value in arr:
        print(value, end=" ")
    
    arr = bubbleSort(arr)
    
    print("\nSorted array:")
    for value in arr:
        print(value, end=" ")


def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        
        if not swapped:
            break
    
    return arr


def Getarray():
    x = int(input("Enter the size of the array: "))
    arr = []
    for j in range(x):
        arr.append(rnd.randint(1, 100))
    return arr


if __name__ == "__main__":
    main()