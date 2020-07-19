# Write a function that find the starting location and
# length of the longest continuous sequence of a single
# element

# [1,2,3,5,5,5,5,6,6,7]
#  number 5 has position of 3, and length of 4

# mylst = [1,2,3,5,5,5,5,6,6,7]
# mylst2 = "dddefkikqwaccccm"
#
# def sequence (alist):
#   pos = 0
#   lens = 1
#
#   mydict = {}
#   for x in alist:
#     if x in mydict:
#         mydict[x][1] +=1
#     else:
#         mydict.update({x:[pos,1]})
#     pos += 1
#
#   maxkey =max(mydict, key = lambda x: mydict[x][1])
#   print (maxkey, mydict[maxkey])
#
# # sequence(mylst)
# # sequence(mylst2)
#
# def removeDup (alist):
#     newlst = []
#     for x in alist:
#        if x in newlst:
#           pass
#        else:
#           newlst.append(x)
#
#     print (newlst)
#
# removeDup(mylst)


# A palindrome is a phrase, a word, or a sequence that reads the same forward and backward.
# One such example will be pip! An example of such a phrase will be ‘nurses run’.

# mystr = "nurses run"
#
# def palindrome (str):
#
#     mystr2 = str[::-1]
#     if str == mystr2:
#        print ("True")
#
# palindrome(mystr)

# mylst3 = [8,5,6,3,7]
#
# def bubblesort (alst):
#
#     for i in range(len(alst)-1,0,-1):
#       for j in range(i):
#         if alst[j] > alst [j+1]:
#            alst[j], alst [j+1] = alst[j+1],alst[j]
#     print (alst)
#
# bubblesort(mylst3)



# Write a function that takes a list L and returns a random sublist of size N of
# that list. Assume that the indexes must be in increasing order. That is,
# you cannot go backwards.
#
# Example:
#
# L = [1, 2, 3, 4, 5]
# N = 3
#
# The function should return one of these lists:
#
# [1, 2, 3]
# [1, 2, 4]
# [1, 2, 5]
# [1, 3, 4]
# [1, 3, 5]
# [1, 4, 5]
# [2, 3, 4]
# [2, 3, 5]
# [2, 4, 5]
# [3, 4, 5]
# def get_perm(nums, k):
#   if k == 1:
#     for n in nums:
#       yield [n]
#   else:
#     for i, n in enumerate(nums):
#       for x in get_perm(nums[i + 1:], k - 1):
#         yield [n] + x
#
# def main(nums, k):
#   if len(nums) < k:
#     return []
#   return list(get_perm(nums, k))
#
#
# print (main([1, 2, 3, 4, 5], 3))
#
# # User generator to create a infinite loop
# def infinite_sequence():
#   num = 0
#   while True:
#     yield num
#     num += 1

#use inifite loop to find palindrome
# def is_palindrome(num):
#     # Skip single-digit inputs
#     if num // 10 == 0:
#       return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#       reversed_num = (reversed_num * 10) + (temp % 10)
#       temp = temp // 10
#
#     if num == reversed_num:
#       return num
#     else:
#       return False



# Given various subsequences of an array, print the overall array:
#
# Example: [1, 3, 5], [1, 3, 9], [9, 5]
#
# Array : [1, 3, 9, 5]
# a = [1,3,5]
# b = [1,3 9]
# c = [9,5]
# print (list(set().union(a,b,c)))

#Given a range of routing numbers, determine which bank it belongs to
# mydict = {
#     'BOA':[1234,4567],
#     'WFG':[9812,9014]
# }
#
# def findBank (RoutNum):
#
#     for name,rnum in mydict.items():
#         num1 =rnum[0]
#         num2 =rnum[1]
#         if num1 == RoutNum or num2 ==RoutNum:
#             print (name)
# findBank (4567)

#Given a string of integer arrays, find the longest sequence
#[4,5,1,2,3,8,0,2], the output is [1,2,3]

# find a pattern in a string and output the parttern's position
# import re
# mystr = "This is a test"
# print (re.search("test",mystr).start())

#The password which contains characters, digits and special symbols are
# considered to be a strong password.
# For example, you want to generate a random Password like this.
#
#     ab23cd#$
#     jk%m&l98
#     87t@h*ki
import random
import string

# get random string password with letters, digits, and symbols
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    print("Random string password is:", password)

get_random_password_string(10)
get_random_password_string(10)

