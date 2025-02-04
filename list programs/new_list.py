master_list=eval(input("Enter a list of numbers: "))
new_list=[]
filter = int(input("Enter a number which is less than the numbers in the list: "))
for num in master_list:
    if num < filter:
        new_list.append(num)
print("The new list with numbers less than", filter, "is:", new_list)
