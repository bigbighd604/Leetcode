#include <string.h>
#include <iostream>
#include <string>
#include <map>

using namespace std;

class Solution {
  public:
    int lengthOfLongestSubstring2(string s) {
      int max = 0;
      map<char, int> m;
      int last_repeat_pos = -1;

      int size = s.size();
      if (size == 1) return 1;

      for (int i = 0; i < size; i++) {
        // Here the last_repeat_pos < m[s[i]] is required, because
        // a char may appear first but get a duplicate later, i.e
        // pguxhxdipji # p--x-x--p, need to make sure we don't rewind
        // last_repeat_pos when we point it to first 'x' already. 
        if (m.find(s[i]) != m.end() && last_repeat_pos < m[s[i]]) {
          // we delayed the maximum check, the maximum number appeared
          // previous cycle, so here need to minus by one
          if (i - last_repeat_pos  - 1> max) {
            max = i - last_repeat_pos - 1;
          }
          last_repeat_pos = m[s[i]];
        }
        m[s[i]] = i;
      }
      // when the longest substring is the suffix, we need a separate
      // check because the for loop can not catch this case.
      if (size - last_repeat_pos  - 1> max) {
        max = size - last_repeat_pos - 1;
      }
      return max;
    }

    int lengthOfLongestSubstring(string s) {
      int max = 0;
      map<char, int> m;
      int last_repeat_pos = -1;

      for (int i = 0; i < s.size(); i++) {
        if (m.find(s[i]) != m.end() && last_repeat_pos < m[s[i]]) {
            last_repeat_pos = m[s[i]];
        }
        if (i - last_repeat_pos > max) {
          max = i - last_repeat_pos;
        }
        m[s[i]] = i;
      }
      return max;
    }

    // 5X speed up comparing to map version.
    int lengthOfLongestSubstring3(string s) {
      int max = 0;
      const int MAX_CHARS = 256;
      int m[MAX_CHARS];
      memset(m, -1, sizeof(m));
      int last_repeat_pos = -1;

      for (int i = 0; i < s.size(); i++) {
        if (m[s[i]]!= -1 && last_repeat_pos < m[s[i]]) {
            last_repeat_pos = m[s[i]];
        }
        if (i - last_repeat_pos > max) {
          max = i - last_repeat_pos;
        }
        m[s[i]] = i;
      }
      return max;
    }
};


int main(int argc, char** argv) {
  Solution solution;
  string s = "abcabcbb";
  cout << s << " : " << solution.lengthOfLongestSubstring(s) << endl;
  cout << s << " : " << solution.lengthOfLongestSubstring2(s) << endl;

  s = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco";
  cout << s << " : " << solution.lengthOfLongestSubstring(s) << endl;
  cout << s << " : " << solution.lengthOfLongestSubstring2(s) << endl;
  cout << s << " : " << solution.lengthOfLongestSubstring3(s) << endl;

  s = "qopubjguxhxdipfzwswybgfylqvjzhar";
  cout << s << " : " << solution.lengthOfLongestSubstring(s) << endl;
  cout << s << " : " << solution.lengthOfLongestSubstring2(s) << endl;
  cout << s << " : " << solution.lengthOfLongestSubstring3(s) << endl;

  if (argc > 1) {
    s = argv[1];
    cout << s << " : " << solution.lengthOfLongestSubstring(s) << endl;
    cout << s << " : " << solution.lengthOfLongestSubstring2(s) << endl;
  }

  return 0;
}
