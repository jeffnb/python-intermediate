def simple_generator(blah):
    print("Hello1")
    yield 1
    blah += 10
    print("Hello2")
    yield "boo!"
    blah += 10
    print("Hello3")
    yield 3


if __name__ == '__main__':
    for i in simple_generator(10):
        print(i)