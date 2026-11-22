class TreeNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None
class TreeMap:
    
    def __init__(self):
        self.root=None

    def insert(self, key: int, val: int) -> None:
        new_node= TreeNode(key,val)
        if self.root==None:
            self.root=new_node
            return
        curr= self.root
        while True:
            if key < curr.key:
                if curr.left==None:
                    curr.left=new_node
                    return
                curr=curr.left
            elif key>curr.key:
                if curr.right==None:
                    curr.right=new_node
                    return
                curr=curr.right
            else:
                curr.val=val
                return


    def get(self, key: int) -> int:
        curr=self.root
        while curr!=None:
            if curr.key<key:
                curr=curr.right
            elif curr.key>key:
                curr=curr.left
            else:
                return curr.val
        return -1
    def getMin(self) -> int:
        curr=self.root
        while curr and curr.left:
            curr=curr.left
        return curr.val if curr else -1

    def getMax(self) -> int:
        curr=self.root
        while curr and curr.right:
            curr=curr.right
        return curr.val if curr else -1
    def remove(self, key: int) -> None:
        self.root=self.removeHelper(self.root,key)

    def removeHelper(self,curr:TreeNode,key:int):
        if curr==None:
            return None
        if curr.key<key:
            curr.right=self.removeHelper(curr.right,key)
        elif curr.key>key:
            curr.left=self.removeHelper(curr.left,key)
        else:
            if curr.right==None:
                return curr.left
            elif curr.left==None:
                return curr.right
            else:
                node=curr.right
                while node and node.left:
                    node=node.left
                curr.val=node.val
                curr.key=node.key
                curr.right=self.removeHelper(curr.right,node.key)
        return curr
    def findMin(self,node:TreeNode):
        while node and node.left:
            node=node.left
        return node

    def getInorderKeys(self) -> List[int]:
        result=[]
        self.inorderTraversal(self.root,result)
        return result

    def inorderTraversal(self, root:TreeNode,result:List[int])->None:
        if root:
            self.inorderTraversal(root.left,result)
            result.append(root.key)
            self.inorderTraversal(root.right,result)
