class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        
        if self.__top==self.get_max_size()-1:
            return True
        else:
            return False
        
    def push(self,data):
        if self.is_full()==False:
            self.__top+=1 
            self.__elements[self.__top]=data
        else:
            print("Stack is full")
                                          
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

stack1=Stack(5)
#Push all the required element(s).
stack1.push("Shirt1")
stack1.push("Shirt2")
stack1.push("Shirt3")
stack1.push("Shirt4")
stack1.push("Shirt5")
print(stack1.__str__())
stack1.push("Shirt1")
