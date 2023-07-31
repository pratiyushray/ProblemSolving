def invertedhalfpyramid(input):
    row=input
    for i in range(0,input):
        for j in range(0,row):
            print(" * ",end=" ")
        
        print()
        row-=1
    

input=int(input("ENTER THE NUMBER: "))
print(invertedhalfpyramid(input))