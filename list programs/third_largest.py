L=eval(input("Enter a list of numbers: "))
L_size = len(L)
if (L_size < 3):
    print(" Invalid Input ")
    exit()
else:
    first = L[0]
    for i in range(1, L_size):
        if (L[i] > first):
            first = L[i]
 
    second = L[0]
    for i in range(1, L_size):
        if (L[i] > second and L[i] < first):
            second = L[i]
 
    third = L[0]
    for i in range(1, L_size):
        if (L[i] > third and L[i] < second):
            third = L[i]
 
    print("The Third Largest element is: ", third)
