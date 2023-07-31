def solidRectangle(input):

    for i in range(0,input):
        for j in range(0,input):
            print(" * ",end="")
        print()

input=int(input("ENTER NUMBER: "))
print(solidRectangle(input))