class Solution {
public:
    string largestNumber(vector<int> &num) {
        vector<string> ss;
        for (int i = 0; i < num.size(); i++) {
            ss.push_back(to_string(num[i]));
        }
        sort(ss.begin(), ss.end(), compareFunc);
        // Since we sort in descending order, if first
        // element is "0", we get an vector full of 0 input
        if (ss[0] != "0") {
            string result;
            for (int i = 0; i < ss.size(); i++) {
                result += ss[i];
            }
            return result;            
        }
        return "0";
    }
private:
    static bool compareFunc(const string &s1, const string &s2) {
        return s1 + s2 > s2 + s1;
    }
};
