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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        boolean result;
        if (root == null || subRoot == null) {
            result = false;
        } else {
            result = helper(root, subRoot);
            if (!result) {
                result = isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
            }
        }
        return result;
    }

    public boolean helper(TreeNode root, TreeNode subRoot) {
        boolean result;
        if (root == null && subRoot == null) {
            result = true;
        } else if (root == null || subRoot == null) {
            result = false;
        } else {
            if (root.val == subRoot.val) {
                result = helper(root.left, subRoot.left) && helper(root.right, subRoot.right);
            } else {
                result = false;
            }
        }
        return result;
    }



}
