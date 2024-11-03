def binary_search(list_of_items, item_to_find):
    low = 0
    mid = None
    high = len(list_of_items)-1
    while (low < high):
        mid = int((low+high)/2)
        guess = list_of_items[mid]
        if (guess==item_to_find):
            return guess
        elif (guess > item_to_find):
            high = mid-1
        else:
            low = mid+1
    return None

def binary_search_recursion(list_of_items, item_to_find, low, high):
    if (low < high):
        mid = int((low+high)/2)
        guess = list_of_items[mid]
        if(guess == item_to_find):
            return guess
        elif (guess > item_to_find):
            return binary_search_recursion(list_of_items, item_to_find, low, mid-1)
        else:
            return binary_search_recursion(list_of_items, item_to_find, mid+1, high)
    else:
        return None


myList1 = [1,2,3,4,5,6,7,8,9,10]
myList2 = ['mo','ah','yo','na','ne','ma','ha','ka','sa','im']
myList2.sort()
print(binary_search(myList2,'no'))
print(binary_search(myList1,9))
print(binary_search_recursion(myList2,'no',0,len(myList2)-1))
print(binary_search_recursion(myList1,9,0,len(myList1)-1))