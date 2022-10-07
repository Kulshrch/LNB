while(1):
    a=input("Enter a string:")
    if (len(a)<=7):
        i=0
        while(i<=len(a)):
            print(a[i])
            i=i+2
    else:
        j=1
        while(j<=len(a)):
            print(a[j])
            j=j+2
