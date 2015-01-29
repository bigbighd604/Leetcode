#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution {
  public:
    bool isValid(string s) {
        int size = s.size();
        // Empty string means 0 pairs
        if (size ==0) return true;
        // Odd number chars must be invalid
        if (size % 2 == 1) return false;
        
        map<char, char> charMap;
          charMap['('] = ')';
          charMap['{'] = '}';
          charMap['['] = ']';
//        // Different ways to add items to map
//        // insert using make_pair
//        charMap.insert(make_pair('(', ')'));
//        charMap.insert(make_pair('{', '}'));
//        charMap.insert(make_pair('[', ']'));
//        // C++98 doesn't support this initialization format.
//        map<char, char> charMap = {
//            {'(', ')'},
//            {'{', '}'},
//            {'[', ']'}
//        };

        vector<char> stack;
        stack.push_back(s[0]);
        for (int i = 1; i < s.size(); i++) {
            char cur = s[i];
            if (cur == '(' || cur == '{' || cur == '[') {
                // It's fine to push lots of opening brackets.
                stack.push_back(cur);
            } else {
                // Right hand side brackets must be paired.
                char top = stack.back();
                // For s == ")}{({))[{{[}", the 
                // charMap[top] will insert an entry and return an "",
                // which will fail the compare, side effect to cover edge case.
                if (charMap[top] != s[i]) {
                    return false;
                }
                // This is a pair, pop last item, pop_back() no return value.
                stack.pop_back();
            }
        }
        // There is left overs.
        // if (stack.size() >0) return false;
        // empty() is preferred comparing size() for containers, because
        // empty() is guaranteed constant O(1) time, per:
        // http://stackoverflow.com/questions/743197/size-vs-empty-in-vector-why-empty-is-preferred
        if (stack.empty()) return true;
        return false;
    }
};


int main(int argc, char **argv) {
  Solution s;
  string input = "()[{()}]((({{}})))";
  bool expect = true;
  bool result = s.isValid(input);
  if (result != expect) {
    cout << "expect: " << expect << " result: " << result << endl;
  }
  return 0;
}
