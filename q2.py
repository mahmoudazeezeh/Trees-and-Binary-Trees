class TreeNode:
    def __init__(self, v=0, l=None, r=None):
        self.v = v
        self.l = l
        self.r = r

def is_balanced(r):
    def chk(n):  
        if not n:
            return (True, 0)
        lb, lh = chk(n.l)
        rb, rh = chk(n.r)
        bal = lb and rb and abs(lh - rh) <= 1
        h = max(lh, rh) + 1
        return (bal, h)
    return chk(r)[0]

# test1
t1 = TreeNode(1)
t1.l = TreeNode(2)
t1.r = TreeNode(3)
print("balanced?", is_balanced(t1))  

# test2
t2 = TreeNode(1)
t2.l = TreeNode(2)
t2.l.l = TreeNode(3)
print("balanced?", is_balanced(t2))  
