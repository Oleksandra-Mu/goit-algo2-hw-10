import timeit
import random
import matplotlib.pyplot as plt


def randomized_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def random_array(n):
    arr = [random.randint(0, 10000) for _ in range(n)]
    return arr


def run_with_timing(func, *args):
    return timeit.timeit(lambda: func(*args), number=5) / 5


def visualize_results(result, n_values):
    random_times = [result[n][0] for n in n_values]
    deterministic_times = [result[n][1] for n in n_values]

    plt.figure(figsize=(10, 6))
    plt.plot(n_values, random_times, label="Рандомізований QuickSort", color="blue")
    plt.plot(
        n_values, deterministic_times, label="Детермінований QuickSort", color="orange"
    )
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого та детермінованого QuickSort")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    result = {}
    n_values = [10000, 50000, 100000, 500000]
    for n in n_values:
        arr = random_array(n)

        # Test randomized quick sort
        arr_copy = arr.copy()
        random_timing = run_with_timing(randomized_quick_sort, arr_copy)

        # Test deterministic quick sort
        arr_copy = arr.copy()
        deterministic_timing = run_with_timing(deterministic_quick_sort, arr_copy)
        result[n] = random_timing, deterministic_timing

        print(f"\nРозмір масиву: {n}")
        print(f"\tРандомізований QuickSort: {random_timing:.4f} секунд")
        print(f"\tДетермінований QuickSort: {deterministic_timing:.4f} секунд")
    visualize_results(result, n_values)


if __name__ == "__main__":
    main()
