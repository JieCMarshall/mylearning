def hello(count):
    if count < 1:
        pass
    count = count-1
    hello(count)
    print ("here")

hello(5)