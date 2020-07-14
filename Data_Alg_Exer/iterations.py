import itertools

#given a list of numbers and a number k,
#print out the sum of any two numbers in the list = k
num = [10,15,3,7]
mylst = list(itertools.combinations(num,r=2))
print (mylst)

def to_k(lst,k):
    for num1, num2 in lst:
        if num1 +num2 == k:
             print (f" found: {num1} + {num2} = {k}")
        else:
             print (None)

if __name__ =="__main__":
    print ("calling main")
    to_k(mylst,17)

