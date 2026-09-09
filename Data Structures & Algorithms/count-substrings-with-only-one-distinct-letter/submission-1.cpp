class Solution {
public:
    int countLetters(string s) {
        int start = 0;
        int result = 0;
        for (int i = 1; i <= s.size(); i++) {
            if (i == s.size() || s[i] != s[start]) {
                result += (i-start) * (i-start+1)/2;
                start = i;
            }
        }
        return result;
    }
};
