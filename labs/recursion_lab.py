def explode(string):
    if string == "":
        return []
    else:
        return [string[0:1]] + explode(string[1:])

def my_filter(func, li):
    if li == []:
        return []
    else:
        return [li[0]] + my_filter(func, li[1:]) if func(li[0]) == True else my_filter(func, li[1:])

print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))