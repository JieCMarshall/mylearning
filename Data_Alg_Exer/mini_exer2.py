# Write a function that find the starting location and
# length of the longest continuous sequence of a single
# element

# [1,2,3,5,5,5,5,6,6,7]
#  number 5 has position of 3, and length of 4

mylst = [1,2,3,5,5,5,5,6,6,7]
mylst2 = "dddefkikqwaccccm"

def sequence (alist):
  pos = 0
  lens = 1

  mydict = {}
  for x in alist:
    if x in mydict:
        mydict[x][1] +=1
    else:
        mydict.update({x:[pos,1]})
    pos += 1

  maxkey =max(mydict, key = lambda x: mydict[x][1])
  print (maxkey, mydict[maxkey])

sequence(mylst)
sequence(mylst2)
