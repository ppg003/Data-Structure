class TreeNode:
    def __init__(self, lchd=None, val=None, rchd=None):
        self.lchd = lchd
        self.val = val
        self.rchd = rchd


class BTree:
    def __init__(self, root=TreeNode(val=0)):
        self.root = root

    def BL_QianXu(self, node):
        if node is None:
            return
        print(node.val)
        self.BL_QianXu(node.lchd)
        self.BL_QianXu(node.rchd)

    def BL_ZhongXu(self, node):
        if node is None:
            return
        self.BL_ZhongXu(node.lchd)
        print(node.val)
        self.BL_ZhongXu(node.rchd)

    def BL_HouXu(self, node):
        if node is None:
            return
        self.BL_HouXu(node.lchd)
        self.BL_HouXu(node.rchd)
        print(node.val)

    def BL_Cengxu(self, queue):
        if len(queue) == 0:
            return
        queue_next = []
        for i in range(len(queue)):
            print(queue[i].val)
            if queue[i].lchd is not None:
                queue_next.append(queue[i].lchd)
            if queue[i].rchd is not None:
                queue_next.append(queue[i].rchd)
        self.BL_Cengxu(queue_next)




nK = TreeNode(val="K")
nJ = TreeNode(val="J")
nI = TreeNode(val="I")
nH = TreeNode(val="H")
nG = TreeNode(val="G")
nF = TreeNode(val="F", rchd=nK)
nE = TreeNode(val="E", rchd=nJ)
nD = TreeNode(lchd=nH, val="D", rchd=nI)
nC = TreeNode(lchd=nF, val="C", rchd=nG)
nB = TreeNode(lchd=nD, val="B", rchd=nE)
nRoot = TreeNode(lchd=nB, val="A", rchd=nC)

tree = BTree(root=nRoot)
# tree.BL_QianXu(nRoot)
# tree.BL_ZhongXu(nRoot)
# tree.BL_HouXu(nRoot)
tree.BL_Cengxu([nRoot])
