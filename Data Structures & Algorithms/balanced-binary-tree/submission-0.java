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
    public boolean isBalanced(TreeNode root) {
        boolean[] arr = {true};
        isBalanced(root, arr);
        return arr[0];
    }
    public int isBalanced(TreeNode root, boolean[] arr) {
        int result;
        if (root == null || arr[0] == false) {
            result = 0;
        } else {
            int leftDepth = isBalanced(root.left, arr);
            int rightDepth = isBalanced(root.right, arr);
            result = 1 + (leftDepth > rightDepth ? leftDepth : rightDepth);
            if (Math.abs(leftDepth - rightDepth) > 1) {
                arr[0] = false;
            }
        }
        return result;
    }
}
