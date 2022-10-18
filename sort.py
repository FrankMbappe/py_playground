def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j + 1] < numbers[j]:
                # Swap
                temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
    return numbers


arr = [7, 3, 5, 9, 11, 13, 6]

print(bubble_sort(arr))
