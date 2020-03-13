class Node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    
    def get_data(self):
        return self.__data
    
    def set_data(self,data):
        self.__data=data
    
    def get_next(self):
        return self.__next
    
    def set_next(self,next_node):
        self.__next=next_node

class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
    
    def get_head(self):
        return self.__head
    
    def get_tail(self):
        return self.__tail
    
    def add(self,data):
        new_node=Node(data)
        if self.get_head()==None:
            self.__head=new_node
            self.__tail=new_node
        else:
            self.get_tail().set_next(new_node)
            self.__tail=new_node
    
    def display(self):
        temp=self.get_head()
        while temp is not None:
            print(temp.get_data())
            temp=temp.get_next()
    
    def find_node(self,data):
        temp=self.get_head()
        while temp is not None:
            if temp.get_data()==data:
                return temp
            else:
                temp=temp.get_next()
    
    def insert(self,data,data_before):
        new_node=Node(data)
        insert_after=self.find_node(data_before)
        if insert_after is not None:
            new_node.set_next(insert_after.get_next())
            insert_after.set_next(new_node)
        else:
            print("invalid node")
                                              
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        temp=self.__head
        msg=[]
        while(temp is not None):
           msg.append(str(temp.get_data()))
           temp=temp.get_next()
        msg=" ".join(msg)
        msg="Linkedlist data(Head to Tail): "+ msg
        return msg


list1=LinkedList()
list1.add("Milk")
list1.add("Biscuit")
list1.add("Sugar")
list1.add("Salt")
list1.display()
#Insert the element in the required position
print("\nafter insertion in middle\n")
list1.insert("New Item","Sugar")
list1.display()


                                              
