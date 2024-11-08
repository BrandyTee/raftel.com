#Python3 code to demonstrate working of
# Shuffle two lists with same order
# Using zip() + * operator + shuffle()
import random
 
# initializing lists
test_list1 = [6, 4, 8, 9, 10]
test_list2 = [1, 2, 3, 4, 5]
test_list3 = [1, 8, 3, 7, 5]
 
# printing lists
print(f"The original list 1 : {test_list1}")
print(f"The original list 2 : {test_list2}")
print(f"The original list 3 : {test_list3}")
 
# Shuffle two lists with same order
# Using zip() + * operator + shuffle()
temp = list(zip(test_list1, test_list2, test_list3))
random.shuffle(temp)
res1, res2, res3 = zip(*temp)
# res1 and res2 come out as tuples, and so must be converted to lists.
res1, res2, res3 = list(res1), list(res2), list(res3)
 
# Printing result
print(f"List 1 after shuffle :  {res1}")
print(f"List 2 after shuffle :  {res2}")
print(f"List 2 after shuffle :  {res3}")