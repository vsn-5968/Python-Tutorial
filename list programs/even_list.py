master_list=eval(input("Enter a list of numbers: "))
new_list=[]
for num in master_list:
    if num%2==0:
        new_list.append(num)
new_list.sort()
print("The new list with even numbers is:", new_list)
