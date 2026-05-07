#in=12345
#luckydig=6
#sum of digits till the number is a single digits
import pdb
pdb.set_trace()
input_num=int(input("enter the number whose lucky digit is to be found\n"))
list1=list(str(input_num))
while len(list1)!=1:
    sum=0
    for i in list1:
        sum+=int(i)
    list1=list(str(sum))

print('the lucky digit for the given numbere is : ',int(list1[0]))

