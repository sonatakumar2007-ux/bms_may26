import quick_sort as qs
import sys 
input_numbers = [ int(value) for value in sys.argv[1:]]


print(f'numbers before sort are \n', input_numbers)
qs.quick_sort(input_numbers,0,len(input_numbers)-1)
print("numbers after sort are \n",input_numbers)