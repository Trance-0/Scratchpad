"""
Interval tree from definition, can be optimized by array.
"""
class INode:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        # val is count of segments within the range
        self.val = 0
        self.left_child = None
        self.right_child = None


class IntervalTree:
    # all the index used in the tree are inclusive.
    def __init__(self):
        self.root = None

    # use low as axis
    def insert(self,  lo:int, hi:int, node:INode=None):
        if node is None:
            node=INode(lo,hi)
            node.val=1
            return node
        if lo<node.l:
            node.left_child=self.insert(lo,hi,node.left_child)
        else:
            node.right_child=self.insert(lo,hi,node.right_child)
            node.val+=1
        node.r=max(node.r,hi)
        return node

    def sum(self,  left: int, right: int, node: INode=None) -> int:
        if node is None or node.r < left:
            return 0
        if left <= node.l and node.r <= right:
            return node.val
        return self.sum( left, right,node.left_child) + self.sum(
             left, right,node.right_child
        )
    
# Example driver code
if __name__ == "__main__":
    tree = IntervalTree()
    tree.root=tree.insert(0,3,tree.root)
    tree.root=tree.insert(1,1,tree.root)
    tree.root=tree.insert(2,4,tree.root)
    tree.root=tree.insert(2,3,tree.root)
    tree.root=tree.insert(4,5,tree.root)

    print("Sum of IntervalTree")
    print(tree.sum(0,5,tree.root))
    print()

    
    tree.root=tree.insert(1,2,tree.root)

    print("Inorder traversal of the Red-Black Tree after deleting 4")
    print(tree.sum(0,4,tree.root))

    print()