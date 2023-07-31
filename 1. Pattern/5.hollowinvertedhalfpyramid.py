def hollowinvertedhalfpyramid(input):

    for i in range(1, input+1):
        for j in range(i, input+1):
            if i == 1 or j == i or j == input:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    # row=input
    # for i in range(0,input):
    #     if (i==0 or i==input-1 or i==input-2):
    #         for j in range(0,row):
    #             print("*",end=" ")
    #     else:
    #         for j in range(0,row+1):

    #             if(j==0 or j==row):
    #                 print("*",end=" ")
    #             else:
    #                 print(" ",end=" ")

    #     print()
    #     row-=1
        

input=int(input("ENTER THE NUMBER: "))
print(hollowinvertedhalfpyramid(input))