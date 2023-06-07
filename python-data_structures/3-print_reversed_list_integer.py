#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
    ##create a copy of the given list
       rList = my_list.copy()
    ##reverse the list
       rList.reverse()
    ##iterate through the list printing
       for i in rList:
          print("{:d}".format(i))
    
