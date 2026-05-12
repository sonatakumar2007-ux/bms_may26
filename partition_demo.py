import partition as pt
import sys 
input_numbers = [ int(value) for value in sys.argv[1:]]


print(f'numbers before partition are \n', input_numbers)
pt.partition_array(input_numbers,0,len(input_numbers)-1)
print("numbers after partition \n",input_numbers)
