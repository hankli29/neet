public class Solution {
    public bool hasDuplicate(int[] nums) {
        System.Collections.Generic.HashSet<int> list = new System.Collections.Generic.HashSet<int>();
        foreach (int i in nums) 
        {
            if (list.Contains(i)) return true;
            list.Add(i);
        }
        return false;
    }
}
