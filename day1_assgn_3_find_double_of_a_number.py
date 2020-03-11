#DSA-Assgn-3

def check_double(list1,list2):
    new_list=[]
    for num in list1:
        temp=2*num
        if temp in list2:
            new_list.append(num)
    return new_list

#Provide different values for the variables and test your program
list1=[11,8,23,7,25,15]
list2=[6,33,50,31,46,78,16,34]
print(check_double(list1, list2))
