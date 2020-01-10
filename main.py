def sort_with_time(callback, *args, **kwargs):
    import time
    t = time.time()
    callback(*args, **kwargs)
    print(time.time() - t)


if __name__ == '__main__':
    import random
    import sort
    import copy
    use_time = True
    for n in [10, 100, 1000, 10000]:
        a = range(n)
        a = list(a)
        random.shuffle(a)
        if use_time:
            print(f'n = {n}')
        else:
            print(a)

        mem = copy.copy(a)
        for name in dir(sort):
            attr = getattr(sort, name)
            if callable(attr):
                print(name)
                if use_time:
                    sort_with_time(attr, a)
                else:
                    attr(a)
                    print(a)
            a = copy.copy(mem)
        print('\n\n')
