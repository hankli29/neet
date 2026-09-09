public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        System.Collections.Hashtable first = new System.Collections.Hashtable();
        System.Collections.Hashtable second = new System.Collections.Hashtable();
        foreach(char c in s)
        {
            if (first.ContainsKey(c)) 
            {
                first[c] = (int)first[c] + 1;
            }
            else {
                first.Add(c, 1);
            }
        }
        foreach(char c in t)
        {
            if (second.ContainsKey(c)) 
            {
                second[c] = (int)second[c] + 1;
            }
            else {
                second.Add(c, 1);
            }
        }
        foreach( System.Collections.DictionaryEntry de in first )
        {
            if (second.ContainsKey(de.Key))
            {
                if ((int)second[de.Key] != (int)de.Value) 
                {
                    return false;
                }
            } else return false;
        }
        return true;
    }
}