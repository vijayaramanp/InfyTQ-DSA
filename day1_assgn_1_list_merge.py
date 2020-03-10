#DSA-Assgn-1

def merge_list(list1, list2):
    merged_data=""
    negative_index=-1
    for i in range(0,len(list1)):
        if list1[i] is not None and list2[negative_index] is not None:
            merged_data=merged_data+" "+list1[i]+list2[negative_index]
        elif list1[i] is None:
            merged_data=merged_data+" "+list2[negative_index]
        else:
            merged_data=merged_data+" "+list1[i]
        negative_index-=1
    resultant_data=merged_data.strip()
    return resultant_data

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
