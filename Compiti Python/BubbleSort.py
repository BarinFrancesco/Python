import random as rnd

def main():
        arr = Getarray()
        for value in arr:
            print(value, end=" ")
        
        

    pass


def bubbleSort(arr):

    swapped = False
    for value in arr:
        swapped = False
        for confrontedvalue in arr:
            if value < confrontedvalue:
                temp = value
                value = confrontedvalue
                confrontedvalue = temp
                swapped = True
            
    if(not swapped):
    return arr

def Getarray():
    x = int(input("Enter the size of the array: "))
    arr = []
    for j in range(x):
        arr.append(rnd.randint(1, 100))
    return arr


if __name__ == "__main__":
    main()