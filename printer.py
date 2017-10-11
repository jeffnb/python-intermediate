def counterwrap(func):
    def inner(s):
        from collections import Counter
        count = Counter(s)
        for item in count:
            print(item, count[item])
        print('    about to execute', func)
        func(s)
    
    return inner

@counterwrap
def printer(s):
    print(s)

printer('mississippi')
