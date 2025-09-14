# def greeting(): #simple function
#     print("Good Evening!")
# def add(num1,num2): #function with parameters
#     print("addition",num1+num2)
# def multi(num1,num2):
#     return num1*num2 #return value

# # Calling functions
# greeting()
# add(12,34)
# result= multi(6,7)
# print (result)
# print("multiplication",multi(5,3))

# write a function which takes 2 parameters username and password.
# if username is admin and password is admin123 then print login successful
# else print invalid credentials.

# Take username and password from user
username = input("Enter username: ")
password = input("Enter password: ")

if username == 'admin' and password == "admin123":
    print ("login successfully")
else:
    print ("invalid credentials")


