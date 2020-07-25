class binarySearchTree:
    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.p = None   #Parent node
        self.root=None
        self.BSTkey=None    #sum of greater node of a particular key
        self.sum=None   #Used while calculating sum of greater nodes
        self.dict_DP ={}    #Dynamic Programming structure to hold the already calculated sums

    def insert(self,key):
        if self.root==None:
            self.key=key
            self.root=self
            return
        y=None
        z=binarySearchTree()
        z.key=key
        x=self.root
        while x!=None:
            y=x
            if z.key<x.key:
                x=x.left
            else:
                x=x.right
        z.p=y
        # if y==None:
        #     self.root=z
        if z.key<y.key:
            y.left=z
        else:
            y.right=z    
        z.root=self.root  

    def contains(self,x,key):
        if x==None :
            return False
        if key==x.key:    
            
            return True
        if key<x.key:
            return self.contains(x.left,key)    
        else:
            return self.contains(x.right,key)    

    def inorder(self,x):
        if x!=None:
            self.inorder(x.left)
            print(x.key)
            self.inorder(x.right)

    def size(self):
        x=self.root
        count=0
        stack=[]
        stack.append(x)
        while len(stack)!=0:
            a=stack.pop()
            if a!=None:
                count=count+1
                stack.append(a.left)
                stack.append(a.right)
        return count

    def smallest(self,x):
        while x.left!=None:
            x=x.left
        return x

    def largest(self,x):
        while x.right!=None:
            x=x.right
        return x

    def get_item(self,x,key):
        if x==None or key==x.key:
            return x
        if key<x.key:
            return self.get_item(x.left,key)    
        else:
            return self.get_item(x.right,key) 

    def successor(self,key):
        x=self.get_item(self.root,key)
        if x==None:
            return None
        if x.right!=None:
            return self.smallest(x.right)
        y=x.p
        while y!=None and x==y.right:
            x=y
            y=y.p
        return y 

    def predecessor(self,key):
        x=self.get_item(self.root,key)
        if x==None:
            return None
        if x.left!=None:
            return self.largest(x.left)
        y=x.p
        while y!=None and x==y.left:
            x=y
            y=y.p
        return y 

    # Find sum of elements in tree rooted at 'x'
    def rightTreeSum(self,x):
        if x!=None:
            self.rightTreeSum(x.left)
            self.sum=self.sum+x.key
            self.rightTreeSum(x.right)
        
    # To find sum of greater node and store it in 'BSTkey'
    def greaterSumPerNode(self,x):
        key=x.key
        y=x
        sum=0
        
        if y.right!=None:
            self.greaterSumPerNode(y.right) 

        while x!=None:
            if x.key>=key:
                self.sum=0  
                # Memoization
                if x.key in self.dict_DP:
                    self.sum=self.sum+self.dict_DP[x.key]  
                    sum=sum+self.sum
                    break
                else:    
                    self.rightTreeSum(x.right)
                sum=sum+self.sum
            x=x.p
            if x!=None and x.key>=key:
                sum=sum+x.key
        y.BSTkey=sum
        self.dict_DP.update({y.key:y.BSTkey})       
        
        if y.left!=None:
            self.greaterSumPerNode(y.left)
        
    # Replace 'key' with 'BSTkey'
    def replaceWithGreaterSum(self,x):
        if x!=None:
            self.replaceWithGreaterSum(x.left)
            x.key=x.BSTkey
            self.replaceWithGreaterSum(x.right)
        
    
    def greaterSumTree(self):
        self.greaterSumPerNode(self.root)
        self.replaceWithGreaterSum(self.root)
        

x=binarySearchTree()

# EXAMPLE BST 1
# x.insert(6)
# x.insert(15)
# x.insert(3)
# x.insert(7)
# x.insert(20)
# x.insert(9)
# x.insert(4)
# x.insert(17)
# x.insert(13)
# x.insert(2)
# x.insert(18)

# EXAMPLE BST 2
x.insert(11)
x.insert(2)
x.insert(29)
x.insert(1)
x.insert(7)
x.insert(15)
x.insert(40)
x.insert(35)

x.inorder(x)

print("Smallest element "+str(x.smallest(x).key))

print("Largest element "+str(x.largest(x).key))

print("Size is "+str(x.size()))

key=35
successor=x.successor(key)
if successor == None:
  print("No successors for "+str(key))
else:
  print("Successor is "+str(successor.key))

key=2
predecessor=x.predecessor(key)
if predecessor == None:
  print("No predecessors for "+str(key))
else:
  print("Predecessor is "+str(predecessor.key))

key=15
y=x.contains(x,key)
if y:
    print(str(key)+" exists in the BST")
else:
    print(str(key)+" does not exist in the tree")

x.inorder(x)
print()
x.greaterSumTree()
x.inorder(x)
