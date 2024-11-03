import random


def find_smallest(list_of_items):
    smallest = list_of_items[0]
    smallest_index = 0
    for i in range(1,len(list_of_items)):
        if (list_of_items[i] < smallest):
            smallest = list_of_items[i]
            smallest_index = i
    return smallest_index

def selection_sort(list_of_items):
    new_list = []
    for i in range(len(list_of_items)):
        smallest = find_smallest(list_of_items)
        new_list.append(list_of_items.pop(smallest))
    return new_list


myList1 = [5,2,6,8,1,3,4,9,7]
myList2 = ['mo','ah','yo','na','ne','ma','ha','ka','sa','im']
print(selection_sort(myList1))
print(selection_sort(myList2))

#.......................................................................................................................

def quick_sort_pivotFirst(list_of_items):
    if (len(list_of_items) < 2):
        return list_of_items
    else:
        pivot = list_of_items[0]
        less = [i for i in list_of_items[1:] if i <= pivot]
        more = [i for i in list_of_items[1:] if i > pivot]
        return quick_sort_pivotFirst(less) + [pivot] + quick_sort_pivotFirst(more)

def quick_sort_pivotRandom(list_of_items):
    if (len(list_of_items) < 2):
        return list_of_items
    else:
        randPivot = random.randint(0,len(list_of_items)-1)
        pivot = list_of_items[randPivot]
        less = [i for i in list_of_items[0:] if i <= pivot]
        more = [i for i in list_of_items[0:] if i > pivot]
        return quick_sort_pivotRandom(less) + quick_sort_pivotRandom(more)


myList1 = [5,2,6,8,1,3,4,9,7]
myList2 = ['mo','ah','yo','na','ne','ma','ha','ka','sa','im']
print(quick_sort_pivotFirst(myList1))
print(quick_sort_pivotFirst(myList2))
print(quick_sort_pivotRandom(myList1))
print(quick_sort_pivotRandom(myList2))