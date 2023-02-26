#   1) Stack e'lon qiling va uning musbat va manfiy elementlar sonini toping.
'''
class Stack:
    def __init__(self):
        self.ls=[]
    def push(self,elem):
        self.ls.insert(0,elem)
    def pop(self):
        if self.ls!=[]:
            self.ls.pop(0)
        else:
            print("Stack is empty")
    def top (self):
        if self.ls!=[]:
            print(f"Top element of stack is {self.ls[0]}")
        else:
            print("Stack is empty")
    def show(self):
        for i in self.ls:
            print(i)
    def count_me(self):
        p=0
        n=0
        for i in self.ls:
            if i>=0:
                p+=1
            else:
                n+=1
        print("Musbat:",p,"\nManfiy:",n)
st1=Stack()
st1.push(-8)
st1.push(58)
st1.push(-69)
st1.push(-12)
st1.push(17)
st1.push(14)
st1.push(-1)
st1.push(4)
st1.count_me()
st1.pop()
st1.count_me()
st1.show()
'''
#   2) Stack e'lon qiling va uning o'rtadagi elementini o'chiring.(Agar elementlar soni toq bo'lsa 
#      o'rtadagi element o'chirilsin, agar elementlar soni juft bo'lsa o'rtadagi 2ta element o'chirilsin)

'''
class Stack:
    def __init__(self):
        self.ls=[]
    def push(self,elem):
        self.ls.insert(0,elem)
    def pop_middle(self):
        index=len(self.ls)
        if index%2==0:
            self.ls.pop(index//2)
            self.ls.pop((index//2)-1)
        else:
            self.ls.pop(index//2)
    def show(self):
        for i in self.ls:
            print(i)
st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.pop_middle()
st.show()
'''

#   3) Stack e'lon qiling va uning elementlarini teskari tartibda joylashtiring

'''
class Stack:
    def __init__(self):
        self.ls=[]
    def push(self,elem):
        self.ls.insert(0,elem)
    def reverse(self):
        index=len(self.ls)
        for i in range(index-1,-1,-1):
            print(self.ls[i])
    
st=Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)
st.reverse()
'''

#   4) Queue e'lon qiling va navbatdagi oxirigi elementiga teng bo'lgan elementlarni barchasini o'chiring
'''
class Queue:
    def __init__(self):
        self.ls=[1,2,3]
    def push_front_and_pop_equals(self,elem):
        self.ls.insert(0,elem)
        self.lp=[]
        for i in range(1,len(self.ls)):
            if self.ls[0]==self.ls[i]:
                self.lp.append(self.ls[i])
        self.remove(self.lp)

    def push_back_and_pop_equals(self,elem):
        self.ls.append(elem)
        self.lp=[]
        for i in range(len(self.ls)-1):
            if self.ls[-1]==self.ls[i]:
                self.lp.append(self.ls[i])
        self.remove(self.lp)
        
    def remove(self,elem):
        if len(elem)==1:
            elem.extend(elem)
        for i in self.ls:
            for j in elem:
                if i==j:
                    self.ls.remove(i)

    def show(self):
        print(self.ls)

qu=Queue()
qu.push_front_and_pop_equals(1)
qu.push_back_and_pop_equals(2)
qu.show()
'''
#   5) Queue e'lon qiling va uning o'rtasiga '+++' elementini qo'shib qo'ying. (Agar elementlar soni juft bo'lsa 
#      o'rtadagi 2ta element o'rtasiga joylashtiring, agar toq bo'lsa o'rtadagi elementning o'rniga joylashtiring)
'''
class Queue:
    def __init__(self):
        self.ls=[1,2,3,4,5,6,7,8,9,10]

    def push_middle(self,elem):
        if len(self.ls)%2==0:
            self.ls.insert(len(self.ls)//2,elem)
        else:
            self.ls[len(self.ls)//2]=elem
            
    def show(self):
        print(self.ls)

qu=Queue()
qu.push_middle('+++')
qu.show()
'''