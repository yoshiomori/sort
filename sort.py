def insertion(a: list):
    i = 0
    n = len(a)
    while i < n:
        x = a.pop(i)
        j = i - 1
        while j >= 0:
            if a[j] < x:
                break
            j -= 1
        a.insert(j+1, x)
        i += 1


def bubble(a: list):
    i = 0
    n = len(a)
    while i < n:
        j = i + 1
        while j < n:
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
            j += 1
        i += 1


def quick(a: list):
    i = 0
    n = len(a)
    stack = [(i, n-1)]
    while stack:
        i, j = init, end = stack.pop()
        pivot = a[int((i+j)/2)]
        while i <= j:
            while a[i] < pivot:
                i += 1
            while a[j] > pivot:
                j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1
                j -= 1
        if init < j:
            stack.append((init, j))
        if i < end:
            stack.append((i, end))
