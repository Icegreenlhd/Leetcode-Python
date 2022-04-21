<!-- #region -->
# Leetcode
HaodongLin work on leetcode, code in python by jupyter notebook.

## Before Add New Answer
There are some information for you to know:
1. Install jupyter notebook and jupytext by pip
   ```shell
   pip install jupyter
   pip install jupytext
   ```
2. Use the same pattern name for the file, the white sapce in leetcode can be maintained, `<number>.<english title>.ipynb`, like, `0001. Two Sum.ipynb`
3. You can translate the jupyter file `.ipynb` into python file `.py` by
   ```shell
   jupytext --set-formats ipynb,py <filename>.ipynb
   ```

## Pretest By Yourself
```python
import unittest


class LeetcodeTest(unittest.TestCase):
    solution = getattr(Solution(), dir(Solution)[-1])

    def test_case1(self):
        test_input = 
        test_output = 
        self.assertEqual(self.solution(test_input), test_output)

unittest.main(argv=['ignored', '-v'], exit=False)
```
Tree initialization
```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def init_bst(tree):
    t = tree.copy()
    root = TreeNode(t.pop(0))
    tree_list = [root]
    while len(t) > 0:
        size = len(tree_list)
        for i in range(size):
            temp = tree_list.pop(0)
            if temp != None:
                left = t.pop(0) if len(t) > 0 else None
                temp.left  = TreeNode(left) if left else None
                right = t.pop(0) if len(t) > 0 else None
                temp.right  = TreeNode(right) if right else None
                tree_list.append(temp.left)
                tree_list.append(temp.right)
    return root
```
<!-- #endregion -->
