/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        boolean result;
        if (p == null && q == null) {
            result = true;
        } else if (p == null || q == null) {
            result = false;
        } else {
            if (p.val == q.val) {
                result = isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
            } else {
                result = false;
            }
        }
        return result;
    }
}
