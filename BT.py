from __future__ import annotations
from typing import Any, Type

class Node:
    def __init__(self, key: Any,value: Any,left:Node = None, right: Node=None):
        self.key = key          #노드를 정렬하는 기준
        self.value = value      #노드에 포함하고 싶은 정보
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self,key:Any) -> Any:
        p = self.root
        while True:
            if p is None:
                return False    #원래는 None인데 임시로 바꿈
            if key == p.key:
                return True   #원래는 value인데 임시로 바꿈
            elif key < p.key:
                p = p.left
            else:
                p = p.right
        

    def add(self,key,value) -> bool:
        def add_node(node: Node,key,value) -> None:
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key,value,None,None)
                else:
                    add_node(node.left,key,value)
            else:
                if node.right is None:
                    node.right = Node(key,value,None,None)
                else:
                    add_node(node.right,key,value)
            return True
        
        if self.root is None:
            self.root = Node(key,value,None,None)
            return True
        else:
            return add_node(self.root,key,value)


    def remove(self,key) -> bool:
        p = self.root
        parent = None
        is_left_child = True

        while True:
            if p is None:
                return False
            
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        
        if p.left is None:  #자식이 없거나 하나인 경우
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                parent.right = p.right
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:               #자식이 둘인 경우
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key
            p.value = left.value
            if is_left_child:   #서브 트리 없는 경우
                parent.left = left.left #None 값을 넣는다.
            else:               #오른쪽 자식 있었을 경우
                parent.right = left.right 
        return True


