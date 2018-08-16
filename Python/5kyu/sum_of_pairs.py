def sum_pairs(lst, s):
    cache = set()
    print(cache)
    for i in lst:
        print(i)
        if s - i in cache:
            print (s-i)
            return [s - i, i]
        cache.add(i)
