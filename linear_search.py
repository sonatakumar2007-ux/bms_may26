n=input("enter the number of elements in list")
ls=[]
for i in range(n):
    ls.append(int(input("enter element")))
key=int(input('enter the key'))
for i in ls:
    if i == key:
        print("key found at index :",ls.index(i))
    else:
        print("key not found")
