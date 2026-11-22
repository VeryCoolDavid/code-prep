class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class Deque:
    
    def __init__(self):
        self.head=Node(-1)
        self.tail=Node(-1)
        self.head.next=self.tail
        self.tail.prev=self.head

    def isEmpty(self) -> bool:
        return self.head.next==self.tail

    def append(self, value: int) -> None:
        new_node=Node(value)
        left_node=self.tail.prev

        new_node.next=self.tail
        self.tail.prev=new_node
        new_node.prev=left_node
        left_node.next=new_node

    def appendleft(self, value: int) -> None:
        new_node=Node(value)
        right_node=self.head.next

        new_node.next=right_node
        right_node.prev=new_node
        new_node.prev=self.head
        self.head.next=new_node

    def pop(self) -> int:
        if not self.isEmpty():
            target_node=self.tail.prev
            left_node=target_node.prev
            left_node.next=self.tail
            self.tail.prev=left_node

            return target_node.val
        return -1

    def popleft(self) -> int:
        if not self.isEmpty():
            target_node=self.head.next
            right_node=target_node.next
            self.head.next=right_node
            right_node.prev=self.head

            return target_node.val
        return -1
