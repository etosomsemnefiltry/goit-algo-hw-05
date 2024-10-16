def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        # Если значение arr[mid] меньше x, продолжаем искать справа
        if arr[mid] < x:
            low = mid + 1
        # Если значение arr[mid] больше или равно x, обновляем upper_bound и продолжаем искать слева
        else:
            upper_bound = arr[mid]
            high = mid - 1

    return (iterations, upper_bound)


arr = [1.1, 2.5, 3.3, 4.8, 6.7, 8.2]
x = 8.1

result = binary_search(arr, x)
print(f"Итераций: {result[0]}, Верхняя граница: {result[1]}")
