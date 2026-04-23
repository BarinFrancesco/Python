import random as rnd

def main():
    arr = Getarray()
    for value in arr:
        print(value, end=" ")
     
    arr = InvertiArray(arr)
    print("\nInverted array: ")
    for value in arr:
        print(value, end=" ")



def Getarray():
    x = int(input("Enter the size of the array: "))
    arr = []
    for j in range(x):
        arr.append(rnd.randint(1, 100))
    return arr

def InvertiArray(arr):
    for i in range(len(arr) // 2):#doppio / perché vsennè ritorna un float e invece ci serve un int
        temp = arr[i]
        arr[i] = arr[len(arr) -1 - i]
        arr[len(arr) - 1 - i] = temp
    return arr


if __name__ == "__main__":
    main() 