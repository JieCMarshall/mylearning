def anagram (st1, st2):
    list1=list(st1)
    list2=list(st2)
    if len(list1) != len(list2):
        raise Exception("two strings have different length")
    else:
        pos = 0
        match = True
        while pos <=len(st1) and match =True:
            if list1[pos]==list2[pos]:
                pos = pos+1
            else:
                match = False
        return match

