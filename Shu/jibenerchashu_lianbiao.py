class TreeNode:
    def __init__(self, lchd=None, val=None, rchd=None):
        self.lchd = lchd
        self.val = val
        self.rchd = rchd


class BTree:
    root = None

    def __init__(self, root=TreeNode(val=0)):
        self.root = root

    def BL_QianXu(self, node=root):
        if node is None:
            return
        print(node.val)
        self.BL_QianXu(node.lchd)
        self.BL_QianXu(node.rchd)

    def BL_ZhongXu(self):
        pass

    def BL_HouXu(self):
        pass

    def BL_Cengxu(self):
        pass


nK = TreeNode(val="K")
nJ = TreeNode(val="J")
nI = TreeNode(val="I")
nH = TreeNode(val="H")
nG = TreeNode(val="G")
nF = TreeNode(val="F", rchd=nK)
nE = TreeNode(val="E", rchd=nJ)
nD = TreeNode(lchd=nH, val="", rchd=nI)
nC = TreeNode(lchd=nF, val="C", rchd=nG)
nB = TreeNode(lchd=nD, val="B", rchd=nE)
nRoot = TreeNode(lchd=nB, val="A", rchd=nC)

tree = BTree(root=nRoot)
tree.BL_QianXu()
