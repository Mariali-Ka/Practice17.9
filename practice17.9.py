error = "Перезапустите программу"
sequence_nums = input("Введите последовательность чисел через пробел: ")
user_num = int(input("Введите любое число: "))

def is_int(str):
    str = str.replace(" ", "")
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in sequence_nums:
    print("\nВ вводе отсутствуют пробелы (выполните корректно задание.)")
    sequence_nums = input("ВВедите последовательность чисел через пробел: ")
if not is_int(sequence_nums):
    print("\nВ Вводе содержаться не цифры, либо не целые числа (выполните корректно задание.) ")
    print(error)
else:
    sequence_nums = sequence_nums.split()

list_sequence_nums = [int(item) for item in sequence_nums]

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left and j < len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result



def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return "Число выходит за диапазон списка, введите меньше число. "

print(f"Последовательность списка по возрастанию: {list_sequence_nums}")

if not binary_search(list_sequence_nums, user_num, 0, len(list_sequence_nums)):
    rI = min(list_sequence_nums, key=lambda  x: (abs(x - user_num), x))
    ind = list_sequence_nums.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_num:
        print(f"В списке нет введенного элемента. \nБлижайщий меньший элемент: {rI}, его индекс: {ind} \nБлижайщий большой элемент: {list_sequence_nums[max_ind]} его индекс: {max_ind}")
    elif min_ind < 0:
        print(f"В списке нет введенного эдемента. \nБлижайщий больший элемент: {rI}, его индекс: {list_sequence_nums.index(rI)}. \nВ списке нет меньшего элемента ")
    elif rI > user_num:
        print(f"В списке нет введенного элемента. \nБлижайший больший элемент: {rI}, его индекс: {list_sequence_nums.index(rI)} \nБлижайший меньший элемент: {list_sequence_nums[min_ind]}, его индекc: {min_ind}")
    elif list_sequence_nums.index(rI) == 0:
        print(f"Индекс введенного элемента: {list_sequence_nums.index(rI)}")
else:
    print(f"Индекс введенного элемента: {binary_search(list_sequence_nums, user_num, 0, len(list_sequence_nums))}")
