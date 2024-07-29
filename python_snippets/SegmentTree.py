"""
Segment tree from definition, can be optimized by array.
"""
class SNode:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.val = 0
        self.left_child = None
        self.right_child = None


class SegmentTree:
    # all the index used in the tree are inclusive.
    def __init__(self, index_min: int, index_max: int):
        self.root = SNode(index_min, index_max)
        self._build(self.root)

    def _build(self, node: SNode):
        if node.l == node.r:
            return
        m = (node.l + node.r) // 2
        node.left_child = SNode(node.l, m)
        node.right_child = SNode(m + 1, node.r)
        self._build(node.left_child)
        self._build(node.right_child)
        return node

    def update(self,  idx: int, val: int,node: SNode=None):
        if node==None: node=self.root
        if node.l == node.r:
            node.val = val
            return
        m = (node.l + node.r) // 2
        if idx <= m:
            self.update( idx, val,node.left_child)
        else:
            self.update( idx, val,node.right_child)
        node.val = node.left_child.val + node.right_child.val

    def sum(self,  left: int, right: int, node: SNode=None) -> int:
        if node==None: node=self.root
        if right < node.l or node.r < left:
            return 0
        if left <= node.l and node.r <= right:
            return node.val
        return self.sum( left, right,node.left_child) + self.sum(
             left, right,node.right_child
        )
    
# Example driver code
if __name__ == "__main__":
    tree = SegmentTree(0,5)
    tree.update(0,3)
    tree.update(1,1)
    tree.update(2,4)
    tree.update(3,2)
    tree.update(4,5)

    print("Sum of SegmentTree")
    print(tree.sum(0,5))
    print()

    tree.update(2,0)

    print("Inorder traversal of the Red-Black Tree after deleting 4")
    print(tree.sum(1,3))

    print()