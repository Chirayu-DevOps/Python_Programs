# Write a Program to check given number is even or odd.

num = int(input("enter a number: "))

if num % 2 == 0:
    print("the give number is even")
else:
    print("the given number is odd")

# Wrire a program to print first 100 even numbers.

for i in range(1,101):
    print (i * 2, end=" ")

# Write a program to take selling price and purchase price from User
#     calculate its profit or loss?
#     if profit then print profit and amount of profit
#     if loss then pront loss and amount of loss

#     sp=100, pp=60 --> result -- profit of 40
#     sp=100, pp=120 --> result -- loss of 2

sp= int(input("Enter the selling price: "))
pp= int(input("Enter the purchase price: "))

if sp > pp:
    profit = sp- pp
    print (f"profit of {profit}")

elif pp> sp:
    loss = pp -sp
    print (f"Loss of {loss}")

else:
    print ("No Loss No Prfit")

