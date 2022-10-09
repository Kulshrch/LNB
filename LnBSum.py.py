a1=int(input("Enter a value:"))
a2=int(input("Enter 2nd value:"))
a3=int(input("Enter 3rd value:"))
a4=int(input("Enter 4th value:"))
a5=int(input("Enter 5th value:"))
List=[a1,a2,a3,a4,a5]
i=0
while(i<=4):
    if(List[i]<9):
        List.pop(i)
        i=i+1
        print(List)       
