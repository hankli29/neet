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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode result;
        if (root.val >= q.val && root.val <= p.val || root.val <= q.val && root.val >= p.val) {
                result = root;
            }
        else {
            if (p.val > root.val) {
                result = lowestCommonAncestor(root.right, p, q);
            } else {
                result = lowestCommonAncestor(root.left, p, q);
            }
        }
        
            
        return result;
    }
}