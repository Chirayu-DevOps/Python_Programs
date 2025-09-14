# f =open ("D:\Chirayu_Devops\Python\Python I\O Operation\Demo.txt", "r")
# Data =f.read()
# print (Data)
# print(type(Data))
# f.close()

# f= open ("Demo.txt", "a")
# f.write("\n I want learn bash next")
# f.close()

# f= open ("Demo.txt", "r+")
# f.write("abc")
# print(f.read())
# f.close()

# f= open ("Demo.txt", "a+")
# print(f.read())
# f.write("Chirayu")
# f.close()

# with open ("Demo.txt", "r") as f:
#     data =f.read()
#     print(data)


# with open ("Demo.txt", "w") as f:
#     f.write ("new Data")

### code to find word "Python" from created fine demo.txt
# def check_for_word():
#     word = "learning"
#     with open("Demo.txt", "r") as f:  # Make sure the file name matches
#         Data = f.read()
#         if word in Data:
#             print("Found")
#         else:
#             print("Not Found")


def check_for_line():
    word = "learning"
    Data = True
    line_no = 1
    with open("Demo.txt", "r") as f:  # Make sure file name is consistent
        while Data:
            Data = f.readline()
            if word in Data:
                print(line_no)
                return
            line_no += 1
    return -1