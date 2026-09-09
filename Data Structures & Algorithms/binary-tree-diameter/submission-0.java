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
    public int diameterOfBinaryTree(TreeNode root) {
        int[] arr = {0};
        diameterOfBinaryTree(root, arr);
        return arr[0];
    }
    public int diameterOfBinaryTree(TreeNode root, int[] arr) {
        int result = 0;
        if (root == null) {
            return result;
        } else {
            int maxLeft = diameterOfBinaryTree(root.left, arr);
            int maxRight = diameterOfBinaryTree(root.right, arr);
            result = 1 + (maxLeft > maxRight ? maxLeft : maxRight);
            if (maxLeft + maxRight > arr[0]) {
                arr[0] = maxLeft + maxRight;
            }
        }
        return result;
    }
}
