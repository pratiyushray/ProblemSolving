def hollowrectangle(input):

    for i in range(0,input):
        if(i==0 or i==input-1):
            for j in range(0,input):
                print("*",end=" ")
        else:
            for j in range(0,input):
                if(j==0 or j==input-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print()


input=int(input("ENTER A NUMBER: "))
print(hollowrectangle(input))