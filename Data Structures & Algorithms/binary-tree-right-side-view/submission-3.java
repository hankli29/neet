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
    public List<Integer> rightSideView(TreeNode root) {
        HashMap <Integer, int[]> temp = new HashMap<>();
        rightSideView(root, temp, 0, 0, 100);
        List<Integer> result = new ArrayList<>();
        for (Integer i: temp.keySet()) {
            result.add(temp.get(i)[1]);
        }
        return result;
    }
    public void rightSideView(TreeNode root, HashMap <Integer, int[]> temp, int depth, int width, int change) {
        if (root == null) {
            return;
        }
        System.out.println(root.val+" "+ depth+" "+ width);
        if (!temp.containsKey(depth)) {
            temp.put(depth, new int[]{width, root.val});
        }
        else if ((temp.get(depth))[0] < width) {
            temp.put(depth, new int[]{width, root.val});
        }
        rightSideView(root.left, temp, depth+1, width-change, change - 1);
        rightSideView(root.right, temp, depth+1, width+change, change - 1);
    }
}
