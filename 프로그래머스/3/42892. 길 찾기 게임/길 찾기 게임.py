import sys
sys.setrecursionlimit(10**6) 

class Node:
    def __init__(self, x, y, index):
        self.x = x
        self.y = y
        self.index = index
        self.left = None
        self.right = None
         
def insert(parent: Node, child: Node):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert(parent.right, child)
    
def buildTree(nodeinfo) -> Node:
    nodes = []
    for index, (x, y) in enumerate(nodeinfo):
        nodes.append( Node(x, y, index+1) )
        
    nodes.sort(key=lambda node: (-node.y, node.x))
    root = nodes[0]
    
    for node in nodes[1:]:
        insert(root, node)
    return root 
       
def preorder(node: Node, result):
    if not node:
        return
    result.append(node.index)
    preorder(node.left, result)
    preorder(node.right, result)
    
def postorder(node: Node, result):
    if not node:
        return
    postorder(node.left, result)
    postorder(node.right, result)
    result.append(node.index)
    

def solution(nodeinfo):
    root = buildTree(nodeinfo)
    
    resultOfPre = []
    preorder(root, resultOfPre)
    
    resultOfPost = []
    postorder(root, resultOfPost)
    
    return [resultOfPre, resultOfPost]