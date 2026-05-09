def insertion_sort(numbers):
    for i in range(len(numbers)):
        element=numbers[i]
        j=i-1
        while element< numbers[j] and  j>=0 :
            numbers[j+1]=numbers[j]
            j-=1
        numbers[j+1]=element
    return numbers
