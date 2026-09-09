
public class Solution {
    public bool hasDuplicate(int[] nums) {
var hashTable = new System.Collections.Hashtable();
foreach(int i in nums)
{
    if (hashTable.Contains(i))
    {
return true;
    }
    hashTable.Add(i, i);
}
return false;
    }
}
