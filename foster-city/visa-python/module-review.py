import mymodule

foo = "bar"

if __name__ == '__main__':
    print(__name__)

    # for i in range(10000):
    #     print(i)

    list1 = ["Harry", "Sally", "Fred", "George"]
    for name in list1:
        if name == "George":
            break
        print(name)
    else:
        print("Lets talk about George behind his back")
