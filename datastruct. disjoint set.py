class DisjoinSet(object):
    def __init__(self, num) -> None:
        self.roots = list(range(num))
    
    def findroot(self, i):
        root = i
        while root != self.roots[root]:
            root = self.roots[root]
        while i != self.roots[i]:
            tmp = self.roots[i]
            self.roots[i] = root
            i = tmp
        return root

    def connected(self, p, q):
        return self.findroot(p) == self.findroot(q)
    
    def union(self, p, q):
        qroot = self.findroot(p)
        proot = self.findroot(q)
        self.roots[proot] = qroot