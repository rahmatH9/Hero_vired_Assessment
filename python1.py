numbers = [1,2,3,6,3,88,22,77]
if numbers:
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    print("Largest number:", largest)
else:
    print("List is empty")