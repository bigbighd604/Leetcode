#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) {
        if (x == 0) return true;
        if (x < 0 || x % 10 == 0) return false;
        int a = x, b = 0;
        while(a > b) {
            b = b * 10 + a % 10;
            a /= 10;
        }
        if(a == 0) return (x == b);
        return (a == b) || a == (b / 10);        
    }
};


int main(int argc, char** argv) {
  Solution s;
  int a[4] = {121, 1231, 1, -1};
  for (int i = 0; i < 4; i++) {
    if (s.isPalindrome(a[i])) {
      std::cout << a[i] << " Pass" << std::endl;
    } else {
      std::cout << a[i] << " Fail" << std::endl;
    }
  }
}
