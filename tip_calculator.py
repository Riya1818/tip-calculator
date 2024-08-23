print("welcome to tip calculator")
bill=int(input("enter the total amount to be paid:"))
ppl=int(input("enter the total no. of people :"))
tip=int(input("enter the tip percentage to be given(10,12 or 15):"))
total_tip=1+(tip/100)
amount=(bill/ppl)*total_tip
print(f"the total amount to be given by each person is: ${round(amount,2)}")