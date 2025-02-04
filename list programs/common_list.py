list_1=eval(input("Enter numbers in List 1: "))
list_2=eval(input("Enter numbers in List 2: "))
common_list=[]
for num in list_1:
    if num in list_2:
        common_list.append(num)
print("The new list with common elements in both the lists is: ", common_list)
