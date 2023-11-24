#Сортировка пузырьком
def bubble_sort(list1):
    for i in range(0, len(list1) - 1):
        for j in range(len(list1) - 1):
            if (list1[j] > list1[j + 1]):
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    return list1

list1 = [5, 3, 8, 6, 7, 2]
print(list1)
print(bubble_sort(list1))

#Сортировка вставками
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp

alist = input('Введите список номеров: ').split()
alist = [int(x) for x in alist]
insertion_sort(alist)
print('Сортированный список: ', end='')
print(alist)

