import sys
import insertion_sort as ins

input_numbers = []

for i in range(1, len(sys.argv)):
    input_numbers.append(int(sys.argv[i]))

print(f'User given elements are \n', input_numbers)
sorted_list= ins.insertion_sort(input_numbers)
print("the sorted list is \n",sorted_list)