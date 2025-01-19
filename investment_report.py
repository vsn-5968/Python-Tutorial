initial_invest=int(input("Enter the initial investment: "))
final_invest=int(input("Enter the final investment: "))
profit=final_invest-initial_invest
return_rate=(profit/initial_invest)*100
print("Return rate: ",return_rate,"%")
