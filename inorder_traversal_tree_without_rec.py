##using Stack
##post order is due , need to do this 

from inspect import stack


class treeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

    def inorder_traversal(self):
         
         ## left most 
         stack=[]
         current=self

         while(current!=None):
            stack.append(current)
            current=current.left
            while current==None and len(stack): ## it means its left tree is none , now we need to pop that as root
               popped=stack.pop()
               print(popped.val)
               current=popped.right  ##if its none , it simply means to move to one step upwards as that is root now
   
    
    def preorder_traversal(self):
        
             ## left most 
         stack=[]
         current=self

         while(current!=None):
            stack.append(current)
            print(current.val)
            current=current.left
            while current==None and len(stack): ## it means its left tree is none , now we need to pop that as root
               popped=stack.pop()
               current=popped.right  ##if its none , it simply means to move to one step upwards as that is root now
   




    def postorder_traversal(self):
         ## left most 
         stack=[]
         current=self

         while(current!=None):
            stack.append(current)
            print(current.val)
            current=current.left
            while current==None and len(stack): ## it means its left tree is none , now we need to pop that as root
               popped=stack.pop()
               current=popped.right  ##if its none , it simply means to move to one step upwards as that is root now
   



    # def inverted_tree(self):


       






root=treeNode(1)
root.left=treeNode(2)
root.right=treeNode(3)
root.left.left=treeNode(4)
root.left.right=treeNode(5)
# root.inorder_traversal()
root.preorder_traversal()

